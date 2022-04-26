# generates qr code for a given url

import qrcode
from qrcode.image.styledpil import StyledPilImage

url = "https://github.com/MattUebel/git-good-with-splunk"
image = "../docs/images/trust_fez.png"

# generate qr code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)

qr.make(fit=True)
qrcode_image = qr.make_image(image_factory=StyledPilImage, embeded_image_path=image)

# write image to disk
qrcode_image.save("git-good-with-splunk.png")
