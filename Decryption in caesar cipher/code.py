def decryption(ciphertext,key):
    plaintext=""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext+=chr((ord(char)-key+65)%26+65)
            elif char.islower():
                plaintext+=chr((ord(char)-key+97)%26+97)
        else:
            plaintext+=char
    return plaintext
ciphertext="KYZJ ZJ R MVIP TFFC DVJJRXV"
key=17
print("Cipher text :",ciphertext)
print("Decryption:",decryption(ciphertext,key))
