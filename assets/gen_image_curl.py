#!/usr/bin/env python3
"""小黑手绘风格配图生成器（curl 兜底实现，规避 Python urllib 的 SSL 重协商 EOF）。

与 gen_image.py 保持相同 CLI：--prompt / --out / --retries
API response_format=url 时返回 data[0].url，再用 curl 下载。
"""
import argparse
import json
import os
import subprocess
import sys
import time

API = "https://apihub.agnes-ai.com/v1/images/generations"
KEY = "sk-uq9rgIyiNpcGze4mPZEGJkPynKLNAhE3nk6xu0N0Ry5BOdfu"


def api_call(prompt: str) -> dict:
    payload = {
        "model": "agnes-image-2.0-flash",
        "prompt": prompt,
        "size": "1024x768",
        "extra_body": {"response_format": "url"},
    }
    # 用 curl 绕过 Python ssl 重协商失败
    proc = subprocess.run(
        [
            "curl", "-sk", "--request", "POST", API,
            "--header", "Authorization: Bearer " + KEY,
            "--header", "Content-Type: application/json",
            "--data", json.dumps(payload, ensure_ascii=False),
        ],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"curl failed: {proc.stderr[:300]}")
    body = json.loads(proc.stdout)
    if "data" not in body or not body.get("data"):
        raise RuntimeError(f"no data in response: {proc.stdout[:500]}")
    return body


def download(url: str, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    proc = subprocess.run(
        ["curl", "-sk", "--request", "GET", url, "--output", out_path],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"download failed: {proc.stderr[:300]}")
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        raise RuntimeError("downloaded file empty")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()

    last_err = None
    for attempt in range(1, args.retries + 1):
        try:
            body = api_call(args.prompt)
            url = body.get("data", [{}])[0].get("url")
            if not url:
                raise RuntimeError(f"no url in response: {json.dumps(body, ensure_ascii=False)[:500]}")
            download(url, args.out)
            print(f"OK:{args.out}")
            return
        except Exception as e:
            last_err = e
            if attempt < args.retries:
                time.sleep(2 * attempt)
    print(f"ERROR:{last_err}")
    sys.exit(1)


if __name__ == "__main__":
    main()
