"""
QR codes for the useful-links page, the AspenAutoKit repository and
Vince's LinkedIn profile.

Writes a high-resolution PNG and a vector SVG for each (the SVG scales
cleanly on a poster or in Word/PowerPoint).

    pip install "qrcode[pil]"
    python make_qr.py
"""

import qrcode
import qrcode.image.svg

TARGETS = {
    # the "useful links" page — point this at wherever index.html is hosted
    "qr_links":        "https://baileyladd01.github.io/",
    "qr_aspenautokit": "https://github.com/BaileyLadd01/AspenAutoKit-opensource",
    "qr_linkedin":     "https://www.linkedin.com/in/vincent-bailey-ladd/",
}


def build(url, factory=None):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # ~15% damage tolerance
        box_size=40,     # pixels per module (PNG only)
        border=4,        # quiet zone in modules; 4 is the spec minimum
        image_factory=factory,
    )
    qr.add_data(url)
    qr.make(fit=True)    # smallest QR version that holds the URL
    return qr.make_image(fill_color="black", back_color="white") \
        if factory is None else qr.make_image()


for name, url in TARGETS.items():
    build(url).save(f"{name}.png")
    build(url, qrcode.image.svg.SvgPathImage).save(f"{name}.svg")
    print(f"wrote {name}.png and {name}.svg for {url}")
