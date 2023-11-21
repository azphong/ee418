import math
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def modulo_inverse_naive(n,m, print_flag = 0):
    if n == 1:
        print('Inverse of 1 in mod '+ str(m) +' is 1')
    else:
        if (float(n)).is_integer() and (float(m)).is_integer() and m > 0:
            if math.gcd(n,m) == 1:
                n_mod_m = n%m
                for x in range(1, m): 
                    if ((n_mod_m * x)%m)  == 1:#(np.mod((n_mod_m * x),m)  == 1):
                        if print_flag == 1:
                            print('Inverse of ' + str(n) + ' in mod '+ str(m) +' is ' + str(x))
                        return x 
            else:
                print('ERROR: gcd(n,m) is not 1. Inverse does not exist for n mod m')
        else:
            print('ERROR: n and m both must be integers. m should be positive')

#region PartA
def factor(n):
    for i in range(2, math.floor(math.sqrt(n))):
        if is_prime(i):
            if n % i == 0:
                return [i, int(n/i)]

def is_prime(x):
    for i in range(2, math.floor(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

def totient(n):
    factors = factor(n)
    return((factors[0]-1)*(factors[1]-1))
        
def compute_RSA_private(e, n):
    return modulo_inverse_naive(e, totient(n))

print(compute_RSA_private(4913, 31313)) 
#RSA private key: 6497
#endregion

#region PartB
def square_and_multiply(c, a, n):
    e = 1
    for i in range(2, len(bin(a)), 1):
        e = e**2 % n
        if bin(a)[i] == "1":
            e = (e * c) % n
    return e
#endregion

#region PartC
def to_text_block(x):
    m = ""
    m += (alphabet[(int)(x/(26**2))])
    x = x%(26**2)
    m += (alphabet[(int)(x/26)])
    x = x%26
    m += (alphabet[x])
    return m

def decode(ciphertext, b, n):
    a = compute_RSA_private(b, n)
    m = ""
    for c in ciphertext:
        e = square_and_multiply(c, a, n)
        m += to_text_block(e)
    return m
    
cipher = [6340, 8309, 14010, 8936, 27358, 25023, 16481, 25809, 23614, 7135, 24996, 30590, 27570, 26486, 30388, 9395, 27584, 14999, 4517, 12146, 29421, 26439, 1606, 17881, 25774, 7647, 23901, 7372, 25774, 18436, 12056, 13547, 7908, 8635, 2149, 1908, 22076, 7372, 8686, 1304, 4082, 11803, 5314, 107, 7359, 22470, 7372, 22827, 15698, 30317, 4685, 14696, 30388, 8671, 29956, 15705, 1417, 26905, 25809, 28347, 26277, 7897, 20240, 21519, 12437, 1108, 27106, 18743, 24144, 10685, 25234, 30155, 23005, 8267, 9917, 7994, 9694, 2149, 10042, 27705, 15930, 29748, 8635, 23645, 11738, 24591, 20240, 27212, 27486, 9741, 2149, 29329, 2149, 5501, 14015, 30155, 18154, 22319, 27705, 20321, 23254, 13624, 3249, 5443, 2149, 16975, 16087, 14600, 27705, 19386, 7325, 26277, 19554, 23614, 7553, 4734, 8091, 23973, 14015, 107, 3183, 17347, 25234, 4595, 21498, 6360, 19837, 8463, 6000, 31280, 29413, 2066, 369, 23204, 8425, 7792, 25973, 4477, 30989]

print(decode(cipher, 4913, 31313)) 
#plaintext: lakewobegonismostlypoorsandysoilandeveryspringtheearthheavesupanewcropofrockspilesofrockstenfeethighinthecornersoffieldspickedbygenerationsofusmonumentstoourindustryourancestorschosetheplacetiredfromtheirlongjourneysadforhavingleftthemotherlandbehindandthisplaceremindedthemoftheresotheysettledhereforgettingthattheyhadlefttherebecausethelandwasntsogoodsothenewlifeturnedouttobealotliketheoldexceptthewintersareworsez
#endregion


