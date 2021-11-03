
# Coding Discussion 04

# Instructions

For this coding discussion, let's play around with some of the linear algebra concepts that we've covered in class. Specifically, let's return to our discussion of representing text as vectors and analyzing the angle between those vectors (which as we saw, offers a measure of similarity).

In the `Data/` folder, there are five separate news reports on Turkish President Erdogan addressing the murder of journalist Jamal Khashoggi in `.txt` files. Each contains the same story (relatively speaking) from different sources with different political leanings/interests. In addition to this, I also include `stop-words.csv` file containing common English words that we want to purge from our text (recall there are words that are common to all sentences, like "the" and "and", that we want to remove when comparing documents).

Use what we know about (a) reading in text files, (b) data manipulation, and (c) linear algebra to analyze the difference between these documents. Does each news site report on these stories in a similar way? Which news sites talk about the Khashoggi scandal in similar/dissimilar ways? If you change what words you remove, does the picture of similarity change?

This discussion is largely open. Probe the data however you see fit. The only restriction is that you must calculate the cosine similarity on your own. Don't rely on any canned functions that do this for you.

## Submit

Please submit your answer as a Jupyter Notebook in the `Submissions/` folder. Title the notebook with your lastname_firstname_netid (`doe_john_jd568.ipynb`). Be sure to submit a docstring if you write any functions indicating what your function does and all the arguments it takes.  As per usual, please submit your answer to the class repository by Sunday 11:59pm deadline.


# Miscellaneous

Curious how I scraped these news stories? Check out the [`newspaper`](https://github.com/codelucas/newspaper) module. As we've seen, there are many ways to scrape content from the web, but this module is specifically designed for downloading news articles. I've included my script with the folder for your reference (see `scrape-khashoggi-news.py`).
