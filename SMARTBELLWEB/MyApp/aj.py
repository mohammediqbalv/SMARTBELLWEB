import qrcode

# House Owner's WhatsApp number (with country code)
whatsapp_number = "7902873459"  # Replace with actual number

# WhatsApp call link
whatsapp_url = f"https://wa.me/{whatsapp_number}?call"

# Generate QR Code
qr = qrcode.make(whatsapp_url)

# Save the QR code
qr.save("whatsapp_call_qr.png")

print("QR Code generated successfully: whatsapp_call_qr.png")
