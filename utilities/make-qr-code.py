import argparse
import os
import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image, ImageDraw, ImageFont

# parse command-line arguments
parser = argparse.ArgumentParser(description='Generate QR code for a given URL')
parser.add_argument('url', type=str, help='the URL to encode')
parser.add_argument('image', type=str, help='the filename of the image to embed')
parser.add_argument('output', type=str, help='the filename to save the QR code image as')
parser.add_argument('label', type=str, help='the label to add at the bottom of the QR code')
args = parser.parse_args()

# Resize the embedded image
embedded_image = Image.open(args.image)

# generate qr code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # Increase box_size for higher resolution
    border=4,
)
qr.add_data(args.url)
qr.make(fit=True)

print(f"making qr code for {args.url} with image {args.image} and saving to {args.output}")

qrcode_image = qr.make_image(image_factory=StyledPilImage, embeded_image_path=args.image)

# Add label at the bottom of the QR code
base = qrcode_image.convert('RGBA')  # Convert qr code to RGBA to ensure compatibility
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))  # Create a blank image with the same size

# Choose a font type and size
fnt = ImageFont.truetype('/Library/Fonts/Roboto-Regular.ttf', 30)
d = ImageDraw.Draw(txt)

# Calculate width and height of the text to center it
bbox = d.textbbox((0, 0), args.label, font=fnt)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
W, H = base.size
d.text(((W-w)/2, H-h-5), args.label, font=fnt, fill=(0, 0, 0, 255))

out = Image.alpha_composite(base, txt)

# write image to disk
out.save(args.output, 'PNG')
