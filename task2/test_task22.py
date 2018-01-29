from __future__ import division
import numpy as np

def div(a, b):
	return(a/b)
def numpydiv(a,b):
	return np.array(a)/np.array(b)

def test_div():
	assert div(2,8) == 0.25

def test_numpydiv():
	assert numpydiv(2,8) == 0.25
