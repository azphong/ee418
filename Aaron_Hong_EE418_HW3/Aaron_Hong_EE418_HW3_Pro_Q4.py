alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#region PartA
#An eavesdropper E can easily decrypt a message encoded this way because each letter of the alphabet can be encrypted to only one number. This makes it easy to figure out which letter corresponds to which number and figure out the plaintext from the ciphertexts.
#endregion

#region PartB
def square_and_multiply(c, a, n):
    e = 1
    for i in range(2, len(bin(a)), 1):
        e = e**2 % n
        if bin(a)[i] == "1":
            e = (e * c) % n
    return e

for letter in range(len(alphabet)):
    print(alphabet[letter],':',square_and_multiply(letter, 25, 18721))

#decoded message: "vanilla"
#endregion