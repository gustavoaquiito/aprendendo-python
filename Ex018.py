import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o tangente de {tangente:.2f}')
