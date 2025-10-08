import numpy

A = numpy.array([[1,3,2],[3,-2,3],[4,1,-2]])  # Coefficient matrix
y = numpy.array([[11],[8],[12]])              # x0, x1 and x2 as a 3x1 matrix

x_method1 = numpy.linalg.inv(A)@y             # Multiply y by the inverse of A
x_method2 = numpy.linalg.solve(A, y)          # Direct calculation of x given A and y

print(x_method1)                              # Both methods should give the same solution
print(x_method2)                              # x0 = 3, x1 = 2, x2 = 1
