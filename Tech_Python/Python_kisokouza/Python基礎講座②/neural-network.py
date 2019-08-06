x1 = 1.0
x2 = 2.0
w1u1 = 3.0
w1u2 = 1.0
w1u3 = -3.0
w2u1 = 2.5
w2u2 = 2.0
w2u3 = -1.0
w3 = -4.0
w4 = 1.5
w5 = 4.2

u1 = x1*w1u1 + x2*w2u1
u2 = x1*w1u2 + x2*w2u2
u3 = x1*w1u3 + x2*w2u3

y = u1*w3 + u2*w4 + u3*w5

print(y)
