#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
from sklearn import linear_model
x = [[4], [5], [6], [7], [8], [9]]
y = [12, 15, 18, 21, 24, 27]
classifier = linear_model.LinearRegression()
classifier.fit(x, y)
X_marks = [[13]]
print(classifier.predict(X_marks))
