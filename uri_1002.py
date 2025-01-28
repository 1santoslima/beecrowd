from _decimal import Decimal

raio = Decimal(input())
pi = 3.14159
area = Decimal(pi) * (raio ** 2)
print(f'A={area.__round__(4)}')