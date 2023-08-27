# MachineLearning
Project based on Python and R

In this project I'm planning to explain impact of such factors as:
 - price
 - number of bedrooms
 - number of max number of accomodates
 
 on the fact that a given accomodation received good reviews (average equals or more than 4). The listed reviews are taken into consideration only if the place was reviewed at least 3 times.
 
The dataset for this regression changed in comparison to previous projects. In order to test data containing dummy variables, I used survey data obtained in July 2017 in Warsaw by Airbnb. The dataset contains such data as:

room_id, host_id, room_type, last_modified, latitude, longitude - details that directly identify the survey. Those data will not be used in the analysis.

reviews: The number of reviews that a listing has received. It is claimed that around 70% of visits are reviewed. That index was an indicator for me, whether the obtained rating was reliable. E.g. the average rating of 4,5 pulled out of  5 reviews was more worthy for me than an avg rating of 5 based on just 2 opinions.

rating - The average rating out of five that the listing has received from those visitors who left a review.

overall satisfaction - this metric is similar to rating, though not used here due to the formatting case

accomodates - the number of guests a host can accommodate in the given apartament/room

bedroom - number of bedrooms

price - The price for a night stay in local currency (PLN). 
 
The analysis will be provided in Python and in R.
