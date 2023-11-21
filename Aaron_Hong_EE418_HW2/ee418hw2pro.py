alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
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

#QUESTION 1A
def affine(ciphertext, key_pair):
    lowercase = ciphertext.lower()
    plaintext = ""
    mod_inverse = modulo_inverse_naive(key_pair[0], 26)
    for char in lowercase:
        if alphabet.__contains__(char):
            result = (int)((alphabet.index(char)-key_pair[1])*mod_inverse)%26
            #print(result)
            plaintext += alphabet[result]
        else:
            plaintext += char
    return plaintext

#QUESTION 1Bi
def p1bi():
    ciphertext = open("enc_ACAD.txt", "r")
    plaintext = open("Aaron_Hong_affine_output.txt", "w")
    plaintext.write(affine(ciphertext.read(), [9,-17]))
    plaintext.close()
    ciphertext.close()
#p1bi()
#QUESTION 1Bii
def p1bii():
    ciphertext = open("enc_ACAD.txt", "r")
    ciphertext_slice = ciphertext.read()[30:40]
    print(ciphertext_slice)
    print(affine(ciphertext_slice, [9,-17]))
    ciphertext.close()
#p1bii()

#QUESTION 6

#QUESTION 7
relationship_table = {
    'A':'b',
    'F':'a',
    'L':'y',
    'T':'u',
    'O':'f',
    'Q':'i',
    'U':'d',
    'J':'o',
    #added values start here
    'C':'e',
    'G':'l',
    'B':'s',
    'H':'n',
    'V':'g',
    'E':'r',
    'I':'t',
    'D':'v',
    'P':'m',
    'N':'h',
    'K':'p',
    'R':'c',
    'M':'w'
}
def sub_cipher(table, ciphertext):
    result = ""
    for char in ciphertext:
        if char in table:
            result += table[char]
        elif char == ' ' or char == '.':
            result += char
        else:
            result += '_'
    return result
def p7():
    ciphertext = "BCDCEFG BCHFIJEB KECBBCU LCGGCH JH MNCINCE INC OCUB CFBL PJHCL KJGQRQCB MCEC OTCGQHV FBBCI ATAAGCB INFI RJTGU INECFICH INC BLBICP."
    print(sub_cipher(relationship_table, ciphertext))
#p7()
#plaintext: several senators pressed yellen on whether the feds easy money policies were fueling asset bubbles that could threaten the system.
#solving step 1: replace all known plaintext letters and replace all unknowns with blanks
#solving step 2: add most likely ciphertext/plaintext pairs to relationship table until message is solved (like wheel of fortune)

#QUESTION 9
english_frequencies = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]
def letter_frequencies(text):
    total = len(text)
    result = [0] * 26
    lowercase = text.lower()
    for char in lowercase:
        result[alphabet.index(char)] += 1
    for i in range(len(result)):
        result[i] /= total
    return result

def cyclic_correlations(a, b):
    result = 0
    a_freq = letter_frequencies(a)
    b_freq = letter_frequencies(b)
    for i in range(26):
        result += a_freq[i] * b_freq[i]
    return result
        
def split(text, m):
    result = []
    for i in range(m):
        result.append("")
    for i in range(len(text)):
        result[i%m] += text[i]
    return result

test2 = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"
test = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"
a = "KTSVFVMHMCHJUBFDYLMGRWZXNHMVDSVNUBJOJULFZNAQILXSXOJYOROEFJTDXWCNERALABFMLVJFFSEFVXLUJQBORDKMLFBVGYNXLSNJQDWARDXQHAMBRHUPGTYXVVUYXEXHAQJVMLJEZFZBVQPBYPQMPBCUJHBUDSKQFOTVTFGKYXNPDWXJQYVOWLJDUJNJHBUUFUPFOFUTCLWKFJWMKDMOLYNZSQBVBJJHWEEQHLLWTWTORYZXXDYZXOVFPMIHXBMEHSSHZRZKXORYWAPSTZNURNUEFVYPWTRZAQBIWPLBQXLLVUNARFVNNJWHFZCBUYVOBVYVWJVMTNOWFJLVVYVVFGFZRXDXAXIRQTNTVHBAJRZZOBFZSCJHXAQJVXBMEHSPWUUZZRPQNUCPPDTXTWNUCJPFANUKTBPIWXDJTXYANSODPWFAUSRDDGSN"
b = "KSQRAUHSQGGBFDQSXOIXMRWCSYFWAAPPOSELGYQGWZGLDCXVFZZIHLCAXILVRTEWGSJPFLWWCWUXAJOWNEFKGHTMUOVLHIUVBYQGLLRETIEDWETEFVHSQVSUREAEKZIXQEEVBRFLWWCHQVKVTETIWHFETXZLGPBEJHHPMRVLEFMPKAOEUSFACHTMUOHSQPSDGZRRSAICQEFKCQZELBFPEKGKSYFMLSSETIEHRPOIFAFPETWJHEAXZLCAURAVBDAJEHBVURVYSBGMJLGETELAVPKWZVIWPHWJZLDILOSNMYKLGHTMUOWXBIDAVPYXGAVPEIHHFLFMGU"
c = "GGAMGHUMEDWXUFFAOQLYYSALSHUMEDDXPDVUMAKREIKLAZFEMJQHKKBYKQKYSHVRQFATXMMSFBAHZBXHXHQCGOLERXXTOPPYFBMFRPNVFPZULZWTFQBIYQTHLRTVCAVSKFTWKZFLJGKNXNUVFALYLFRSIXVUHOVJWHVLGOLOHSXTPQFVMQGHVNRQRKTQLXEVGPRCLZBKXWGZEFWFHLVPREVJRQRNWJPHAVDZBSESFFGPVZMTQPVERTHFBHEACKNSFEBXSUEOLWAAZWEEJFPHSSHWMIJJFJYKIYECCILZPEBSGAWARZATXXXJFVBMZUWJGWCKALSMMYERMPGOHFWTRDVQNYNQMBIPMKRZZQLNRIJBPYFBMTKGCMUPJMELSGKQUTZFAJQHGIILZNNYMCUQRHKQQUPDKQJLHWGJWHGPVUATXNVXOMYLTQGYEIKLALCQGYLDWDUAOQZTEAJXFILQGYLTUXZLATXRIIJLQZHZWYIRJKVXBQLTJRTVCAHZTQCHKPUHCQVMECIBQKYMLYMRCIYFATKTYVJQULOULYSGALSJYKIYSVTXCOFMWFTIKKTAVUGHVTCPVUNOKDTIQDEHWTBHGDOMYLEUMDVPPDVUNRKTQIJBCLUMGITPRBETLFATHHQCGOLBTXXIJOBBNTFFGWKKRZSUDJXWGYEPAULMFDOYRZHZWHSAQPFBZOHRTJVBEZHFUQIIEEYLFBTWOXPTBYSPPFVXKQBAOQFFXWGJNAPOTQPNCAIHUOXIGDOMHALDBEISUZULTQLTJIJBCYLEXSXBGQUVKEYTVQTBNRPZZRSSGOAJYKIYSHAPGLTEHKXTPFACVXOJWDNSVUNOTWIUWIYFJAGXXGWZGLKBKTFAGJFPUBNWIBCQULTMMNGHVERILEMPRDYKOLPZZNRIGDRYMMVYSGKWNAPAG"

