# Coding Discussion 05

# Instructions

**Can we predict whether someone will vote or not?**

In the discussion folder, you'll find the `turnout.csv` data, which was drawn from the 2012 National Election Survey. The data records the age, eduction level (of total years in school), income, race (caucasian or not), and past voting record (i.e. whether or not the respondent voted in the 2012 Presidential election). The sample is composed of 2000 individual respondents. 

Please break the data up into a training (1600 entries, 80%) and test dataset (400 entries, 20%). 

Build a Naive Bayesian Classifier from scratch that tries to predict whether a respondent will vote in a presidential election or not, pr(Vote==1). The classifier must be built from scratch. Do not use a third party ML or statistical package. 

Run your algorithm and see how it predicts on the test data by calculating the predictive accuracy. 

Does your model perform better than chance (i.e. coin flip)?

When completing this answer, be sure to: 

- comment on all your code
- provide a narrative for what you're doing
- summarize your results and findings

## Submit

Please submit your answer as a Jupyter Notebook in the `Submissions/` folder. Title the notebook with your lastname_firstname_netid (`doe_john_jd568.ipynb`). Be sure to submit a docstring if you write any functions indicating what your function does and all the arguments it takes.  As per usual, please submit your answer to the class repository by Sunday 11:59pm deadline.