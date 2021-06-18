import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

# Please read this documentation
# https://pypi.org/project/pyzbar/
#1.
#sudo apt-get install libzbar0
#2.
#pip install pyzbar


img = cv2.imread('fotos/qr28.jpg')

# print(dir(decode(img)))
code1 = ''
# Detect just QR Code
for code in decode(img,symbols=[ZBarSymbol.QRCODE]):
    #print(code)
    code1 = code.data.decode('utf-8')
    print(code1)
    print(type(code1))


# # image = cv2.imread('qr12.jpg')
image = img
height, width = image.shape[:2]

# 8 bpp by considering just the blue channel
code_blue = decode((image[:, :, 0].astype('uint8').tobytes(), width, height),symbols=[ZBarSymbol.QRCODE])
#print(code[0].data)
#print(code_blue[0].data.decode('utf-8'))

# 8 bpp by converting image to greyscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
code_grey = decode((grey.tobytes(), width, height),symbols=[ZBarSymbol.QRCODE])
#print(code_grey[0].data.decode('utf-8'))


if code1 or code_blue or code_grey:
    print('Si Hay QR Code')
else: 
    print('No Hay QR Code')