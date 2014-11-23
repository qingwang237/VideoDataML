import pandas as pd
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


d1 = pd.read_csv("bilibili_week1.csv")
for i in range(2, 12):
    csvname = "bilibili_week" + str(i) + '.csv'
    d2 = pd.read_csv(csvname)
    newframe = pd.concat([d1, d2])
    d1 = newframe
newframe.drop_duplicates()
newframe.reset_index(inplace=True)
newframe = newframe[newframe.ViewCount != 0]
newframe.to_csv("original_data.csv")

df_input = newframe[["ViewCount", "Favorites", "Danmu"]]
df_input.to_csv("data.csv")
