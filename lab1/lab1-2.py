import numpy as np

# 1) Create Two numpy array of size 3 X 2 and 2 X 3
# 2) Randomly Initalize that array

m1 = np.array([[1,2], [3,4], [5,6]])

m2 = np.random.randint(100, size=(2, 3))
#print(m1, m2)

# 3) Perform matrix multiplication

mult = np.matmul(m1, m2)
dotmult = np.dot(m1, m2)
# print(mult)
# print(dotmult)

# 4) 4) Perform elementwise matrix multiplication
m3 = np.array([[10,20], [30,40], [50,60]])
elemmult = m1 * m3
# print(elemmult)

# 5) Find mean of first matrix
mean = np.mean(m1)
# print(mean)

# Convert Numeric entries(columns) of mtcars.csv to Mean Centered Version