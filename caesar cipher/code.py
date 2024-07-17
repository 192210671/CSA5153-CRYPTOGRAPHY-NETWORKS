#caesar cipher
def encryption(plaintext,k):
    encryptData=""
    for i in range(len(plaintext)):
        char=plaintext[i]

        if(char.isupper()):
            encryptData+=chr((ord(char)+k-65)%26+65)
        elif(char.islower()):
            encryptData+=chr((ord(char)+k-97)%26+97)
        else:
            encryptData+=char

    return encryptData

def decryption(CT,k):
    decryptData = ""
    for i in range(len(CT)):
        char = CT[i]

        if (char.isupper()):
            decryptData += chr((ord(char) - k - 65) % 26 + 65)
        elif (char.islower()):
            decryptData += chr((ord(char) - k - 97) % 26 + 97)
        else:
            decryptData += char

    return decryptData

plaintext="HELLO EVERYONE"
k=1
CT=encryption(plaintext,k)
print("ENCRYPTION:",CT)
PT=decryption(CT,k)
print("DECRYPTION:",PT)

