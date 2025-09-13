import math
n1 = int(input('Dig. o ângulo que você deseja: '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O ângulo é {} e o SENO é {:.2f}'. format(n1, sen))
print('O ângulo é {} e o COSSENO é {:.2f}'. format(n1, cos))
print('O ângulo é {} e o TANGENTE é {:.2f}'. format(n1, tan))
