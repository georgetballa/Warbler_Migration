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


### Transform Data
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

############Transforms for testing only one day

obsall = obsall.reset_index()
obsall = obsall.drop(columns='index')
obsall['obsDt'] = pd.to_datetime(obsall['obsDt']).dt.date
mask = ((obsall['obsDt'] == date(2020,4,8)) | (obsall['obsDt'] == date(2019,4,8)) | (obsall['obsDt'] == date(2018,4,8)) | (obsall['obsDt'] == date(2017,4,8)) | (obsall['obsDt'] == date(2016,4,8)) | (obsall['obsDt'] == date(2015,4,8)) | (obsall['obsDt'] == date(2014,4,8)) | (obsall['obsDt'] == date(2013,4,8)))
obsall_apr_8 = obsall.loc[mask]
obsall_apr_8 = obsall_apr_8.reset_index()

obs2020_r = obs2020.reset_index()
obs2020_r = obs2020_r.drop(columns='index')
obs2020_r['obsDt'] = pd.to_datetime(obs2020_r['obsDt']).dt.date
mask = ((obs2020_r['obsDt'] == date(2020,4,8)))
obs2020_apr_8 = obs2020_r.loc[mask]
obs2020_apr_8 = obs2020_apr_8.reset_index()

y = np.array(obsall_apr_8['lat'])
scipy.stats.normaltest(y)
#It is unlikely that the distribution is normal

###Plot bootstraped distribution of means from all years:
y = np.array(obsall_apr_8['lat'])
sample_means_obsall = sample_means_from_population(
    n_samples=10000, n_summands=500, sampler=y)

mean_sample_means_obsall = np.mean(sample_means_obsall)
variance_sample_means_obsall = np.var(sample_means_obsall)
sample_means_model_obsall = stats.norm(mean_sample_means_obsall, np.sqrt(variance_sample_means_obsall))

fig, ax = plt.subplots(1, figsize=(10, 4))
ax.hist(sample_means_obsall, bins=50, density=True, color="yellow", alpha=0.5,
            label="Histogram of Sample Means")
x = np.linspace(30.5,32.5, 100)
ax.plot(x, sample_means_model_obsall.pdf(x), linewidth=2, color="saddlebrown", 
        label="Normal PDF With Same Mean and Variance")

upper_bound_obsall = np.percentile(sample_means_obsall,97.5)
lower_bound_obsall = np.percentile(sample_means_obsall,2.5)
bounds_obsall = upper_bound_obsall, lower_bound_obsall


ax.axvline(lower_bound_obsall, label = f'Lower Bound 2.5% CI: {str(round(lower_bound_obsall,4))}')
ax.axvline(upper_bound_obsall, label = f'Upper Bound 97.5% CI: {str(round(upper_bound_obsall,4))}')


ax.set_title("Distributon of All Years Sample Means 8-Apr (Size = 10000)", color = 'saddlebrown')
plt.xlabel('Latitude')
plt.ylabel('pdf of sampled means')
ax.legend(loc='lower left');
# fig.savefig(f'./graphs/warbler_plots/CLT_all_years_8-Apr.jpg', dpi=200);

### Plot distribution of means for just one year:
y = np.array(obs2020_apr_8['lat'])
sample_means_obs2020 = sample_means_from_population(
    n_samples=10000, n_summands=500, sampler=y)

mean_sample_means_obs2020 = np.mean(sample_means_obs2020)
variance_sample_means_obs2020 = np.var(sample_means_obs2020)
sample_means_model_obs2020 = stats.norm(mean_sample_means_obs2020, np.sqrt(variance_sample_means_obs2020))

fig, ax = plt.subplots(1, figsize=(10, 4))
ax.hist(sample_means_obs2020, bins=50, density=True, color="yellow", alpha=0.5,
            label="Histogram of Sample Means")
x = np.linspace(32.5,34.5, 100)
ax.plot(x, sample_means_model_obs2020.pdf(x), linewidth=2, color="saddlebrown", 
        label="Normal PDF With Same Mean and Variance")

