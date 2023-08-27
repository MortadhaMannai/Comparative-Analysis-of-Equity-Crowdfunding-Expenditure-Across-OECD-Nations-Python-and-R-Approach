# Multiple Linear Regression

# Importing the dataset
dataset = read.csv('crowdfunding_stats.csv')

# Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(111)
split = sample.split(dataset$Y, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Multiple Linear Regression to the Training set. The country is irrelevant here.
regressor = lm(formula = Y ~ .-Kraj,
               data = training_set)
summary(regressor)

# Refitting Multiple Linear Regression to the Training set. Backward elimination used. Last try below.
regressor = lm(formula = Y ~ PKB ,
               data = training_set)
summary(regressor)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Visualising the gap between Test set and y_pred results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$PKB, y = test_set$Y),
             colour = 'red') +
  geom_point(aes(x = test_set$PKB, y = y_pred),
             colour = 'green') +
  #geom_line(aes(x = training_set$PKB, y = predict(regressor, newdata = training_set)),
  #          colour = 'blue') +
  ggtitle('GDP vs Crowdfunding in OECD (Test set)') +
  xlab('GDP') +
  ylab('Crowdfunding size')