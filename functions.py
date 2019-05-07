import numpy as np
from math import sqrt

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
    