

def generate_key_square(keyword):
    keyword=keyword.upper().replace('J','I')
    key_square=[]
    used_chars=set()
    for char in keyword:
        if char not in used_chars and char.isalpha():
            key_square.append(char)
            used_chars.add(char)
    alphabets="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char  in alphabets:
        if char not in used_chars:
            key_square.append(char)
            used_chars.add(char)
        #slicing the array
    return [key_square[i*5:(i+1)*5] for i in range(5)]

def find_position(char,key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col]==char:
                return row,col
    return None

def encrypt_digraph(digraph,key_square):
    row1,col1=find_position(digraph[0],key_square)
    row2,col2=find_position(digraph[1],key_square)
    if row1==row2:
        return key_square[row1][(col1+1)%5]+key_square[row2][(col2+1)%5]
    elif col1==col2:
        return key_square[(row1+1)%5][col1]+key_square[(row2+1)%5][col2]
    else:
        return key_square[row1][col2]+key_square[row2][col1]
def prepare_text(text):
    text=text.upper().replace('J','I')
    prepared_text=""
    i=0
    while i<len(text):
        if text[i].isalpha():
            prepared_text+=text[i]
            if i+1<len(text) and text[i]==text[i+1]:
                prepared_text+='X'
            else:
                if i+1<len(text) and text[i+1].isalpha():
                    prepared_text+=text[i+1]
                elif i+1==len(text):
                    prepared_text+='Z'
                i+=1
        i+=1
    if len(prepared_text)%2!=0:
        prepared_text+='Z'
    return prepared_text

def playfair_encrypt(plaintext,keyword):
    key_square=generate_key_square(keyword)
    prepared_text=prepare_text(plaintext)
    ciphertext=""
    for i in range(0,len(prepared_text),2):
        ciphertext+=encrypt_digraph(prepared_text[i:i+2],key_square)
    return ciphertext


keyword="monarchy"
plaintext="instruments"
ciphertext=playfair_encrypt(plaintext,keyword)
print("Key square_____________")
for row in generate_key_square(keyword):
    print(" ".join(row))
print("plaintext:",plaintext)
print("ciphertext:",ciphertext)

