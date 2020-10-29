# Warbler Migration

Why warblers?

Warbler's are sensitive to changes in climate, and have well studied migration patterns. They have very predictable migration patterns. Looking at changes in these patterns can be an indicator for climate change.

Every Year, warblers migrate from their winter homes in South America to their summer homes in Canada. 

My goal is to look at the migration patterns from 2013 to 2020 to determine if 2020 was a typical year for warbler spring migration.
___________

## Ebird Data


[Ebird Api Documentation](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest)

The ebird API supports a handful of requests for recent observation data. Since I was interested in historical data, I was limited to the historic API request. This took in a region code as well as a date. In order to get data from past observations over long periods of time, it was neccessary to write a function to pull each day from a given year. The data pulls came in at about one day every 30 seconds. 

```
https://api.ebird.org/v2/data/obs/{{regionCode}}/historic/{{y}}/{{m}}/{{d}}
```

Data was collected from daily observations into yearly datasets. Some pull requests failed during this process. A function ran through each day and appended it to a CSV. A list of missing days was provided to put back through the API request. 

Duplicate observations also needed to be removed. Some observations were duplicated many times.

A search was performed on the common names column to filter out any birds that were not warblers.

## Number of Warbler Observations Against Total Observations
**A significant percentage of observations are of warblers**

![2017 Warblers Vs. Total](./graphs/monthly_distribution/2017_warbler_observations.jpg)
![2017 Warblers Vs. Total](./graphs/monthly_distribution/2018_warbler_observations.jpg)

After filtering I ended up with an average of 12,200 warbler observations per year.

>Sample of 2019 Warbler Observation Data

![Dataframe Example](./images/obs_df)
____________________


## Mapping and Data Exploration


**Testing Assumption: Observations of warblers correlate with migration**

Sightings of warblers are expected to move further north as the warblers move towards their home in Canada. Plotting every observation on each day based on latitude and longitude assisted in visualizing the migration. Linear regression was used to plot a latitude line across the US for each day. I then compiled those images into a GIF to confirm my assumption.

This was done for each year, with each year showing similar patterns.

![Warbler Gif 2020](./graphs/2020_migration.gif)

_______________________________

**What does the yearly migration pattern look like?**

Plotting the average warbler latitude across every day shows a well defined pattern across all years. 

Each point represents the average latitude of warbler observations on a given day. Each year has a unique color.

![5 Years of Warbler Migration](./graphs/5_years_boxed.jpg)


**Plotting Spring Migration**

After focusing in on spring migration from Apr-7 to May-22 of each year I wanted to visualize the slope of each migration with a regression line in to look at differences between years. 

2018 and 2020 had the largest difference with migration in 2018 starting at a lower average lattitude, and ending at a higher average latitude.

![Warbler Spring Regression](./graphs/warbler_plots/spring_migrations_fit.jpg)

**What does the average latitude look like across all years?**

Combining all years into one linear regression visualizes an estimation of the expected latitude on any given day based on migration from 2013 to 2020.

![All Years Regressions](./graphs/warbler_plots/all_spring_migrations_fit.jpg)

__________________
## Statistical Testing

**Some of these days look like they are far from the regression line. I wwanted to test how many days of each year had a latitude that was equal to the mean latitude across all years.**

To accomplish this I started by look at one observations of one single day in 2020. April-8 had a point that looked far from the mean latitude.

Bootstrapping 10,000 samples (each of length 50) from April-8 2020 and taking the means of those allowed me to plot a normal distribution of means.

Doing the same thing on the samples of all observations from 2013 to 2020 gave me a normal distribution of the mean latitude on April-8 2020 for all years.

I was then able to create a 95% confidence interval for each as well as plot a normal distribution curve to the sampled means.

Using the Welch's T-test with the assumption of non-equal variances I was able to determine that the mean latitude on April-8 2020 was not equal to the mean latitude over all years. 

The reported P-Value was 0.0 and this visualization shows that both distributions do not overlap, confirming the test results.

**This raised the question how many days in each year were latitudes not equal to the mean?**

Automating the test above allowed me to run a T-test for every day of every year from 2014 to 2020 and append the P-Values to a list. The alpha value used to reject the null hypothesis was 0.05. Filtering the list for P-Values under 0.05 and summing those numbers of days over total days observed in that year answered the above question.

* 99.67% of days in 2020 did not have a mean equal to that of all years
* 98.08% of days in 2019 did not have a mean equal to that of all years
* 99.45% of days in 2018 did not have a mean equal to that of all years
* 99.73% of days in 2017 did not have a mean equal to that of all years
* 99.72% of days in 2016 did not have a mean equal to that of all years
* 98.25% of days in 2015 did not have a mean equal to that of all years
* 98.47% of days in 2014 did not have a mean equal to that of all years

This test told me that it is not unusal for the mean on any given day to be different from the average latitude. A better test might be to see how many days were above or below the calculated 5% and 95% Confidence Interval.

### Might Try

* Fit migration curve

* Look at just migration durations only

* Predit future years 

    * Need more years

    *Need to look at trend from one year to the next

