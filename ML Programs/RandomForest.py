#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
from sklearn.ensemble import RandomForestRegressor

X = [[30], [40], [50], [60], [20], [10], [70]]
y = [0, 1, 1, 1, 0, 0, 1]
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(X, y)
X_marks = [[50]]
print(RandomForestRegModel.predict(X_marks))
