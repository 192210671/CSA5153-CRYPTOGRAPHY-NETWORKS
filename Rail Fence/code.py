def encryptRailFence(text,key):
    rail=[['\n' for i in range(len(text))] for j in  range(key)]
    dir_down=False
    row,col=0,0
    for i in range(len(text)):
        if (row==0) or (row==key-1):
            dir_down=not dir_down
        rail[row][col]=text[i]
        col+=1
        if dir_down:
            row+=1
        else:
            row-=1

    result=[]
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j]!='\n':
                result.append(rail[i][j])
    return "".join(result)

def decryptRailFence(cipher_text,key):
    rail=[['\n' for i in range(len(cipher_text))] for j in range(key)]
    dir_down=None
    row,col=0,0
    for i in range(len(cipher_text)):
        if(row==0):
            dir_down=True
        if(row==key-1):
            dir_down=False
        rail[row][col]="*"
        col+=1
        if dir_down:
            row+=1
        else:
            row-=1
    index=0;
    for i in range(key):
        for j in range(len(cipher_text)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher_text))):
                rail[i][j]=cipher_text[index]
                index+=1
    result=[]
    row,col=0,0
    for i in range(len(cipher_text)):
        if row==0:
            dir_down=True
        if row==key-1:
            dir_down=False
        if (rail[row][col]!="*"):
            result.append(rail[row][col])
            col+=1
        if dir_down:
            row+=1
        else:
            row-=1
    return "".join(result)


print("========================RAIL FENCE======================")

text="attack at once"
key=2
cipher_text=encryptRailFence(text,key)
print("Cipher Text:",cipher_text)

plain_text=decryptRailFence(cipher_text,key)
print("Plain Text:",plain_text)
