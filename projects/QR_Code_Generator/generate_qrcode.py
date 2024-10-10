import qrcode

qr = qrcode.QRCode(
    # The version is an integer from 1 to 40 that controls the size of the QR Code and Complicated picture
    version = 15,

    # The error_correction parameter controls the error correction used for the QR Code
    # ERROR_CORRECT_L
    # About 7% or less errors can be corrected.

    # ERROR_CORRECT_M (default)
    # About 15% or less errors can be corrected.

    # ERROR_CORRECT_Q
    # About 25% or less errors can be corrected.

    # ERROR_CORRECT_H.
    # About 30% or less errors can be corrected.
    error_correction=qrcode.constants.ERROR_CORRECT_L, 

    # The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
    box_size = 10, # Size of the box where QR code will be displyed 

    # The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
    border = 5, # It is white part of image - border in all 4 sides with white color
    
)

# data = "https://www.youtube.com/@chandrasekharreddymaram"
data = input("Enter anything to generate QR Code: ")

qr.add_data(data)
qr.make(fit=True)
# fill_color and back_color can change the background and the painting color of the QR, 
# when using the default image factory. Both parameters accept RGB color tuples.
img = qr.make_image(fill_color="black", back_color="White") 
img.save("test.png")