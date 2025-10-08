import numpy

A = numpy.array([[1,3,2],[3,-2,3],[4,1,-2]])   # Coefficient matrix
x = numpy.array([[8],[4],[2]])                 # x0, x1 and x2 as a 3x1 matrix
y = A@x                                        # y = A.x by matrix multiplication
print(y)
