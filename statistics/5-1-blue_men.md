[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

5'10" = 177.80 cm  
6'1" = 185.42 cm  
```
>>> import scipy.stats
>>> mu = 178
>>> sigma = 7.7
>>> male_dist = scipy.stats.norm(loc=mu, scale=sigma)
>>> male_dist.cdf(185.42) - male_dist.cdf(177.80)
0.34274683763147368
```
About 34% of the US male population is eligible.