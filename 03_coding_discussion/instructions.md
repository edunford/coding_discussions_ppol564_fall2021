# Coding Discussion 03

# Instructions

## Task

Please read in the Chicago Summer 2018 Crimes Dataset located in the repository folder.

Using the data wrangling methods covered in class this week, create a new data frame where:

- the **_unit of observation_** is the crime type (i.e. `primary_type`),
- the **_column variables_** corresponds with the **_day of the month_**, and
- **_each cell_** is populated by the **_proportion of times that crime type was committed over all days of the month_**
    + For example, assume there were just two days in a month and 2 thefts were committed on the first day, and 1 on the second day, then the _proportion_ of thefts committed on the first day would be .66 and .33 on the second day).

Make sure that:

- all missing values are filled with zeros. Zeros in this case means no crimes were committed that day;
- the data is rounded to the second decimal place; and
- the data frame is printed at the end of the notebook.


## Submit

Please submit your answer as a Jupyter Notebook in the `Submissions/` folder. Title the notebook with your lastname_firstname_netid (`doe_john_jd568.ipynb`). Be sure to submit a docstring if you write any functions indicating what your function does and all the arguments it takes.  As per usual, please submit your answer to the class repository by Sunday 11:59pm deadline.


## Things to keep in mind

To answer this question: we'll want to think carefully about assigning an index, aggregating data by groups, and reshaping data. Everything you need is in the lecture notes.
