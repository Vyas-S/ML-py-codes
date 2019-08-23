"""this program contains the code for data preprocessing a missing data in a csv file"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Data.csv')    #csv file name "Data"
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values
