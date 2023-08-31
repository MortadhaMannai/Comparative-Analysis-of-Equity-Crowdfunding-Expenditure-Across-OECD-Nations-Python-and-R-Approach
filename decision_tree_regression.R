# Decision Tree Regression

# Importing the dataset
dataset = read.csv('crowdfunding_stats.csv', sep = ',')
#dataset = dataset[c(2,14)]

# no feature scaling - the dataset is not based on euclidean distances
# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Decision Tree Regression to the dataset
# install.packages('rpart')
library(rpart)
regressor = rpart(formula = Y ~ PKB,
                  data = dataset,
                  control = rpart.control(minsplit = 2))

# Predicting a new result with Decision Tree Regression
y_pred = predict(regressor, data.frame(PKB = 600000))

# Non-continuous model: Visualising the Decision Tree Regression results (higher resolution)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$PKB), max(dataset$PKB), 1)
ggplot() +
  geom_point(aes(x = dataset$PKB, y = dataset$Y),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(PKB = x_grid))),
            colour = 'blue') +
  ggtitle('GDP vs Crowdfunding in OECD (Test set)') +
  xlab('GDP') +
  ylab('Crowdfunding size')

# Plotting the tree
plot(regressor)
text(regressor)