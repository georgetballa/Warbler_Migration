# Warbler Migration





### Getting the Data

[Ebird Api Documentation](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest)

```
https://api.ebird.org/v2/data/obs/{{regionCode}}/historic/{{y}}/{{m}}/{{d}}
```

The ebird API support a handful of requests for recent observation data. Since I was interested in historical data, I was limited to the historic API request. This took in a region code as well as a date. In order to get data from past observations over long periods of time, it was neccessary to write a function to pull each day from a given year. The data pulls came in at about one day every 30 seconds. After running for a few days, I had data for each day from 2013 to 2020. Some pull requests failed during this process. A function was written to check that all days existed and woudlrequest missing days. Another function was used to merge all days from a given year into a CSV. Some processing was done to remove duplicate observations. It appears that some observations were duplicated many times, possibly due to the user pressing submit many times on the same inputs. I was able to confidently remove these duplicates as the observations had both date and time of observation. Only completely identical rows were removed.



____________________


### Mapping and Data Exploration

![Warbler Observations 2020](./graphs/2020_migration.gif)

Plotted Coordinates Each Day Over a Year

![Warbler Observations 2020](./graphs/5_years_migrations.jpg)


Fit Regression Line to Each Day
![Warbler Observations 2020](./graphs/warbler_plots/spring_migrations_fit.jpg)





Saw clear movement latitudally

Plot of Means each day for 5 years
Overlay to Visualize Trend
No immediately apparent trend

Look at just migration weeks where movement is linear
Plot Regression for each year

Plot all years as one set
Plot Regression
Predict Future Dates








### Might Try

* Fit migration curve

* Look at just migration durations only

* Predit future years 

    * Need more years

    *Need to look at trend from one year to the next

