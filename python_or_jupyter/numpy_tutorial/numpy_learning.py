import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])

print(f"Printing a:\n{a}\n")
print(f"Printing a type:\n{type(a)}\n")
print(f"Printing a in position:\n{a[1]}\n")

b = np.array([i for i in range(1,10)] )

print(b)
print(type(b))

c = [i for i in range(1,10)]

print(c)
print(type(c))

d = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]]
             )

print(d[0][1])
print(d[0,1])
print("d shape is {d.shape}")
print("d dimension is {d.ndim}")

e = np.array([[[1,2,3],
             [4,5,6],
             [7,8,9]],
             [[1,2,3],
             [4,5,6],
             [7,8,9]]
             ])

print(e[0][0][1])
print(e[0,0,1])
print(e.shape)
print(e.ndim)
print(e.size)
print(e.dtype)

f = np.array([[[1,2,3],
             [4,5,6],
             [7,8,9]],
             [[1,2,3],
             [4,"Hello",6],
             [7,8,9]]
             ])

print(f[1][1][1].dtype)

g = np.full((2,3,4), 9)
print(g)

h = np.zeros((2,3,4))
print(h)

i = np.ones((2,3,4))
print(f"Printing i variable:\n{i}\n")

j = np.empty((2,3,4))
print(f"Printing j variable:\n{j}\n")

x_values = np.arange(0, 100, 5)
print(x_values)

x_values_2 = np.linspace(0, 100, 101)
print(x_values_2)

print(np.nan)
print(np.inf)
print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10])/0))

l1 = [i for i in range(1,6)]
l2 = [j for j in range(6,11)]

a1 = np.array(l1)
a2 = np.array(l2)
a3 = 3
print(f"Print l1 times 2 value:\n{l1*2}\n")
print(f"Print a1 times 2 value:\n{a1*2}\n")

# print(l1 - l2)
# print(a3*l1 - l2)
# print(a3*l1 + l2)
print(f"Print a3*a1 value:\n{a3*a1}\n")
print(f"Print sqrt(a1) value:\n{np.sqrt(a1)}\n")
print(f"Print a3*a1 - a2 value:\n{a3*a1 - a2}\n")
print(f"Print a3*a1 + a2 value:\n{a3*a1 + a2}\n")
print(f"Print a1*a2 value:\n{a1*a2}")


a_array = []
b = [i for i in range(1,51)]
for i in range(0, len(b), 10):
    a_array.append(b[i:i+10])
print(f"Print a_array variable:\n{a_array}\n")
print(f"Print a_array array:\n{np.array(a_array)}\n")

print(f"Print a_array array shape:\n{np.array(a_array).shape}\n")
print(f"Print a_array array reshape to (10,5):\n{np.array(a_array).reshape(10,5)}")
print(f"Print a_array array reshape to (2,25):\n{np.array(a_array).reshape(2,25)}")