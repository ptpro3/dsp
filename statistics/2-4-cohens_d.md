[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Comparison of means:  
```
>>> firsts.totalwgt_lb.mean()
7.201094430437772
>>> others.totalwgt_lb.mean()
7.325855614973262
```

Cohen's _d_ shows the difference in means is -.089 standard deviations:
```
>>> thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
-0.088672927072602
```

This result is larger in magnitude than the difference in pregnancy length of .029 standard deviations, but it is still relatively small and could be clinically insignificant considering the sample size.