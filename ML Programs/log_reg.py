import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
x = [[30], [40], [50], [60], [20], [10], [70]]
y = [0, 1, 1, 1, 0, 0, 1]
classifier = LogisticRegression()
classifier.fit(x,y)
X_marks = [[50]]
print(classifier.predict(X_marks))
