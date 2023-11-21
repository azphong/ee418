import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#region PartA
x = 85975324443166
y = 462436106261
n = 537069139875071

print(gcd(x-y,n))
print(n/(gcd(x-y,n)))
#factors: 9876469 * 54378659 = 537069139875071
#endregion
