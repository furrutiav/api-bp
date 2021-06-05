import requests
import io
from PIL import Image
import os
import json

file_tag_names = open("tag_names.json")
tag_names = json.load(file_tag_names)

for bp_id in [f"{i:03}" for i in range(1, 100+1)]:
    full_url = tag_names["gifs"]+f"p{bp_id}.gif"
    print("url:", full_url)
    r = requests.get(full_url, headers={"User-Agent": "XY"})
    print("status:", r.status_code)

    image_content = r.content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('1')
    file_path = os.path.join(r"images", f"#BP{bp_id}.jpg")
    with open(file_path, 'wb') as f:
        image.save(f, "JPEG", quality=100)


