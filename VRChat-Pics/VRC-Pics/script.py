from pathlib import Path
from html import escape



#Change DEFAULT_CAPTION below if needed.
#Run: python script.py
#Open output.txt, check it, then copy everything in it.
# Paste it inside:
#       <div class="gallery">
#           ...PASTE HERE...
#       </div>

DEFAULT_CAPTION = "Provided by Mocha"

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif",
}

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = SCRIPT_DIR / "output.txt"


def make_card(image_path: Path) -> str:
    """Create one gallery card for the modern VR Famo VRChat gallery."""

    filename = image_path.name

    # HTML escaping keeps unusual filenames/captions from breaking the page.
    safe_filename = escape(filename, quote=True)
    safe_caption = escape(DEFAULT_CAPTION, quote=True)

    # A simple accessible description based on the filename.
    readable_name = image_path.stem.replace("_", " ").replace("-", " ")
    safe_alt = escape(f"VRChat community photo - {readable_name}", quote=True)

    return f"""<button
    class="photo-card"
    type="button"
    data-img="VRC-Pics/{safe_filename}"
    data-caption="{safe_caption}"
    aria-label="Open {safe_caption}"
>
    <img
        src="VRC-Pics/{safe_filename}"
        alt="{safe_alt}"
        loading="lazy"
    >
    <span>{safe_caption}</span>
</button>"""


def main():
    images = sorted(
        (
            path
            for path in SCRIPT_DIR.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        ),
        key=lambda path: path.name.lower(),
    )

    if not images:
        OUTPUT_FILE.write_text(
            "<!-- No gallery images were found in VRC-Pics. -->\n",
            encoding="utf-8",
        )
        print("No images found.")
        print(f"Checked: {SCRIPT_DIR}")
        print(f"Created: {OUTPUT_FILE.name}")
        return

    output = "\n\n".join(make_card(image) for image in images)
    OUTPUT_FILE.write_text(output + "\n", encoding="utf-8")

    print(f"Done! Generated {len(images)} gallery cards.")
    print(f"Review them in: {OUTPUT_FILE}")
    print()
    print("Then copy everything from output.txt and paste it")
    print('between <div class="gallery"> and </div> in VRChat-Pics/index.html.')


if __name__ == "__main__":
    main()