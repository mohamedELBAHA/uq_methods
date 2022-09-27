#!/usr/bin/env python
__author__ = " Mohamed El Baha"


#----------------------------------
# Import Libraries
#---------------------------------
import numpy as np
from scipy.stats import norm


# sharpness
def sharpness(std):
    """
    Sharpness as defined in the article (see documentation)
    Parameters
    ----------
    numpy array : std = standard deviations of predictions
    
    Returns 
    -------
        float : sh = Sharpness 
    """
    sh = np.sqrt(np.mean(std**2))
    return sh


# Dispersion
def dispersion(std):
    """ A metric to measure the dispersion of predictions
    
    Parameters  
    ----------
    std : numpy array, standard deviations of predictions
    
    Returns
    -------
    disp : float, dispersion 
    """
    disp = np.sum(np.sqrt((std-np.mean(std)**2))) / (len(std)-1) / np.mean(std)
    return disp



# Negative Log-Likelihood
def neglog(residuals, prediction_stdv):
    """
    Negative Log-Likelihood
    """
    nll_list = []
    for (res, std) in zip(residuals, prediction_stdv):
        nll_list.append(norm.logpdf(res, scale=std))

    nll = -1 * np.sum(nll_list)
    return nll
    
    
# Coverage
def compute_coverage(y_test,y_lower,y_upper,significance,name=""):
    """ Compute average coverage and length, and print results

    Parameters
    ----------

    y_test : numpy array, true labels (n)
    y_lower : numpy array, estimated lower bound for the labels (n)
    y_upper : numpy array, estimated upper bound for the labels (n)
    significance : float, desired significance level
    name : string, optional output string (e.g. the method name)

    Returns
    -------

    coverage : float, average coverage
    avg_length : float, average length

    """
    in_the_range = np.sum((y_test >= y_lower) & (y_test <= y_upper))
    coverage = in_the_range / len(y_test) * 100
    print("%s: Percentage in the range (expecting %.2f): %f" % (name, 100 - significance*100, coverage))
    sys.stdout.flush()

    avg_length = abs(np.mean(y_lower - y_upper))
    print("%s: Average length: %f" % (name, avg_length))
    sys.stdout.flush()
    return coverage, avg_length