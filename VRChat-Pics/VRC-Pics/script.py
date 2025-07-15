import os

CAPTION = "Provided by "
image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".gif")
skip_files = {"output.txt", "script.py"}

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")

with open(output_path, "w", encoding="utf-8") as out:
    for filename in sorted(os.listdir(script_dir)):
        if (
            filename.lower().endswith(image_extensions)
            and filename not in skip_files
        ):
            name_no_ext = os.path.splitext(filename)[0]
            html = f'''<div class="photo-item" data-img="VRC-Pics/{filename}" data-caption="{CAPTION}">
    <img src="VRC-Pics/{filename}" alt="VRChat Photo {name_no_ext}">
    <div class="photo-caption">{CAPTION}</div>
</div>

'''
            out.write(html)