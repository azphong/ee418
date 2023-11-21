import math

#region PartA
#With this information, (880525*2057502*648581)^2 = 6^2 mod 2288233. This gives us x and y that we can use to factor 2288233.
#endregion

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#region PartB
x = (880525 * 2057202 * 648581)
y = 6
n = 2288233
print(gcd(x-y,n))
print(n/gcd(x-y,n))
#factors: 1223 * 1871 = 2288233
#endregion
