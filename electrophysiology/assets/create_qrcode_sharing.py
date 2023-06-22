import qrcode
from PIL import Image

# User inputs
in_url = "https://colab.research.google.com/drive/1ix5N38T4tl9ih4u2pSt-tuu3R5WCuL2W?usp=sharing"
in_logo = "electrophysiology/assets/FAUHS Research Program.png"
out_qr = "electrophysiology/assets/qr_code_lab_skills_workshop.png"

# Process logo
logo = Image.open(in_logo)

basewidth = 530
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# Generate QR code
QRcode.add_data(in_url)

QRcode.make()
QRimg = QRcode.make_image(fill_color="black", back_color="white") #.convert("RGB")

pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# Save to file
QRimg.save(out_qr)
print('QR code generated.')
