import qrcode
import sys

# Default to the GitHub Pages URL for your repo; can override with an argument
default_url = 'https://csathaye-prog.github.io/BitwardsLanding/'
url = sys.argv[1] if len(sys.argv) > 1 else default_url

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
img.save('qr-code.png')
print('Saved qr-code.png for', url)
