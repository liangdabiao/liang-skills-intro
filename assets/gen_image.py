#!/usr/bin/env python3
"""小黑手绘风格配图生成器（agnes-image-2.0-flash，curl 实现更稳健）"""
import argparse, json, os, subprocess, sys, tempfile, time

API = "https://apihub.agnes-ai.com/v1/images/generations"
KEY = "sk-uq9rgIyiNpcGze4mPZEGJkPynKLNAhE3nk6xu0N0Ry5BOdfu"


def api_call(prompt: str) -> dict:
    payload = {
        "model": "agnes-image-2.0-flash",
        "prompt": prompt,
        "size": "1024x768",
        "extra_body": {"response_format": "url"},
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
        payload_path = f.name

    try:
        cmd = [
            "curl", "-sk", "--request", "POST",
            "--url", API,
            "--header", "Authorization: Bearer " + KEY,
            "--header", "Content-Type: application/json",
            "--data", "@" + payload_path,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            raise RuntimeError(f"curl POST failed: {result.stderr}")
        return json.loads(result.stdout)
    finally:
        try:
            os.unlink(payload_path)
        except OSError:
            pass


def download(url: str, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cmd = ["curl", "-sk", "--max-time", "120", "-o", out_path, url]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=150)
    if result.returncode != 0:
        raise RuntimeError(f"curl download failed: {result.stderr}")


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
