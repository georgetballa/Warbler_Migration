from functions import*
import os.path
from os import path
import pickle
import pandas as pd
from ebird.api import *
import matplotlib.pyplot as plt
from datetime import *
import datetime as dt
import re
import requests
import numpy as np
from dateutil.relativedelta import relativedelta
import gc
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import statsmodels.api as sm
from glm.glm import GLM
from glm.families import Gaussian
import scipy
import scipy.stats as stats
from matplotlib.dates import (YEARLY, DateFormatter,rrulewrapper, RRuleLocator, drange)

### Data Transforms for Graphing

obs2020 = cleaner(2020,'warb', 'comName')
obs2019 = cleaner(2019,'warb', 'comName')
obs2018 = cleaner(2018,'warb', 'comName')
obs2017 = cleaner(2017,'warb', 'comName')
obs2016 = cleaner(2016,'warb', 'comName')
obs2015 = cleaner(2015,'warb', 'comName')
obs2014 = cleaner(2014,'warb', 'comName')
obs2013 = cleaner(2013,'warb', 'comName')

counts2013 = count_observations(obs2013, date(2013,1,1))
counts2014 = count_observations(obs2014, date(2014,1,1))
counts2015 = count_observations(obs2015, date(2015,1,1))
counts2016 = count_observations(obs2016, date(2016,1,1))
counts2017 = count_observations(obs2017, date(2017,1,1))
counts2018 = count_observations(obs2018, date(2018,1,1))
counts2019 = count_observations(obs2019, date(2019,1,1))
counts2020 = count_observations(obs2020, date(2020,1,1))

total2020 = total_cleaner(2020)
total2019 = total_cleaner(2019)
total2018 = total_cleaner(2018)
total2017 = total_cleaner(2017)
total2016 = total_cleaner(2016)
total2015 = total_cleaner(2015)
total2014 = total_cleaner(2014)
total2013 = total_cleaner(2013)


totalcounts2013 = count_observations(total2013, date(2013,1,1))
totalcounts2014 = count_observations(total2014, date(2014,1,1))
totalcounts2015 = count_observations(total2015, date(2015,1,1))
totalcounts2016 = count_observations(total2016, date(2016,1,1))
totalcounts2017 = count_observations(total2017, date(2017,1,1))
totalcounts2018 = count_observations(total2018, date(2018,1,1))
totalcounts2019 = count_observations(total2019, date(2019,1,1))
totalcounts2020 = count_observations(total2020, date(2020,1,1))

mean_loc_obs2020 = mean_lats(obs2020)
mean_loc_obs2019 = mean_lats(obs2019)
mean_loc_obs2018 = mean_lats(obs2018)
mean_loc_obs2017 = mean_lats(obs2017)
mean_loc_obs2016 = mean_lats(obs2016)
mean_loc_obs2015 = mean_lats(obs2015)
mean_loc_obs2014 = mean_lats(obs2014)
mean_loc_obs2013 = mean_lats(obs2013)

spring2020 = date_searcher(obs2020, '2020-04-07', '2020-05-22')
spring2019 = date_searcher(obs2019, '2019-04-07', '2019-05-22')
spring2018 = date_searcher(obs2018, '2018-04-07', '2018-05-22')
spring2017 = date_searcher(obs2017, '2017-04-07', '2017-05-22')
spring2016 = date_searcher(obs2016, '2016-04-07', '2016-05-22')
spring2015 = date_searcher(obs2015, '2015-04-07', '2015-05-22')
spring2014 = date_searcher(obs2014, '2014-04-07', '2014-05-22')
spring2013 = date_searcher(obs2013, '2013-04-07', '2013-05-22')

mean_loc_spring2020 = mean_lats(spring2020)
mean_loc_spring2019 = mean_lats(spring2019)
mean_loc_spring2018 = mean_lats(spring2018)
mean_loc_spring2017 = mean_lats(spring2017)
mean_loc_spring2016 = mean_lats(spring2016)
mean_loc_spring2015 = mean_lats(spring2015)
mean_loc_spring2014 = mean_lats(spring2014)
mean_loc_spring2013 = mean_lats(spring2013)

