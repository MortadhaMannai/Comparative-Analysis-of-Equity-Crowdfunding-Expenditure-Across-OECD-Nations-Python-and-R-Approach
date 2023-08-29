# SVR

# Importing the dataset
dataset = read.csv('crowdfunding_stats.csv', sep = ',')
dataset = dataset[c(2,14)]

# Fitting SVR to the dataset
# install.packages('e1071')
library(e1071)
regressor = svm(formula = Y ~ PKB,
                data = dataset,
                type = 'eps-regression',
                kernel = 'radial')

# Predicting a new result
y_pred = predict(regressor, data.frame(PKB = 600000))

# Visualising the SVR results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$PKB, y = dataset$Y),
             colour = 'red') +
  geom_line(aes(x = dataset$PKB, y = predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Forecast vs Reality (SVR)') +
  xlab('GDP') +
  ylab('Crowdfunding size')