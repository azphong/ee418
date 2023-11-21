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
        
def square_and_multiply(c, a, n):
    e = 1
    for i in range(2, len(bin(a)), 1):
        e = e**2%n
        if bin(a)[i] == "1":
            e = (e*c)%n
    return e

def to_text_block(x):
    m = ""
    m += (alphabet[(int)(x/(26**2))])
    x = x%(26**2)
    m += (alphabet[(int)(x/26)])
    x = x%26
    m += (alphabet[x])
    return m

def decode(cipher, a, p):
    plaintext = ""
    for c in cipher:
        m = (c[1]*modulo_inverse_naive(square_and_multiply(c[0],a,p),p))%p
        plaintext += to_text_block(m)
    return plaintext

cipher = [(3781, 14409), (31552, 3930), (27214, 15442), (5809, 30274), (5400, 31486), (19936, 721), (27765, 29284), (29820, 7710), (31590, 26470), (3781, 14409), (15898, 30844), (19048, 12914), (16160, 3129), (301, 17252), (24689, 7776), (28856, 15720), (30555, 24611), (20501, 2922), (13659, 5015), (5740, 31233), (1616, 14170), (4294, 2307), (2320, 29174), (3036, 20132), (14130, 22010), (25910, 19663), (19557, 10145), (18899, 27609), (26004, 25056), (5400, 31486), (9526, 3019), (12962, 15189), (29538, 5408), (3149, 7400), (9396, 3058), (27149, 20535), (1777, 8737), (26117, 14251), (7129, 18195), (25302, 10248), (23258, 3468), (26052, 20545), (21958, 5713), (346, 31194), (8836, 25898), (8794, 17358), (1777, 8737), (25038, 12483), (10422, 5552), (1777, 8737), (3780, 16360), (11685, 133), (25115, 10840), (14130, 22010), (16081, 16414), (28580, 20845), (23418, 22058), (24139, 9580), (173, 17075), (2016, 18131), (19886, 22344), (21600, 25505), (27119, 19921), (23312, 16906), (21563, 7891), (28250, 21321), (28327, 19237), (15313, 28649), (24271, 8480), (26592, 25457), (9660, 7939), (10267, 20623), (30499, 14423), (5839, 24179), (12846, 6598), (9284, 27858), (24875, 17641), (1777, 8737), (18825, 19671), (31306, 11929), (3576, 4630), (26664, 27572), (27011, 29164), (22763, 8992), (3149, 7400), (8951, 29435), (2059, 3977), (16258, 30341), (21541, 19004), (5865, 29526), (10536, 6941), (1777, 8737), (17561, 11884), (2209, 6107), (10422, 5552), (19371, 21005), (26521, 5803), (14884, 14280), (4328, 8635), (28250, 21321), (28327, 19237), (15313, 28649)]

print(decode(cipher, 7899,31847))
#plaintext: shestandsupinthegardenwhereshehasbeenworkingandlooksintothedistanceshehassensedachangeintheweatherthereisanothergustofwindabuckleofnoiseintheairandthetallcypressesswaysheturnsandmovesuphilltowardsthehouseclimbingoveralowwallfeelingthefirstdropsofrainonherbarearmsshecrossestheloggiaandquicklyentersthehouse

