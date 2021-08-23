import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("./cars.csv")
# print(data.head())

data = data[["symboling", "engine-size", "horsepower",
            "peak-rpm", "city-mpg", "highway-mpg", "price"]]
print(data.head())

predict = "symboling"
