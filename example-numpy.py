import numpy

A = numpy.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
b = numpy.array([4, 5, 6])

invA = numpy.linalg.inv(A)
x = invA.dot(b)

print(x)
