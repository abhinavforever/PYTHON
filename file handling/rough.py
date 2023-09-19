# class student:
#     def __f__():
#         print("im static")
#     def func(self):
#         print("a")
# class abhinav(student):
#     def func1(self):
#         print("b")

# a=abhinav()
# a.func()
# a.func1()
# student.__f__()

import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

plt.imshow(arr, cmap='viridis')
plt.colorbar()
plt.show()

