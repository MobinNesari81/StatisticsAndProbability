"""
 Project: Create a program which could compute all of the statistics parameters with some data
 This whole project Designed and Developed by : Mobin Nesari 99222107 CopyRight T.Stark
 Hope you enjoy it :D """

# Libraries:
import numpy as np
import matplotlib.pyplot as plt
import math
#   Notice that you need both numpy and matplotlib libraries for running this program.

# Functions:
    # Central Tendecies:
def mean(arr):
    #This function compute mean of data.
    summation = sum(arr)
    answer = summation / len(arr)
    return answer

def median(arr):
    #This function compute median of data.
    #Here I assume that data in dicrete.
    length = len(arr)
    if len(arr) % 2 == 1:
        return arr[int( (length + 1) / 2) - 1 ]
    else:
        answer = 1 / 2 * (arr[int( length / 2 ) - 1] + arr[int( length / 2 + 1 ) - 1])
        return answer

def Sortation(arr):
    arr.sort()

def mode(arr):
    #This function compute mode of data. It will also return multiple modes as well.
    seen = []
    counter = []
    for i in arr:
        if i in seen:
            counter[seen.index(i)] += 1
        else:
            seen.append(i)
            counter.append(1)
    answer = []
    max_count = max(counter)
    for i in range(len(counter)):
        if counter[i] == max_count:
            answer.append(seen[i])
    return answer

def quartiles(arr):
    #This function compute quartiles of data.
    #Here I assume that data in dicrete.    
    length = len(arr)
    answer = []
    if (length + 1) * 0.25 % 1 == 0:
        answer.append(arr[int( (length + 1) * 0.25 ) - 1])
        answer.append(arr[int( (length + 1) * 0.5 ) - 1])
        answer.append(arr[int( (length + 1) * 0.75 ) - 1])

    else:
        r = int(math.floor((length + 1) * 0.25))
        w = (length + 1) * 0.25 - r
        answer.append((1 - w) * arr[r - 1] + w * arr[r])
        r = int(math.floor((length + 1) * 0.5))
        w = (length + 1) * 0.5 - r
        answer.append((1 - w) * arr[r - 1] + w * arr[r])
        r = int(math.floor((length + 1) * 0.75))
        w = (length + 1) * 0.75 - r
        answer.append((1 - w) * arr[r - 1] + w * arr[r])
    
    return answer

#   # Variation:

def maximum(arr):
    # This function will return maximum element of data
    answer = max(arr)
    return answer

def minimum(arr):
    # This function will return minimum element of data
    answer = min(arr)
    return answer

def range_data(arr):
    # This function will return range of elements
    answer = maximum(arr) - minimum(arr)
    return answer

def variance(arr, m):
    answer = 0
    for i in arr:
        answer += (i - m) ** 2
    answer /= len(arr)
    return answer

def deviation_from_standard(arr, m):
    answer = math.sqrt(variance(arr, m))
    return answer

def coefficient_of_variation(m, d):
    answer = d / m
    return answer

def first_skewness_coefficient(m,M,ds):
    #This function will compute first skewness coefficient.
    answer = m - M
    answer /= ds
    return answer

def second_skewness_coefficient(m,med,ds):
    #This program compute second skewness coefficient
    answer = 3 * (m - med)
    answer /= ds
    return answer
 



# Main program:
