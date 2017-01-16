[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> ```
>>> import numpy as np
>>> import thinkstats2
>>> import thinkplot
>>> t = np.random.random(1000)
>>> pmf = thinkstats2.Pmf(t)
>>> thinkplot.Pmf(pmf)
>>> thinkplot.Config(xlabel='Random value', ylabel='PMF')
>>> thinkplot.Show()
>>> cdf = thinkstats2.Cdf(t)
>>> thinkplot.Cdf(cdf)
{'xscale': 'linear', 'yscale': 'linear'}
>>> thinkplot.Config(xlabel='Random value', ylabel='CDF')
>>> thinkplot.Show()
```
![Ch4Ex2 Plot](https://github.com/ptpro3/dsp/blob/master/statistics/ch4ex2_pmf.png)
![Ch4Ex2 Plot](https://github.com/ptpro3/dsp/blob/master/statistics/ch4ex2_cdf.png)

The CDF is approximately a straight line, suggesting that the distribution is indeed uniform.