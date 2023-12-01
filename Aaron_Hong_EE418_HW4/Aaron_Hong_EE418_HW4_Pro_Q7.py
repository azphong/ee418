iv = 0b1010000011111010
hill_key = 0b0100100000010010
vigenere_key = 0b1001001111001001

def xor(a, b):
    return bin(a^b)

def matrix_multiply(m_str, k_str):
    m = to_4x4(pad(m_str[2:],16))
    k = to_4x4(pad(k_str[2:],16))
    result = [[0 for x in range(len(m))] for y in range(len(k[0]))]
    for a in range(len(m)):
        for b in range(len(k[0])):
            for c in range(len(k)):
                result[a][b] += m[a][c] * k[c][b]
                result[a][b] %= 2
    return from_4x4(result)

message = 0b100110010011100011000101000111101100111110101010010110110101100001101110010101111000000010001001

def split(m_int,size):
    m = str(bin(m_int))[2:]
    result_str = ["" for i in range(int(len(m)/size))]
    for i in range(len(m)):
        result_str[int(i/size)] += m[i]
    while(len(result_str[len(result_str)-1])<size):
        result_str[len(result_str)-1] += "0"
    result = [0 for i in range(len(result_str))]
    for i in range(len(result_str)):
        result[i] = bin(int(result_str[i],2))
    return result

def to_4x4(m):
    result = [[0 for x in range(4)] for y in range(4)]
    for i in range(2,len(str(m))):
        result[int(i/4)][i%4] = int(m[i],2)
    return result

def from_4x4(m):
    result = ""
    for i in range(len(m)):
        for j in range(len(m[0])):
            result += str(m[i][j])
    return result

def pad(m,size):
    result = str(m)
    while len(result)<size:
        result = "0"+result
    return result

def cbc_mac(m):
    forward = ""
    chunks = split(m,16)
    for i in range(len(chunks)):
        if i == 0:
            forward = matrix_multiply(xor(int(chunks[i],2),int(iv)),bin(hill_key)[2:])
        elif i%2==0:
            forward = matrix_multiply(xor(int(chunks[i],2),int(forward,2)),bin(hill_key)[2:])
        else:
            forward = xor(int(xor(int(chunks[i],2),int(forward,2)),2),int(vigenere_key))
    return forward

print(cbc_mac(message)) #result:0010100111111001
