import pyimgur
import base64
import requests
import json
from stegano import lsb

msg = input("Message to encode with UTF-8: ")
msg_utf8 = msg.encode("utf-8")
msg_b64encoded = base64.b64encode(msg_utf8)

print(f"Encoded string to Base64: " + msg_b64encoded.decode("utf-8"))

msg_b64decoded = msg_b64encoded.decode("utf-8")

image = lsb.hide("chaeyoung.png", msg_b64decoded)
image.save("chaeyoung1.png")
image_decode = lsb.reveal("chaeyoung1.png")
print(image_decode) 
print("\nMessage succesfully injected")

CLIENT_ID = "APIKEY"
PATH = "chaeyoung1.png"

imageUpload = pyimgur.Imgur(CLIENT_ID)
uploaded_image = imageUpload.upload_image(PATH, title="Stegano")

print(uploaded_image.link)