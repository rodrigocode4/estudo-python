from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_mult

from pacote1.modulo1 import soma
from pacote2.modulo1 import mult

print(modulo1.soma(2,2))
print(modulo1_mult.mult(2,3))
print(soma(3,3))
print(mult(3,3))