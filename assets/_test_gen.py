import json, urllib.request, urllib.error, sys

API = "https://apihub.agnes-ai.com/v1/images/generations"
KEY = "sk-uq9rgIyiNpcGze4mPZEGJkPynKLNAhE3nk6xu0N0Ry5BOdfu"

prompt = (
    "Generate one standalone 16:9 horizontal Chinese article illustration.\n"
    "Visual DNA: Pure white background. Minimalist black hand-drawn line art. "
    "Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue "
    "handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, "
    "no shadows, no paper texture, no complex background, no commercial vector style, "
    "no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.\n"
    "Recurring IP character required: 小黑, a small solid-black absurd creature with white "
    "dot eyes, tiny thin legs, blank serious expression, slightly uneven hand-drawn body shape. "
    "小黑 must perform the core conceptual action, not decorate the scene. Make 小黑 serious, "
    "deadpan, and slightly bizarre, not cute.\n"
    "Theme: 把任意图片变成照着拼的拼豆图纸\n"
    "Structure type: 输入输出闭环\n"
    "Core idea: 小黑把一张彩色照片变成一格格标好品牌色号的拼豆施工图\n"
    "Composition: 左边小黑双手举着一张照片，照片被网格线分割成许多小格子；右边是一张拼豆图纸，"
    "每格写着色号，地上散落几颗拼豆。中间用橙色箭头表示量化流向。\n"
    "Suggested elements: 照片 / 网格线 / 拼豆图纸 / 散落豆子\n"
    "Chinese handwritten labels: 素材图 / 量化 / 拼豆图纸 / 色号\n"
    "Color use: Black for main line art and 小黑. Orange for the flow arrow. "
    "Red for the final 拼豆图纸 result. Blue for a small note.\n"
    "Constraints: One image explains only one core structure. Keep main subject 40%-60% of canvas. "
    "Preserve at least 35% blank white space. At most 5-8 short handwritten Chinese labels. "
    "No title in top-left corner. Do not write structure type on image. Not a formal diagram. "
    "Invent a fresh visual metaphor. Clear but not instructional, interesting but not childish, strange but clean."
)

payload = {
    "model": "agnes-image-2.0-flash",
    "prompt": prompt,
    "size": "1024x768",
    "extra_body": {"response_format": "url"},
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(API, data=data, method="POST")
req.add_header("Authorization", "Bearer " + KEY)
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    print("HTTP_OK")
    print(json.dumps(body, ensure_ascii=False)[:800])
except urllib.error.URLError as e:
    print("URLERROR:", e)
except Exception as e:
    print("ERR:", repr(e))