obsall = obs2020.append(obs2019)
obsall = obsall.append(obs2018)
obsall = obsall.append(obs2017)
obsall = obsall.append(obs2016)
obsall = obsall.append(obs2015)
obsall = obsall.append(obs2014)
obsall = obsall.append(obs2013)

mean_loc_spring_total = mean_loc_spring2020.append(mean_loc_spring2019)
mean_loc_spring_total = mean_loc_spring_total.append(mean_loc_spring2018)
mean_loc_spring_total = mean_loc_spring_total.append(mean_loc_spring2017)
mean_loc_spring_total = mean_loc_spring_total.reset_index()

mean_loc_spring_total = mean_loc_spring_total.drop(columns=['index', 'dtnum'])
mean_loc_spring_total['obsDt'] = mean_loc_spring_total['obsDt'].map('{}-00'.format)
mean_loc_spring_total['obsDt'] = pd.to_datetime(mean_loc_spring_total['obsDt'])
mean_loc_spring_total['obsDt'] = mean_loc_spring_total['obsDt'].map(dt.datetime.toordinal)


####Graphing

#### PLOT MEAN LAT OF EVERY DAY 2013-2020
fig, ax = plt.subplots() 
fig.set_size_inches(30, 20)

x = mean_loc_obs2020['obsDt']
y = mean_loc_obs2020['lat']
ax.scatter(x,y, label = '2020', s=100, alpha=.6)

x19 = mean_loc_obs2019['obsDt']
y19 = mean_loc_obs2019['lat']
ax.scatter(x19,y19, label = '2019', s=100, alpha=.6)

x18 = mean_loc_obs2018['obsDt']
y18 = mean_loc_obs2018['lat']
ax.scatter(x18,y18, label = '2018', s=100, alpha=.6)

x17 = mean_loc_obs2017['obsDt']
y17 = mean_loc_obs2017['lat']
ax.scatter(x17,y17, label = '2017', s=100, alpha=.6)

x16 = mean_loc_obs2016['obsDt']
y16 = mean_loc_obs2016['lat']
ax.scatter(x16,y16, label = '2016', s=100, alpha=.6)

x15 = mean_loc_obs2015['obsDt']
y15 = mean_loc_obs2015['lat']
ax.scatter(x15,y15, label = '2015', s=100, alpha=.6)

x14 = mean_loc_obs2014['obsDt']
y14 = mean_loc_obs2014['lat']
ax.scatter(x14,y14, label = '2014', s=100, alpha=.6)

x13 = mean_loc_obs2013['obsDt']
y13 = mean_loc_obs2013['lat']
ax.scatter(x13,y13, label = '2013', s=100, alpha=.6)

plt.xlabel('Day', fontsize=20)
plt.ylabel('Latitude', fontsize=20)
plt.xlim(0,365)
plt.title(f'Warbler Latitudes 2013-2020', fontsize=60, color='saddlebrown')
plt.xticks(x18[::7],rotation=90)
plt.yticks(rotation=0)
plt.legend(loc = 2, prop={'size': 26})
plt.tight_layout()
# fig.savefig(f'./graphs/warbler_plots/5_years_migrations.jpg', dpi=200);

### Plot and fit individal year migrations

fig, ax = plt.subplots() 
fig.set_size_inches(30, 10)


x = np.array(mean_loc_spring2020['dtnum'])
y = mean_loc_spring2020['lat']
ax.scatter(x,y, label = '2020', s=100, alpha=.6)

linear_model = LinearRegression()
linear_model.fit(x.reshape(-1, 1), y)
y_hat = linear_model.predict(x.reshape(-1, 1))
ax.plot(x, y_hat, color="b", label='2020', linewidth=5)

x19 = np.array(mean_loc_spring2020['dtnum'])
y19 = mean_loc_spring2019['lat']
ax.scatter(x19,y19, label = '2019', s=100, alpha=.6)

