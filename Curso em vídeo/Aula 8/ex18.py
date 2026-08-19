
# from fractions import Fraction
# co = int(input("Digite o valor do cateto oposto "))
# ca = int(input("Digite o valor do cateto adjacente "))
# h = math.sqrt(ca **2 + co **2)
# sen = Fraction(co / h).limit_denominator()
# cos = Fraction(ca / h).limit_denominator()
# tang = Fraction(co / ca).limit_denominator()
# print(f" O valor do seno é {sen}, o valor da tangente é {tang} e o valor do cosseno é {cos}")

import math
angulo = float(input("digite um angulo "))
print (f"o angulo de seno é {math.sin(math.radians(angulo)):.2f} \n o cosseno é {math.cos(math.radians(angulo)):.2f} \n a tangente é {math.tan(math.radians(angulo)):.2f}")


from math import sin, cos, tan, radians
angulo = float(input("digite um angulo "))
print (f"o angulo de seno é {sin(radians(angulo)):.2f} \n o cosseno é {cos(radians(angulo)):.2f} \n a tangente é {tan(radians(angulo)):.2f}")
