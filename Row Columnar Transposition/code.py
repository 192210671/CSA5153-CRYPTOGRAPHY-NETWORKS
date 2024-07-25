def encryption(msg,key):
    no_columns=len(key)
    no_rows=len(msg)//no_columns
    if len(msg)%no_columns!=0:
        no_rows+=1
    padding_len=no_rows*no_columns-len(msg)
    msg+='X'*padding_len

    grid=[['x' for _ in range(no_columns)] for _ in range(no_rows)]
    index=0
    for r in range(no_rows):
        for c in range(no_columns):
            if index<len(msg):
                grid[r][c]=msg[index]
                index+=1

    sorted_key=sorted(list(enumerate(key)),key=lambda x:x[1])
    ciphertext=""
    for col_index,_ in sorted_key:
        for row in grid:
            ciphertext+=row[col_index]
    return ciphertext

def decryption(ciphertext,key):
    no_columns=len(key)
    no_rows=len(ciphertext)//no_columns
    sorted_key=sorted(list(enumerate(key)),key=lambda x:x[1])

    grid=[['' for _ in range(no_columns)] for _ in range(no_rows)]


    index=0
    for col_index,_ in sorted_key:
        for row in range(no_rows):
            grid[row][col_index]=ciphertext[index]

            index+=1
    plaintext=""
    for row in grid:
        plaintext+="".join(row)
    plaintext=plaintext.rstrip('X')
    return plaintext

print("===================ROW COLUMNAR TRANSPOSITION===================")
key="HACK"
msg="GREEKSFORGREEK"
ciphertext=encryption(msg,key)
print("Cipher Text:",ciphertext)
plaintext=decryption(ciphertext,key)
print("Plain text:",plaintext)
