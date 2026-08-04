import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = "https://claude.ai/code/artifact/71efed19-774b-432e-adcf-6402d845964c"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="#12181a", back_color="#ffffff")
img.save("/tmp/claude-0/-home-user-SA-TECH/35d3f060-ad8f-5637-b8f7-04a8c121d28e/scratchpad/qr/sa-tech-qrcode.png")
print("saved", img.size)
