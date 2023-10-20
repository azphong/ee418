import math, time

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

#QUESTION 3A
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd_of_three(a, b, c):
    return gcd(gcd(a, b), c)

#QUESTION 3B
#print(gcd_of_three(-144, 2058, 302526))   # output: 6
#print(gcd_of_three(3674160, -243, 51030)) # output: 243
#print(gcd_of_three(-733, -21379, 46782))  # output: 1

n=2161
m=12235
start_time = time.time()
modulo_inverse_naive(n,m,1)
end_time = time.time()
print("Run time in seconds (s):", (end_time-start_time))

#QUESTION 3D
#0.0s, 0.0s, 0.0s, 0.006s, 0.06s

#QUESTION 5B
def perm_cipher8(key, ciphertext):
    cipher_array = [char for char in ciphertext]
    result = ""
    for i in range(len(cipher_array)):
        result += cipher_array[key[i%8]]
    return result

#QUESTION 5C
print(perm_cipher8([2,4,6,1,8,3,5,7],"TGEEMNELNNTDROEOAAHOETCSHAEIRLM"))

#QUESTION 6A
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def shift_cipher(key, ciphertext):
    lowercase = ciphertext.lower()
    plaintext = ""
    for char in lowercase:
        plaintext += alphabet[(alphabet.index(char)-key)%26]
    return plaintext

#QUESTION 6B
print(shift_cipher(15, "TRDCITCIBP"))
