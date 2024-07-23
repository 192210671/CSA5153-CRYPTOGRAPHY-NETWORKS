def generateKey(string,key):
    key=list(key)
    if len(string)==len(key):
        return key
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return ("".join(key))

def cipher_text(string,key):
    ciphertext=[]
    for i in range(len(string)):
        x=(ord(string[i])+ord(key[i]))%26
        x+=ord('A')
        ciphertext.append(chr(x))
    return ("".join(ciphertext))
def originalText(ciphertext, key):
    orig_text = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i])-ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
string = "GEEKSFORGEEKS"
keyword = "AYUSH"
key = generateKey(string, keyword)
ciphertext = cipher_text(string,key)
print("Ciphertext :", ciphertext)
print("plaintext: ",originalText(ciphertext,key))
