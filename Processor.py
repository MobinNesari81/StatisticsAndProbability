"""
 Project: Create a program which could compute all of the statistics parameters with some data
 This whole project Designed and Developed by : Mobin Nesari 99222107 CopyRight T.Stark
 Hope you enjoy it :D """

# Libraries:
import numpy as np
import matplotlib.pyplot as plt
#   Notice that you need both numpy and matplotlib libraries for running this program.

# Functions:
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








# Main program:
