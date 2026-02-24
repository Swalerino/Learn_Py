import numpy as np

Array3D = np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                   [[1,1,1],
                   [1,2,3],
                   [3,3,3]]])

print(Array3D)
print("")

Array3D = np.roll(Array3D, shift=1, axis=0)

print(Array3D)
#print("")

#Array3D = np.roll(Array3D, shift=-1, axis=2)

#print(Array3D)