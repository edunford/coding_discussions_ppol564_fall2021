# Coding Discussion 02

## Instructions

In the repository, I have provided a dataset from the New York Times on the number of COVID cases and deaths by day, from January 21 through September 2 2020. Note that states do not appear in a dataset prior to the days in which they had their first confirmed case.

The chunk of code below imports the data for this assignment. We'll talk more on Week 5 regarding what this code is doing.

```python
## Read in the data (we would provide this)
import csv
with open('us-states.csv') as file:
    state_covid_data = []
    for row in csv.reader(file):
        state_covid_data.append(row)

len(state_covid_data)
```

Note that the data is imported as a **nested list**. Below I've sliced the list to print off the first 5 rows of the data. Note that the first row contains the variable names. 
```python
state_covid_data[:5]
```
```
[['date', 'state', 'fips', 'cases', 'deaths'],
 ['2020-01-21', 'Washington', '53', '1', '0'],
 ['2020-01-22', 'Washington', '53', '1', '0'],
 ['2020-01-23', 'Washington', '53', '1', '0'],
 ['2020-01-24', 'Illinois', '17', '1', '0']]
```

Please use these data to answer the following questions.

## Question

### (1) Count up the number of _unique_ dates in the data. 


### (2) Find the first date in which the District of Columbia recorded a case. 


### (3) Write a function that takes in a _state name_ as input (e.g. "Wisconsin") and outputs the date of its first case.

```
# For example:
first_case("Wisconsin")
# > "2020-02-05"
```


### (Optional) Bonus

Write a function that takes in a _state name_ as input (e.g. "Wisconsin") and outputs the date when the number of reported cases within the state exceeded 1000.


```
# For example:
locate_date_1000("Wisconsin")
# > "2020-04-03"
```


## Submit

Please submit your answer as a Jupyter Notebook. Title the notebook with your lastname_firstname_netid (`doe_john_jd568.ipynb`). Be sure to submit a docstring indicating what your function does and all the arguments it takes.  As per usual, please submit your answer to the class repository by the Sunday 11:59pm deadline.


## Things to keep in mind

To answer this question: we'll want to use both of what we learned regarding loops, data types and functions. Specifically, since the data is read in as a nested list, you'll want to be familiar with the `list` methods and loops. 

In addition, keep in mind that the first row entry in the data (`state_covid_data[0]`) corresponds with variable names, but is not a data entry itself. 

## Aim 

In this coding discussion, we will have done three things: 

1. Subsetted and worked with real data represented as a nested list 
2. Practiced writing loops to move through nested data structures
3. Practiced writing functions
