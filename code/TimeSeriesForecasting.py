#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 下午8:36
# @Author  : Cyy
# @File    : TimeSeriesForecasting.py
# @Software: PyCharm

# https://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/

# load and plot dataset
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt
# load dataset
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')
series = read_csv('../data/shampoo.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# summarize first few rows
print(series.head())
# line plot
series.plot()
pyplot.show()

# split data into train and test
X = series.values
train, test = X[0:-12], X[-12:]
# walk-forward validation
history = [x for x in train]
predictions = list()
for i in range(len(test)):
	# make prediction
	predictions.append(history[-1])
	# observation
	history.append(test[i])
# report performance
rmse = sqrt(mean_squared_error(test, predictions))
print('RMSE: %.3f' % rmse)
# line plot of observed vs predicted
pyplot.plot(test)
pyplot.plot(predictions)
pyplot.show()