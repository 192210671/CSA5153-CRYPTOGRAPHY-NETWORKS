def hackingkey(ciphertext,shift):
    plaintext=""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext+=chr((ord(char)-shift-65)%26+65)
            elif char.islower():
                plaintext+=chr((ord(char)-shift-97)%26+97)
        else:
            plaintext+=char
    return plaintext

def brute_force(ciphertext):
    for shift in range(0,26):
        decryptData=hackingkey(ciphertext,shift)
        print(f"Hacking key {shift} : {decryptData}")

ciphertext=" IFMMP FWFSZPOF"
print("Cipher text:",ciphertext)
print("Brute force----------")
brute_force(ciphertext)
