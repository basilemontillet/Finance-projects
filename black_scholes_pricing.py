import numpy as np
import scipy.stats import norm
import matplotlib


def main():
  # make sure that the inputs are considered as float ("numbers")
  s = float(input("enter spot price"))
  k = float(input("enter strike price"))
  r = float(input("enter risk-free rate"))
  v = float(input("enter volatility"))

  # converting time to maturity to annual basis
  time = float(input("enter time to maturity in month"))
  t = time / 12
  
  # calculate d_1 and d_2
  d_1 = (np.log(s/k)+(r+0.5*v**2)*t)/v*np.sqrt(t) # related to the expected value of the stock, given the option expiring ITM
  d_2 = (np.log(s/k)+(r-0.5*v**2)*t)/v*np.sqrt(t) # risk-adjusted proba that option expires ITM

  # calculate the standard normal distribution of d_1 and d_2
  n_1 = norm.cdf(d_1)
  n_2 = norm.cdf(d_2)

  # calculate the price for the call option
  c = s*n_1 - k*np.exp(-r*t)*n_2

  print(c)

if __name__ = "__main__":
  main()

  
  
  
