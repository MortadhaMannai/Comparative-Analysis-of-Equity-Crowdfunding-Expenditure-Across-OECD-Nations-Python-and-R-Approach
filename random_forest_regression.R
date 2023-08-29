# Random Forest Regression

# Importing the dataset
dataset = read.csv('crowdfunding_stats.csv', sep = ',')

# Fitting Random Forest Regression to the dataset
# install.packages('randomForest')
library(randomForest)
set.seed(12)
regressor = randomForest(x = dataset[2],  # dataframe
                         y = dataset$Y,  # vector
                         ntree = 100)

# Predicting a new result with Random Forest Regression
y_pred = predict(regressor, data.frame(PKB = 590000))

# Visualising the Random Forest Regression results (higher resolution)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$PKB), max(dataset$PKB), 100)
ggplot() +
  geom_point(aes(x = dataset$PKB, y = dataset$Y),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(PKB = x_grid))),
            colour = 'blue') +
  ggtitle('GDP vs Crowdfunding in OECD (Random Forest Regression)') +
  xlab('GDP') +
  ylab('Crowdfunding Size')