upper_bound_obs2020 = np.percentile(sample_means_obs2020,97.5)
lower_bound_obs2020 = np.percentile(sample_means_obs2020,2.5)
bounds_obs2020 = upper_bound_obs2020, lower_bound_obs2020


ax.axvline(lower_bound_obs2020, label = f'Lower Bound 2.5% CI: {str(round(lower_bound_obsall,4))}')
ax.axvline(upper_bound_obs2020, label = f'Upper Bound 97.5% CI: {str(round(upper_bound_obsall,4))}')


ax.set_title("Distributon of 2020 Sample Means 8-Apr (Size = 10000)", color = 'saddlebrown')
plt.xlabel('Latitude')
plt.ylabel('pdf of sampled means')
ax.legend(loc='lower left');
# fig.savefig(f'./graphs/warbler_plots/CLT_2020_8-Apr.jpg', dpi=200);

### Plot Distributions Together

fig, ax = plt.subplots(1, figsize=(10, 4))

x = np.linspace(30,34.5, 100)
y2 = np.array(obsall_apr_8['lat'])
sample_means_obsall = sample_means_from_population(n_samples=10000, n_summands=500, sampler=y2)

mean_sample_means_obsall = np.mean(sample_means_obsall)
variance_sample_means_obsall = np.var(sample_means_obsall)
sample_means_model_obsall = stats.norm(mean_sample_means_obsall, np.sqrt(variance_sample_means_obsall))


ax.hist(sample_means_obsall, bins=50, density=True, color="yellow", alpha=0.5,
            label="Histogram of Sample Means- All Years")

ax.plot(x, sample_means_model_obsall.pdf(x), linewidth=2, color="saddlebrown", 
        label="Normal PDF of Means - All Years")



y = np.array(obs2020_apr_8['lat'])
sample_means_obs2020 = sample_means_from_population(
    n_samples=10000, n_summands=500, sampler=y)

mean_sample_means_obs2020 = np.mean(sample_means_obs2020)
variance_sample_means_obs2020 = np.var(sample_means_obs2020)
sample_means_model_obs2020 = stats.norm(mean_sample_means_obs2020, np.sqrt(variance_sample_means_obs2020))


ax.hist(sample_means_obs2020, bins=50, density=True, color="saddlebrown", alpha=0.5,
            label="Histogram of Sample Means - 2020")

ax.plot(x, sample_means_model_obs2020.pdf(x), linewidth=2, color="yellow", 
        label="Normal PDF of Means - 2020")


ax.set_title("Distributon of 2020 Sample Means 8-Apr (Size = 10000)", color = 'saddlebrown')
ax.legend(loc='lower left');
plt.xlabel('Latitude')
plt.ylabel('pdf of sampled means')
# fig.savefig(f'./graphs/warbler_plots/CLT_overlay.jpg', dpi=200);

### Ttest Results for one day
scipy.stats.ttest_ind(sample_means_obs2020,sample_means_obsall, equal_var=False)

### Do the test above for every day
test_results2020 = mean_differentiator(obsall, obs2020, date(2020,1,1))
test_results2019 = mean_differentiator(obsall, obs2019, date(2019,1,1))
test_results2018 = mean_differentiator(obsall, obs2018, date(2018,1,1))
test_results2017 = mean_differentiator(obsall, obs2017, date(2017,1,1))
test_results2016 = mean_differentiator(obsall, obs2016, date(2016,1,1))
test_results2015 = mean_differentiator(obsall, obs2015, date(2015,1,1))
test_results2014 = mean_differentiator(obsall, obs2014, date(2014,1,1))


percent_days(test_results2020, '2020')
percent_days(test_results2019, '2019')
percent_days(test_results2018, '2018')
percent_days(test_results2017, '2017')
percent_days(test_results2016, '2016')
percent_days(test_results2015, '2015')
percent_days(test_results2014, '2014')

