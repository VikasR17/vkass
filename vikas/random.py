import random as random
import numpy as n
import pandas as pd
ser = pd.Series(n.random.random(size=10))
print(ser.nlargest(n=1))