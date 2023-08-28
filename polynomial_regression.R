# Polynomial Regression

# Importing the dataset
dataset = read.csv('crowdfunding_stats.csv')
# Excluding the first column (Country name)
dataset = dataset[, 2:ncol(dataset)]

# Fitting Linear Regression to the dataset
lin_reg = lm(formula = Y ~ .,
             data = dataset)

# Fitting Polynomial Regression to the dataset
dataset$PKB2 = dataset$PKB^2
dataset$PKB3 = dataset$PKB^3
dataset$PKB4 = dataset$PKB^4
poly_reg = lm(formula = Y ~ PKB + PKB2 + PKB3 + PKB4,
              data = dataset)

# Visualising the Linear Regression results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$PKB, y = dataset$Y),
             colour = 'red') +
  geom_line(aes(x = dataset$PKB, y = predict(lin_reg, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Forecast vs. reality (Linear Regression)') +
  xlab('GDP') +
  ylab('Crowdfunding size')

# Visualising the Polynomial Regression results
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$PKB, y = dataset$Y),
             colour = 'red') +
  geom_line(aes(x = dataset$PKB, y = predict(poly_reg, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Forecast vs. reality (Polynomial Regression)') +
  xlab('GDP') +
  ylab('Crowdfunding size')

# Visualising the Regression Model results (for higher resolution and smoother curve)
# install.packages('ggplot2')
library(ggplot2)

# Predicting a new result with Linear Regression
predict(lin_reg, data.frame(Level = 6.5))

# Predicting a new result with Polynomial Regression
predict(poly_reg, data.frame(Level = 6.5,
                             Level2 = 6.5^2,
                             Level3 = 6.5^3,
                             Level4 = 6.5^4))