a_freq = letter_frequencies(a)
#print(cyclic_correlations(english_frequencies, a_freq))
#print(split(a, 3))
#print(cyclic_correlations(english_frequencies, t))
def find_key_length(ciphertext):
    for m in range(1,10):
        ac_values = []
        chunks = split(ciphertext, m)
        for chunk in chunks:
            ac_values.append(cyclic_correlations(chunk, chunk))
        print(m,":",ac_values)
find_key_length(a)
#key length of a: probably 5
find_key_length(b)
find_key_length(c)
find_key_length(test)
#print(split(test,5))
'CVABWEBQBUAWWQRWWXANTBDPXXRDWBFAXCVLWYXJBLZEIWMLPRJVELMRQEEEKWMHTRCPIMI', 
'HOEITESEWOOEGMFTIFUDSTNSNVTNDPASNHPHTGTHFLBKKRGXHBTLMXGWHVBEAAXHKZLWWGF', 
'RARANOBQRASAJNVRAPTCXUGRJRUQTHLVGRRDWBFAXCWMNJJFAIACNRNCATBWKDMCDCQQXWK', 
'EHAXXPQEVKXHMKGZKSEMMIMEEVLWYXJBLVTNDPASNHESBGSEGEMRDRSHEAIEORTHNHOANOE', 
'EMTXBHMRXXXBMGXXLKMGXAGLLPHTGTHFLRUQTHLVGRLJHNGYNQRRGINRYQPVEEBRVRHIRIE'

#print(cyclic_correlations(letter_frequencies('CVABWEBQBUAWWQRWWXANTBDPXXRDWBFAXCWMNJJFAIACNRNCATBWKDMCDCQQXWK'), english_frequencies))
p1 = 'CVABWEBQBUAWWQRWWXANTBDPXXRDWBFAXCWMNJJFAIACNRNCATBWKDMCDCQQXWK'
p2 = 'HOEITESEWOOEGMFTIFUDSTNSNVTNDPASNHESBGSEGEMRDRSHEAIEORTHNHOANOE'
p3 = 'RARANOBQRASAJNVRAPTCXUGRJRUQTHLVGRLJHNGYNQRRGINRYQPVEEBRVRHIRIE'
p4 = 'EHAXXPQEVKXHMKGZKSEMMIMEEVLWYXJBLZEIWMLPRJVELMRQEEEKWMHTRCPIMI '
p5 = 'EMTXBHMRXXXBMGXXLKMGXAGLLPHTGTHFLBKKRGXHBTLMXGWHVBEAAXHKZLWWGF '
p = ""
for i in range(len(p1)):
    p += p1[i] + p2[i] + p3[i] + p4[i] + p5[i]

halves = split(test, 2)
#for half in halves:
    #print(letter_frequencies(half))
#print(p)
#print(cyclic_correlations(letter_frequencies('HOEITESEWOOEGMFTIFUDSTNSNVTNDPASNHESBGSEGEMRDRSHEAIEORTHNHOANOE'), english_frequencies))
#print(cyclic_correlations(letter_frequencies('HOEITESEWOOEGMFTIFUDSTNSNVTNDPASNHPHTGTHFLBKKRGXHBTLMXGWHVBEAAXHKZLWWGF'), english_frequencies))





