import os

CAPTION = "Art by user"  # Change as needed
image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".gif")
skip_files = {"fanart_output.txt", "script.py"}

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "fanart_output.txt")

with open(output_path, "w", encoding="utf-8") as out:
    for filename in sorted(os.listdir(script_dir)):
        if (
            filename.lower().endswith(image_extensions)
            and filename not in skip_files
        ):
            name_no_ext = os.path.splitext(filename)[0]
            html = f'''<div class="fanart-item" data-img="{filename}" data-caption="{CAPTION}">
    <img src="{filename}" alt="Fan Art {name_no_ext}">
    <div class="fanart-caption">{CAPTION}</div>
</div>

'''
            out.write(html)