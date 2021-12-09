import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading score"].to_list()


mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
sd = statistics.stdev(data)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(mean,median,mode))
                       
first_std_deviation_start, first_std_deviation_end = mean-sd, mean+sd
second_std_deviation_start, second_std_deviation_end = mean-(2*sd), mean+(2*sd)
third_std_deviation_start, third_std_deviation_end = mean-(3*sd), mean+(3*sd)



fig = ff.create_distplot([data],["reading scores"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))

data_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
data_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
data_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("Mean of the data is:- {}".format(mean))
print("Median of the data is:- {}".format(median))
print("Mode of the data is:- {}".format(mode))
print("{}% of data for height lies within 1 standard deviation".format(len(data_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data for height lies within 2 standard deviation".format(len(data_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data for height lies within 3 standard deviation".format(len(data_of_data_within_3_std_deviation)*100.0/len(data)))
