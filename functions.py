import numpy as np
from math import sqrt
from statsmodels.stats.weightstats import ztest

def sample_var(x1, x2):
    '''Returns sample variance value for 2-samples'''
    sum_x1 = 0
    sum_x2 = 0
    
    for i in x1:
        sum_x1 += (i - x1.mean())**2
        
    for j in x2:
        sum_x2 += (j - x2.mean())**2
        
    return (sum_x1 + sum_x2) / (len(x1) + len(x2) - 2)

def twosample_tstatistic(x1, x2):
    '''Returns t-statistic value for 2-samples test'''
    return (x1.mean() - x2.mean()) / sqrt(sample_var(x1, x2) * (1/len(x1) + 1/len(x2)) )

def get_author_scores(list_of_dict):
    '''Iterate throught a list of dictionaries representing dataframe's rows and returns a dictionary with
    author names and a list of scores ordered by date'''
    
    authors_scores = {}
    
    for i in list_of_dict:
        
        if i['author'] in authors_scores.keys():
            #update dictionary values for this author
            authors_scores[i['author']]['scores'].append(i['score'])
            authors_scores[i['author']]['dates'].append(i['pub_date'])
        
        else:
            #add this author name to authors_scores keys
            authors_scores[i['author']] = {'scores': [], 'dates': []}

            authors_scores[i['author']]['scores'].append(i['score'])
            authors_scores[i['author']]['dates'].append(i['pub_date'])
        
    return authors_scores


def get_biased_authors_manual(authors_dict, pop_mean, pop_std, alpha):
    '''Apply z-test to samples retrieved from authors_dict.
    Returns a list of author names where the null hypothesis of
    the z-test was rejected'''
    biased_authors = []
    
    for key, value in authors_dict.items():
        sample_mean = np.mean(value['scores'])
        
        z = (sample_mean - pop_mean) / pop_std/sqrt(len(value['scores']))        

        if z < -1.96 or z > 1.96:
            print('Reject null hypothesis')
            biased_authors.append([key, z])

    return biased_authors

def get_biased_authors(authors_dict, pop_mean, alpha):
    '''Apply statsmodels library's z-test to values retrieved from authors_dict.
    Returns a list of author names where the null hypothesis of
    the z-test was rejected'''
    
    biased_authors = []
    
    for key, value in authors_dict.items():
        scores = value['scores']
        
        z_statistic, p_value = ztest(scores, value=pop_mean)

        if p_value < alpha:
            biased_authors.append([key])   
    
    return biased_authors



def get_biased_authors_with_samples(authors_dict, pop_mean, alpha):
    '''Apply statsmodels library's z-test to random samples of the values retrieved
    from authors_dict. Returns a list of author names where the null hypothesis of
    the z-test was rejected'''
    
    biased_authors = []
    
    for key, value in authors_dict.items():
        
        scores = np.array(value['scores'])
    
        sample = np.random.choice(scores, 50) 

        z_statistic, p_value = ztest(sample, value=pop_mean)

        if p_value < alpha:
            biased_authors.append([(key, p_value)])   
    
    return biased_authors
            


    
    
#functions used in McNemar test
    
def process_row(row):
    """for each row in array, returns array representing one of four categories"""
    if row[0] == row[1] and row[0] == row[2]: # 
        result = [1,0,0,0]
    
    elif row[0] == row[1]:
        result = [0,1,0,0]
        
    elif row[0] == row[2]:
        result = [0,0,1,0]
        
    else:
        result = [0,0,0,1]
    
    return np.array(result)


def process_ndarray(array):
    '''Returns a numpy array suitable for McNemar test'''
    result = sum([process_row(row) for row in array])
    return np.array([[result[0], result[2]], [result[1], result[3]]])
    