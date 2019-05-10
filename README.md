# music_reviews

**Team**: [Lee Mackey](https://github.com/glmack) and [Anna Zubova](https://github.com/AnnaLara)

## Structure

**Working jupyter notebook**: [link]()

**Presentation**: [link]()

Functions used in the jupyter notebook can be found in the `functions.py` file.


## Project overview

**Project goal**: explore Pitchfork Apply different methods of hypothesis testing to [music reviews dataset](https://www.kaggle.com/nolanbconaway/pitchfork-data) to produce valuable insights.

**Data exploration**

The raw data was contained in a sqlite database with no defined relations between tables. We loaded the data and converted it to a Postgres database using `pgloader` migration tool.

We used SQL commands for data querying and exploration as well as `pandas` library.

**Hypothesis testing**

We explored the relationships between music genres, authors and review scores.

We conducted 3 standard statistical test to answer the following questions:

- Is there a statistical difference between 'metal' and 'jazz' music genres?
- If the same person does the review, does he/she score genres differently, in particular, 'metal' and 'jazz' genres?
- Looking at the scores produced by one author, are they different from the average scores given by the total of aythors? That, is any of the authors biased?

**Methodology and assumptions**

To answer these questions we used Student t-test as well as a z-test to produce p-value necessary to reject or accept null hypothesis. Chosen level of confidence was 95%. The reason to choose this level is that we wanted to leave a reasonable margin of error to optimize for:

a) subjective nature of reviewing music albums (there are no fixed guidelinies on how to evaluate music, thus, we cannot make a confidence interval too high)
b) we wanted to be reasonably certain in our evaluations

To peform t-test and z-test we assumed that data is:

- Approximately normally distribuited: we checked the distribution plotting a histogram.
    
- Collected randomly: we collected random samples for each test.
    
- The observations are independent: we can assume that the observations are independent.

**Findings**

Throughout the analysis we dicovered that these are the answer to the questions :

1. There is statistical difference between review scores of 'metal' genre and 'jazz' genre.
2. However, when the same person does the review, they do not assign different scores to 'metal' and 'jazz' genres.
3. The reviewers have no particular bias towards assigning higher or lower score in general comparing to mean dataset score. 