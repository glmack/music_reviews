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

To answer these questions we used Student t-test as well as a z-test to produce p-value necessary to reject or accept null hypothesis. Chosen level of confidence was 95%. The reason to choose this level is that we wanted to leave a reasonable margin of error to optimize for:

a) subjective nature of reviewing music albums (there are no fixed guidelinies on how to evaluate music, thus, we cannot make a confidence interval too high)
b) we wanted to be reasonably certain in our evaluations

To peform t-test and z-test we assumed that data is:

- Approximately normally distribuited: we checked the distribution plotting a histogram.
    
- Collected randomly: we collected random samples for each test.
    
- The observations are independent: we can assume that the observations are independent.


## Findings

### Question 1: Is there a statistical difference between 'metal' and 'jazz' music genres?

To compare 'metal' and 'jazz' scores we looked at the scores of metal and jazz genres, taking a random sample of the size 50 from each group.

**Null hypothesis**: there is no statistical difference between reviews scores for 'metal' and 'jazz' genres, that is, the difference in means is equal to 0.

**Alternative Hypothesis**: there is difference between reviews scores for 'metal' and 'jazz' genres: the difference in means is not equal to 0.

Confidence level: 95%

We applied a two-sample t-test. The resulting p-value was smaller that our significance level. So we rejected the null hypothesis in favor of the alternative hypothesis.

### Question 2: If the same person does the review, does he/she score genres differently, in particular, 'metal' and 'jazz' genres?

To answer this questions we performed a 2-tailed paired t-test to see if multigenre reviewrs produced different review scores for 'metal' and 'jazz' genres in particular, since these genres are very different. We took random samples of the size 50 to do the test

**Null hypothesis**: the mean difference between paired observations is equal to zero

**Alternative hypothesis**: the mean difference between paired observations is not equal to zero

Confidence level: 95%

The resulting p-value of p-value is:  0.953 was higher than out significance level aplha=0.05, so we could not reject the null hypothesis.

### Question 3: Looking at the scores produced by one author, are they different from the average scores given by the total of aythors? That, is any of the authors biased?

To answer that question we looked at reviews made by each particular author, and selected those that did more than 50 reviews. Fewer amount of reviews per author would have less normally distribuited data.

For the statistical test from each author we took a sample from each of those authors and applied the custom-built function that looped through the data, created a sample and applied the z-test on each sample. The function returned a list of authors, where p-value was lower than alpha level, implying that those are the authors that give higher or lower average review score than average of all scores across the dataset.

Considering we treated the Pitchfork data as population, we can generalize and say that around 40% of authors give higher or lower review score than average within Pitchfork dataset.