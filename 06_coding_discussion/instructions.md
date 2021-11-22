# Coding Discussion 06

# Instructions

Building off what we did in lecture this week, please build a model that predicts the _log_ selling price of a house in DC (`PRICE`). Please use what you've learned of the `sklearn` library to accomplish this task.  

I've split this dataset into a training and test dataset (so you don't need to split it on your own). Using the training data, build a model that predicts the price of a residential unit in District of Columbia.

You may use any feature in the dataset to generate a model. Some things to keep in mind:

- Be sure to predict the log Price, not the raw Price
- Be sure to pre-process your data. 
- Be careful of missing data values. You can do whatever you like with them. 
- Try different models (doesn't just need to be the ones we covered in class), some algorithms perform better on a specific data outcome than others. 
- Be sure to tune your model (if it has relevant tuning parameters).

Once you've come up with a model that you think performs well, please test your model on the provided test data and report the mean squared error. 

# Data 

The provided data comes from the D.C. Residential Properties dataset downloaded from Kaggle and available via Open Data DC. The following provides a description of the data as provided at this [link](https://dcdatahub.maps.arcgis.com/sharing/rest/content/items/c5fb3fbe4c694a59a6eef7bf5f8bc49a/info/metadata/metadata.xml?format=default&output=html):

> Computer Assisted Mass Appraisal (CAMA) database. The dataset contains attribution on housing characteristics for residential properties, and was created as part of the DC Geographic Information System (DC GIS) for the DC Office of the Chief Technology Officer (OCTO) and participating D.C. government agencies. This data is used for the planning and management of Washington, D.C. by local government agencies.

Again, the data has been pre-split into a training and test dataset. 


## Submit

Please submit your answer as a Jupyter Notebook in the `Submissions/` folder. Title the notebook with your lastname_firstname_netid (`doe_john_jd568.ipynb`). Be sure to submit a docstring if you write any functions indicating what your function does and all the arguments it takes.  As per usual, please submit your answer to the class repository by Sunday 11:59pm deadline.
