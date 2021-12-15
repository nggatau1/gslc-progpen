import base64
import urllib.request
from stegano import lsb

imgurLink = input("Insert IMGUR Image Link: ")

urllib.request.urlretrieve(imgurLink, "chaeyoung2.png")

image_decode = lsb.reveal("chaeyoung2.png")

print("\nENCRYPTED MESSAGE FOUNDED!!")
print("This is the encrypted message: " + image_decode)

msg_encrypted = image_decode.encode("utf-8")
msg_decode = base64.b64decode(msg_encrypted)
print(f"\nDecode Message: " + msg_decode.decode("utf-8"))