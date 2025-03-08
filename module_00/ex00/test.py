from matrix import Matrix

# Test __init__
m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
m2 = Matrix([[10.0, 20.0], [30.0, 40.0]])
m3 = Matrix([[10.0, 20.0, 30.0], [50.0, 60.0, 70.0]])
m0 = Matrix([[0.0, 0.0], [0.0, 0.0]])

print(m1.data)
print(m2.data)

print("Test __add__")
sum = m1 + m2
print(sum.data)

try:
    sum = m1 + m3
except ValueError as e:
    print(f"Error: {e}")

print("Test __radd__")
sum = 100 + m1
print(sum.data)

print("Test __sub__")
sub = m1 - m2
print(sub.data)

sum = m1 - 1000
print(sub.data)

print("Test __rsub__")
sum = 100 - m1
print(sub.data)

print("Test __truediv__")
truediv = m1 / m2
print(truediv.data)

try:
    truediv = m1 / m0
    print(truediv.data)
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    truediv = m1 / 0
    print(truediv.data)
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("Test __rtruediv__")
truediv = 100 / m1
print(truediv.data)

print("Test __mul__")
mul = m1 * m2
print(mul.data)

try:
    mul = m1 * m3
    print(mul.data)
except ValueError as e:
    print(f"Error: {e}")

print("Test __rmul__")
mul = 100 * m1
print(mul.data)

print(str(m1))
print(repr(m1))

print(str(m3))
print(repr(m3))

print(repr(m1))
print(repr(m1.T()))

