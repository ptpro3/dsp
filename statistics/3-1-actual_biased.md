[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> ```
>>> import thinkstats2
>>> import probability
>>> import nsfg
>>> import thinkplot
>>> nsfg_data = nsfg.ReadFemResp()
>>> pmf = thinkstats2.Pmf(nsfg_data.numkdhh, label='numkdhh')
>>> pmf_biased = probability.BiasPmf(pmf, label='biased')
>>> pmf.Mean()
1.0242051550438309
>>> pmf_biased.Mean()
2.4036791006642821
>>> thinkplot.PrePlot(2)
>>> thinkplot.Pmfs([pmf, pmf_biased])
>>> thinkplot.Config(xlabel='# of Kids', ylabel='PMF')
>>> thinkplot.Show()
```
![Ch3Ex1 Plot](https://github.com/ptpro3/dsp/blob/master/statistics/ch3ex1_plot.png)