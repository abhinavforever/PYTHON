import pandas as pd
import numpy as np

a=np.array([1,2,3,77,56,32])
a=a.reshape((2,3))
print(a)
df=pd.DataFrame(a)
print(df)