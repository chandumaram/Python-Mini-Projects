import qrcode

# Link to open WCC2 app directly in the Play Store app
# 1) com.nautilus.realcricket 2) com.nextwave.wcc2
play_store_app_url = "https://play.google.com/store/apps/details?id=com.nautilus.realcricket"

# Generate QR code
qr = qrcode.make(play_store_app_url)

# Save the QR code as an image file
qr.save("app_playstore_qr_code.png")

print("QR code generated and saved as 'app_playstore_qr_code.png'")
