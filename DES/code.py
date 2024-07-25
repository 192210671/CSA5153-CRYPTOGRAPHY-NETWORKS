import base64
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

password = "Password"
salt = b'\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'

key = password.encode() + salt
m = hashlib.md5(key)
key = m.digest()

(dk, iv) = (key[:8], key[8:])


crypter = DES.new(dk, DES.MODE_CBC, iv)


plain_text = "I see you"
print("===================DES====================")
print("The plain text is:", plain_text)


padded_plain_text = pad(plain_text.encode(), DES.block_size)


ciphertext = crypter.encrypt(padded_plain_text)


encoded_string = base64.b64encode(ciphertext).decode()
print("The encoded string is:", encoded_string)


decipher = DES.new(dk, DES.MODE_CBC, iv)


decoded_ciphertext = base64.b64decode(encoded_string)

decrypted_padded_plaintext = decipher.decrypt(decoded_ciphertext)


decrypted_plaintext = unpad(decrypted_padded_plaintext, DES.block_size).decode()
print("The decrypted plaintext is:", decrypted_plaintext)
