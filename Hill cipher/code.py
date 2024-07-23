import numpy
#key to matrix form
def create_matrix_from(key):
    m=[[0]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j]=ord(key[3*i+j])%65
    return m
#encryption
def encrypt(P,K):
    c=[0,0,0]
    c[0] = (K[0][0] * P[0] + K[1][0] * P[1] + K[2][0] * P[2]) % 26
    c[1] = (K[0][1] * P[0] + K[1][1] * P[1] + K[2][1] * P[2]) % 26
    c[2] = (K[0][2] * P[0] + K[1][2] * P[1] + K[2][2] * P[2]) % 26
    return c
def hill(message,K):
    cipher_text=[]
    for i in range(0,len(message),3):
        P=[0,0,0]
        for j in range(3):
            P[j]=ord(message[i+j])%65
        C=encrypt(P,K)
        for j in range(3):
            cipher_text.append(chr(C[j]+65))
    return "".join(cipher_text)
def MatrixInverse(K):
    det = int(numpy.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = numpy.delete(Dji, (j), axis=0)
            Dji = numpy.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) *
            det) % 26
    return K_inv

message = "MYSECRETMESSAGE"
key="RRFVSVCCT"
K = create_matrix_from(key)
cipher_text = hill(message, K)
print ('Cipher text: ', cipher_text)
K_inv = MatrixInverse(K)
plaintext=hill(cipher_text,K_inv)
print('Plain text: ',plaintext)
