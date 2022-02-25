import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd


df = pd.read_csv("data.csv")
AvgRating1 = df["Avg Rating"]
AvgRating = AvgRating1.tolist()
fig = ff.create_distplot([AvgRating],["Avg Rating"])
fig.show()
fig.show()
