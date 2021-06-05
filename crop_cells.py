from PIL import Image
import os

for bp_id in [f"{i:03}" for i in range(1, 100+1)]:
    img = Image.open(f"images\#BP{bp_id}.jpg")
    w, h = 100-2, 100-2
    x0, y0 = 8, 6
    gap = 10
    n = 0
    for k in range(2):
        for i in range(3):
            for j in range(2):
                x, y = x0+293*k+(w+gap)*j, y0+(h+gap)*i
                area = (x, y, x+w, y+w)
                cropped_img = img.crop(area)
                # cropped_img.show()
                file_path = os.path.join(r"cells", f"#BP{bp_id}_{n}.jpg")
                with open(file_path, 'wb') as f:
                    cropped_img.save(f, "JPEG", quality=100)
                n += 1
