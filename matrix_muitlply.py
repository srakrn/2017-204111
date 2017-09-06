'''
=== Matrix Multiplication === 
This initialises the use of NumPy, a library which
will be taught on the next half session of the semester,
alongside with data tools like scikit, matplotlib.
'''

import numpy

rows_a = int(input("Rows of matrix a: "))
print("Input matrix a:")
a = []
for i in range(rows_a):
    a.append([float(x) for x in input().split()])
rows_b = int(input("Rows of matrix b: "))
print("Input matrix b:")
b = []
for i in range(rows_b):
    b.append([float(x) for x in input().split()])

try:
    a_times_b = numpy.dot(a,b)

    print()
    for i in a_times_b:
        for j in i:
            print("{:<10.2f}".format(j) if int(j)==j else "{:<10.0f}".format(j),end='')
        print()
except ValueError:
    print("The matrices dimension resulted error in multiplication.")