linear_model19 = LinearRegression()
linear_model19.fit(x19.reshape(-1, 1), y19)
y_hat19 = linear_model19.predict(x.reshape(-1, 1))
ax.plot(x, y_hat19, color="orange", label='2019', linewidth=5)

x18 = np.array(mean_loc_spring2020['dtnum'])
y18 = mean_loc_spring2018['lat']
ax.scatter(x,y18, label = '2018', s=100, alpha=.6)

linear_model18 = LinearRegression()
linear_model18.fit(x18.reshape(-1, 1), y18)
y_hat18 = linear_model18.predict(x18.reshape(-1, 1))
ax.plot(x, y_hat18, color="green", label='2018', linewidth=5)

x17 = np.array(mean_loc_spring2020['dtnum'])
y17 = mean_loc_spring2017['lat']
ax.scatter(x,y17, label = '2017', s=100, alpha=.6)

linear_model17 = LinearRegression()
linear_model17.fit(x17.reshape(-1, 1), y17)yall = np.array(obsall_day['lat'])
            y2020 = np.array(obs2020_day['lat'])
            
            sample_means_2020 = sample_means_from_population(n_samples=10000, n_summands=500, sampler=y2020)
            sample_means_all = sample_means_from_population(n_samples=10000, n_summands=500, sampler=yall)
            
            newdt = year+timedelta(n)
            
            result = scipy.stats.ttest_ind(sample_means_2020,sample_means_all, equal_var=False)[1]
            strdt = str(newdt)
            d[strdt] = result
y_hat17 = linear_model17.predict(x17.reshape(-1, 1))
ax.plot(x, y_hat17, color="red", label='2017', linewidth=5)

formatter = DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(formatter)

plt.xlabel('Apr-7 to May-22', fontsize=20)
plt.ylabel('Latitude', fontsize=20)
ax.set_facecolor('lightgoldenrodyellow')
plt.title(f'Warbler Spring Migrations 2017-2020', fontsize=60, color = 'saddlebrown')
plt.xticks(x[:], rotation=90)
plt.yticks(rotation=0)
plt.legend()
plt.tight_layout()
# fig.savefig(f'./graphs/warbler_plots/spring_migrations_fit.jpg', dpi=200);

#### Results of Regression
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#### PLOT Combined Means and Fit

fig, ax = plt.subplots() 
fig.set_size_inches(30, 10)

x = np.array(mean_loc_spring_total['obsDt'])
y = mean_loc_spring_total['lat']
ax.scatter(x,y, label = 'Mean Latitude on Date', s=100, alpha=.6)

linear_model = LinearRegression()
linear_model.fit(x.reshape(-1, 1), y)
y_hat = linear_model.predict(x.reshape(-1, 1))
ax.plot(x, y_hat, color="saddlebrown", label='Regression Line Over All Years', linewidth=5)
ax.set_facecolor('lightgoldenrodyellow')

plt.xlabel('Apr-7 to May-22', fontsize=20)
plt.ylabel('Latitude', fontsize=20)
# plt.xlim(0,46)
plt.title(f'Warbler Spring Migrations 2017-2020', fontsize=60, color = 'saddlebrown')
plt.xticks(x[:],rotation=90)
plt.yticks(rotation=0)
formatter = DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(formatter)
plt.legend()
plt.tight_layout()
# fig.savefig(f'./graphs/warbler_plots/all_spring_migrations_fit.jpg', dpi=200);

###OLS RESULTS

X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

### Plot Residuals
y_hat = results.predict(X)
residuals = y_hat-y

fig, ax = plt.subplots() 
fig.set_size_inches(30, 10)

ax.scatter(y_hat,residuals)
ax.axhline(0)

plt.xlabel('Latitude Predictions', fontsize=20)
plt.ylabel('Residuals Between Predicted and Actual', fontsize=20)
ax.set_facecolor('lightgoldenrodyellow')
plt.title(f'Linear Regression Performance', fontsize=60, color = 'saddlebrown')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.legend()
plt.tight_layout()
fig.savefig(f'./graphs/warbler_plots/regression_qq.jpg', dpi=200);


