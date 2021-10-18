import pandas as pd 
import plotly.figure_factory as ff 
import csv

df=pd.read_csv("data2.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],["Average Ratings"])
fig.show()