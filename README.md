# MachineLearning
Project based on Python and R

In this project I'm planning to explain difference between OECD countries in terms of money spent in each of them on "Crowdfunding" projects (*)

I'll look for explanation in independent variabes such as those below:

economic factors:
- GDP value
- PPP (purchasing power parity)

"open-mindeness":
- number of foreign languages spoken

social awareness:
- electoral turnout
- percentage of people working in R&D sectors

sense of security:
- European Patent Office patents gained (per habitant)
- Number of violations by the government reported by residents of the country

technology awareness:
- number of purchases made online
- percentage of people working in IT

Data used in the analysis is obtained from the Eurostat database. It covers latest possible years (oldest data, concerning electoral turnout, reaches up to 2011).

The data analysis is developed gradually and is going to contain such methods as:

- Basic Linear Regression
- Polynomial Regression
- SVR
- Random Forrest Regression
- Logistic Regression
- Kernel SVM
- Apriori
- Clustering

The analysis will be provided in Python and in R.

(*) One and only type of crowdfunding I'm going to analyse is "Equity crowdfunding". Equity crowdfunding involves the issuance of securities whereas the other forms of crowdfunding do not. Almost every country in the world regulates the selling and issuance of securities. Thus, I'll focus merely on that kind of crowdfunding, as the only case of crowdfunding that has trustworthy sources of information.