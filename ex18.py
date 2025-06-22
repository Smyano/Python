import math
from fractions import Fraction
co = int(input("Digite o valor do cateto oposto "))
ca = int(input("Digite o valor do cateto adjacente "))
h = math.sqrt(ca **2 + co **2)
sen = Fraction(co / h).limit_denominator()
cos = Fraction(ca / h).limit_denominator()
tang = Fraction(co / ca).limit_denominator()
print(f" O valor do seno é {sen}, o valor da tangente é {tang} e o valor do cosseno é {cos}")
