# Simple Linear Regression

# Importing the dataset
dataset = read.csv('crowdfunding_stats.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(111)
split = sample.split(dataset$Y, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Simple Linear Regression to the Training set
# All variables (except country)
regressor = lm(formula = Y ~ . -Kraj,
               data = training_set)
# GDP, language variables
regressor = lm(formula = Y ~ PKB + three_languages_or_more + Turnout + IT_employment,
               data = training_set)

summary(regressor) # GDP and IT employment turned out to be valuable 

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Visualising the Training set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$PKB, y = training_set$Y),
             colour = 'red') +
  geom_line(aes(x = training_set$PKB, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('GDP vs Crowdfunding in OECD (Training set)') +
  xlab('GDP') +
  ylab('Crowdfunding size')

# Visualising the Test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$PKB, y = test_set$Y),
             colour = 'red') +
  geom_line(aes(x = training_set$PKB, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('GDP vs Crowdfunding in OECD (Test set)') +
  xlab('GDP') +
  ylab('Crowdfunding size')