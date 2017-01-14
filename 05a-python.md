# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of values, but tuples are immutable. This allows tuples to be used as keys in dictionaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets both contain values, but sets are unordered and don't support indexing.  
```
myList = [1,2,3]	# indexed list
mySet = {1,2,3}		# unordered set
```
Sets are faster for element search: O(1) for sets vs. O(n) for lists because sets are implemented using hash tables.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` allows creation of anonymous functions at runtime. They can be used to return expressions or function results anywhere in the code.
```
>>> t
[('a', 2), ('b', 1), ('c', 0)]
>>> sorted(t, key = lambda x: x[1])
[('c', 0), ('b', 1), ('a', 2)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow convenient construction of lists.
```
>>> [x**2 for x in range(4)]
[0, 1, 4, 9]
>>> map(lambda x: x**2, [0,1,2,3])
[0, 1, 4, 9]
>>> filter(lambda x: x==2, [0,1,2,3])
[2]
>>> {x**2 for x in range(4)}
set([0, 1, 4, 9])
>>> {key:value**2 for (key,value) in [(0,0),(1,1),(2,2),(3,3)]}
{0: 0, 1: 1, 2: 4, 3: 9}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





