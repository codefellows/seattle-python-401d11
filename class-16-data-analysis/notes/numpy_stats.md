# Descriptive Statistics and Numpy

## What are Descriptive Statistics?

Most analysis projects start with some base-level exploration and characterization of the data.
Descriptive statistics give us an idea of what our data "looks" like.

- where is most of the data clustered?
- what's the spread of the data?
- what's the most common value?
- what are my extremes?

So, before we get into any fancy analytics, let's make sure we can understand the "shape" of our data.
Your basic experiences with Python have shown you about the `min()` and `max()` built-in functions that return the respective minimum and maximum value in an iterable.
What follows will build on that.

## Arithmetic Mean

The **arithmetic mean** is typically known as the [average](https://en.wikipedia.org/wiki/Average){:target="_blank"}, or more simply the [mean](https://en.wikipedia.org/wiki/Mean){:target="_blank"}.
There are other more broad definitions for each of those, but for our purposes they're interchangeable.

For a given set of measurements, the arithmetic mean is defined as **the cumulative sum of values divided by the total number of values**.
We calculate the mean to find **the value around which our data clusters.**
Expressed mathematically, for values in `X` we define the mean as:

![average equation](http://www.sciweavers.org/upload/Tex2Img_1517529934/render.png
){:target="_blank"}

We're a coding school, so we should be able to write something like this in code.
If you're calculating the mean of, say, a list of values, it'd look something like this:

```python
def mean(nums):
    return sum(nums) / len(nums)
```

Let's consider the following set of [Google stock prices](https://www.nasdaq.com/symbol/googl/historical){:target="_blank"} during September 2016:


| Date | Open | High | Low | Close |
| ---- | ---- | ---- | --- | ----- |
| Sep 30, 2016 | 776.33 | 780.94 | 774.09 | 777.29 |
| Sep 29, 2016 | 781.44 | 785.80 | 774.23 | 775.01 |
| Sep 28, 2016 | 777.85 | 781.81 | 774.97 | 781.56 |
| Sep 27, 2016 | 775.50 | 785.99 | 774.31 | 783.01 |
| Sep 26, 2016 | 782.74 | 782.74 | 773.07 | 774.21 |
| Sep 23, 2016 | 786.59 | 788.93 | 784.15 | 786.90 |
| Sep 22, 2016 | 780.00 | 789.85 | 778.44 | 787.21 |
| Sep 21, 2016 | 772.66 | 777.16 | 768.30 | 776.22 |
| Sep 20, 2016 | 769.00 | 773.33 | 768.53 | 771.41 |
| Sep 19, 2016 | 772.42 | 774.00 | 764.44 | 765.70 |
| Sep 16, 2016 | 769.75 | 769.75 | 764.66 | 768.88 |
| Sep 15, 2016 | 762.89 | 773.80 | 759.96 | 771.76 |
| Sep 14, 2016 | 759.61 | 767.68 | 759.11 | 762.49 |
| Sep 13, 2016 | 764.48 | 766.22 | 755.80 | 759.69 |
| Sep 12, 2016 | 755.13 | 770.29 | 754.00 | 769.02 |
| Sep 9, 2016 | 770.10 | 773.24 | 759.66 | 759.66 |
| Sep 8, 2016 | 778.59 | 780.35 | 773.58 | 775.32 |
| Sep 7, 2016 | 780.00 | 782.73 | 776.20 | 780.35 |
| Sep 6, 2016 | 773.45 | 782.00 | 771.00 | 780.08 |
| Sep 2, 2016 | 773.01 | 773.92 | 768.41 | 771.46 |
| Sep 1, 2016 | 769.25 | 771.02 | 764.30 | 768.78 |

If we store all of the closing prices in a list

```python
goog_close = [
              777.29, 775.01, 781.56, 783.01, 774.21, 786.90, 787.21,
              776.22, 771.41, 765.70, 768.88, 771.76, 762.49, 759.69,
              769.02, 759.66, 775.32, 780.35, 780.08, 771.46, 768.78
             ]
```

we can find the average closing price of Google in september by applying the `sum` function and dividing by the length of the list

```python
>>> sum(goog_close) / len(goog_close)
773.6195238095238
```

One *major* drawback to the mean is that it's **very** sensitive to [outliers](https://en.wikipedia.org/wiki/Outlier){:target="_blank"} in the data.
What this means is that if there's a small number of values that are waaaaay outside the norm (either above or below), they'll heavily influence the mean and so that mean will no longer be a good representative of the data.

As an example with our Google data, the prices generally hover around $775 per share.
If Google had one REALLY bad day that dropped its price to around $10 per share, the mean would plummet from $773.62 to $738.91.
Another $10 day would mean $707.22 per share, even though that's not representative of the general trend of the data.

## Median

The median is **the literal middle** of your data if your data was sorted.
It's also known as the 50th percentile (more on that in [quantiles](#quantiles){:target="_blank"}).
If your data has an even number of items, then the median is the average of the two values surrounding the middle of the data.

So, if you've got a sorted list of 5 values, the median value would be at `mylist[2]`.
If 6 values, the median is `(mylist[2] + mylist[3]) / 2`.

The median is useful for finding where the *actual* middle of the data sits, and can at times be more representative of the distribution of the data than the mean.
If the actual middle is close to the maximum, we know that our data is skewed toward high values.
If the median is toward the minimum, probably skewed toward low values.
If the median is close to the average of the data, the data is likely (BUT NOT GUARANTEED) to be evenly-spread.

For our Google stock, we can find the median value in the following way:

```python
>>> sorted_prices = sorted(goog_close)

>>> len(sorted_prices)
21

>>> k = int(len(sorted_prices) / 2)

>>> sorted_prices[k]
774.21
```

The median is often used instead of the mean because it's insensitive to outliers.
If that final day of Google stock had its closing at $1,000,000 per share instead of its current price, the median would still be $774.21.
The largest (or smallest) value in a data set has no bearing on the *middle* of the data.

## Mode

The **mode** is defined as **the most common value** in a data set.
There's no fancy way of calculating this, you just find the value that occurs most often.
One way is to use the `Counter` object from the Python standard library's `collections` package.

```python
>>> from collections import Counter

>>> import random

>>> some_data = [random.randint(0, 10) for i in range(20)]

>>> counts = Counter(some_data)

>>> counts
Counter({1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 6: 3, 7: 1, 8: 3, 10: 4})

>>> counts.most_common()[0]
(10, 4)            # (value, counts)
```

Note that the mode is for an exact value.
This isn't as useful when the data contains continuous, floating-point (decimal) values.
Consider our Google data:

```python
>>> Counter(goog_close).most_common()[0]
(768.88, 1)        # useless
```

## Standard Deviation

The standard deviation is based on the mean of the data.
It's a metric that tells you, on average, **how far the data is spread from its mean value**.
It's all in the name!
All your data will deviate from the average of the data set.
What's the standard for that deviation?

By math, we define it in the following way:

![equation for standard deviation](http://www.sciweavers.org/upload/Tex2Img_1517533289/render.png){:target="_blank"}

Let's break this down into the questions that this equation answers:

- ![distance from mean](http://www.sciweavers.org/upload/Tex2Img_1517533356/render.png){:target="_blank"}: "What's my distance from the mean?"
- ![total distance across data set](http://www.sciweavers.org/upload/Tex2Img_1517533496/render.png){:target="_blank"}: "What’s the total distance from the mean across my data set?"
- ![average distance from the mean](http://www.sciweavers.org/upload/Tex2Img_1517533516/render.png){:target="_blank"}: "What’s my average distance from the mean across my data set?"
- ![unit correction and reduction](http://www.sciweavers.org/upload/Tex2Img_1517533536/render.png){:target="_blank"}: "Get my units right and reduce down from squared-distance."

The larger the spread of the data, the larger the standard deviation.
Consider the opposite––if every data point had the exact same value, the standard deviation would be zero.
That data would be as tight as possible.

If the standard deviation is approximately equal to the mean, then the data is pretty widely spread.
Dividing the standard deviation by the mean gives us that metric of tightness.

Characterizing the spread is important because **it gives us a measure of the variability of the data.**
With our Google data, our standard deviation is as follows:

```python
>>> mean = sum(goog_close) / len(goog_close)

>>> total_dev = sum([(num - mean)**2 for num in goog_close])

>>> from math import sqrt

>>> sqrt((1.0 / len(goog_close)) * total_dev)
7.808048641162937   # <-- the standard deviation

>>> std_dev = _

>>> std_dev / mean
0.010092879510995112
```

The spread of the data is shown to be about 1% of the mean (see output 18).
That tells us that Google's stock was fairly steady over the month of September.

## Quantiles

A **quantile** (or "percentile") looks at the sorted data and asks "what is the value when I'm X% of the way through this data?"
The median is an example of a quantile, representing the value 50% of the way through the data.

Commonly, people are most interested in the **quartiles** of the data set, or the values at 25, 50, and 75% (one quarter, two quarters, three quarters).

Much like how we found the median, we can find quantiles:

```python
>>> k = len(sorted_prices)

>>> q50 = sorted_prices[int(k * 0.5)] # 50th percentile

>>> q50
774.21

>>> q25 = sorted_prices[int(k * 0.25)] # 25th percentile

>>> q25
768.88

>>> q75 = sorted_prices[int(k * 0.75)] # 75th percentile

>>> q75
780.08
```

As with the median's relationship to the mean, we can use these quantiles to get an idea of the _spread_ of the data, but with **a metric that's insensitive to outliers**.
That quantile-based spread is called the **interquartile range**, and is as follows:

![interquartile range equation](http://www.sciweavers.org/upload/Tex2Img_1517534056/render.png){:target="_blank"}

This answers the quation of "what's the spread of the _**middle**_ of our data?"

With our Google data, that interquartile range is

```python
>>> q75 - q25
11.20
```

## Introduction to NumPy

[NumPy](http://www.numpy.org/){:target="_blank"} is the primary package for doing scientific/numerical computing in Python.
You can do lovely things like linear algebra (i.e. matrix math), as well as store regular data like floats, ints, strings, and dicts.

NumPy comes pre-built with some objects and functions that already exist as built-ins for Python or as a part of Python's standard library.
Examples are the number `pi`, the `sum()` function, `min()`, `max()`, trigonometry functions, and square roots.

Because there's so much overlap with either Python's built-in functionality or portions of the standard library, **YOU SHOULD NEVER EVER EVER EVER IMPORT EVERYTHING FROM NUMPY INTO YOUR GLOBAL NAMESPACE!!!**.

When working with NumPy, we alias the `numpy` package as `np`.

```python
>>> import numpy as np

>>> np.pi
3.141592653589793
```

## Working with NumPy Arrays

NumPy introduces a new data structure into the mix called an **Array**.
NumPy Arrays (hereon `np.ndarray`) look like lists and share some of the behavior of lists, but *are most definitely not lists*.
**They are semi-mutable containers of single-type objects.**
Let's see what this means.

You can create an `np.ndarray` from a `list` or `tuple` fairly easily.

```python
>>> this_list = list(range(0, 100, 10))

>>> this_array = np.array(this_list)

>>> print(this_array)
[ 0 10 20 30 40 50 60 70 80 90]
```

No commas! Not a list!

When checking the type of this object, you'll see that it's of the type `np.ndarray`, and inherits direct from the `object` object.

```python
>>> type(this_array)
<class 'numpy.ndarray'>

>>> np.ndarray.__mro__
(<class 'numpy.ndarray'>, <class 'object'>)
```

The `nd` part of `ndarray` stands for `n-dimensional`.
It basically means that it can be nested in a variety of ways, where an array like [ 1 2 3] is one-dimensional, an array like [ [1 2 3] [4 5 6]] is two-dimensional, an array like [ [ [1 2 3] [4 5 6]] [ [7 8 9] [10 11 12]]] is three-dimensional, and so on.

You can reference values in the same way that you would for a `list`.
You can even slice like a list:

```python
>>> this_array[2]
20

>>> this_array[5:12]
array([30, 40, 50, 60, 70])

>>> this_array[7:]
array([70, 80, 90])

>>> this_array[22]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index 22 is out of bounds for axis 0 with size 10

>>> this_array[6:22]
array([60, 70, 80, 90])

>>> this_array[::-2]
array([90, 70, 50, 30, 10])
```

You can also re-assign values like you would in a `list`.

```python
>>> this_array[2] = 12
>>> print(this_array)
[ 0 10 12 30 40 50 60 70 80 90]

>>> this_array[2:4] = [145, 269]
>>> print(this_array)
[ 0 10 145 269 40 50 60 70 80 90]
```

However, you **cannot** reassign a value inside of the `np.ndarray` to a data type that doesn't match the data type of the array.

```python
>>> this_array[2] = "banana"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'banana'
```

In our particular case, if you try to reassign with a numerical value that doesn't match what's in the `np.ndarray` already, it'll assume you made a mistake and alter its type for you.
For example, if your `np.ndarray` is filled with `floats` and you try to reassign with an `int`, it'll convert your `int` into a `float`.
If you try to put a `float` amongst `ints`, it'll round the number down.

```python
>>> this_array[8] = np.pi
[ 0 10 145 269 40 50 60 70 3 90]
```

You can always inspect your `np.ndarray` to see what data type is being held, or you can get Python to tell you.

```python
>>> this_array.dtype
dtype('int64')

>>> type(this_array[0])
<class 'numpy.int64'>
```

Notice, NumPy has its own integer type.
It also uses its own versions of other types like `float` and even `string`.

`np.ndarray` objects have no `append()` or `push()` method.
This is because it's built on the abstract idea of an array, which represents one continuous block of memory, so it cannot be extended on a whim.

As such, you **cannot** extend an existing `np.ndarray`.
You can, however, stick multiple arrays together and assign the result to a new variable with `np.concatenate`:

```python
>>> that_array = np.array(range(256, 266))
>>> other_array = np.array(range(-20, -1))
>>> together = np.concatenate([this_array, that_array, other_array])
>>> print(together)
[ 0 10 145 269 40 50 60 70 3 90 256 257 258 259 260 261 262 263
264 265 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7
-6  -5  -4  -3  -2]
```

Sticking to a single data type in a container of fixed size makes `np.ndarray` operations notably faster than for similar operations on Python `list` or `tuple` objects.
That's also part of the point, and `np.ndarrays` have special methods for math operations for just that reason.

### Broadcasting

For example, if you wanted to double every number in a `list`, you'd have to do something like:

```python
>>> [num * 2 for num in this_list]
>>> [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
```

With `np.ndarray`, you can just apply the math operation directly

```python
>>> this_array * 2
array([  0,  20, 290, 592,  80, 100, 120, 140,   6, 180])
```

This is called **broadcasting**, as in you're taking a signal and sending it to each item in the array at effectively the same time, rather than iterating over the values one at a time and applying the operation.

You can use **broadcasting** to filter across the entire array, finding out which indices match your criteria.

```python
>>> this_array < 50
array([ True,  True, False, False,  True, False, False, False,  True,
       False])

>>> this_array[this_array < 50]
array([ 0, 10, 40,  3])
```

Mathematical operations can be performed between arrays of the same size.

```python
>>> this_array + that_array
array([256, 267, 403, 555, 300, 311, 322, 333, 267, 355])
```

Note here that NumPy added across indices, instead of doing a concatenation like you would with a list.
So effectively, `[this_array[0] + that_array[0], this_array[1] + that_array[1], ... , this_array[-1] + that_array[-1]]`.

Given that, we can see what arrays of a different size raise a `ValueError`

```python
>>> small_array = np.array([2, 2, 2, 2])
>>> this_array / small_array
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (10,) (4,)
```

`np.ndarrays` also have some data aggregation methods, like `.mean()`, `.sum()`, `.min()`

```python
>>> this_array.sum()  # the sum of the entire array
764

>>> this_array.min()  # the minimum value in the array
0

>>> this_array.max()  # the maximum value in the array
296

>>> this_array.mean()  # the arithmetic mean of the array
76.4

>>> this_array.std()  # the standard deviation of the array
84.3091928558209
```

Finally, you can do awesome things like find the index of the minimum/maximum value of the array.
This comes in handy when you need to find that sort of thing quickly.

```python
>>> this_array.argmax()  # the index of the maximum value
3

>>> this_array[this_array.argmax()]
296
```

## Other Useful NumPy Things

If you need an array of some size filled with zeros or ones, `np.zeros` and `np.ones` have you covered.
They both take an argument that is the size of the array that you want.

```python
>>> np.zeros(10)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

>>> np.ones(5, dtype=bool)
array([ True,  True,  True,  True,  True])
```

NumPy is also great for reading and writing numerical data.
[np.loadtxt](https://scipython.com/book/chapter-6-numpy/examples/using-numpys-loadtxt-method/){:target="_blank"} and [np.genfromtxt](https://www.dataquest.io/blog/numpy-tutorial-python/){:target="_blank"} are the two functions used for reading regularly-delimited files like CSV files.
That data is read one row at a time directly into an array of arrays.
This can be somewhat inconvenient when reading in most data sets, as they will often times have different data types across one row.

To get your data organized by columns instead, you can use the `unpack` keyword argument

```python
>>> np.loadtxt("data.csv", unpack=True, delimiter=",")
array([[   1.   ,    1.   ,    1.   ,    1.   ,    1.   ,    1.   ], #  <-- first column
       [   1.   ,    1.   ,    1.   ,    1.   ,    1.   ,    1.   ],
       [   0.   ,    0.   ,    0.   ,    0.   ,    0.   ,    0.   ],
       [   1.   ,    1.   ,    2.   ,    2.   ,    2.   ,    5.   ],
       [   1.   ,    2.   ,    1.   ,    2.   ,    3.   ,    0.   ],
       [   1.855,    1.959,    1.929,    2.054,    2.193,    1.63 ],
       [  16.4  ,   35.2  ,   14.3  ,   31.8  ,   28.5  ,   25.6  ],
       [  15.5  ,   58.7  ,   18.8  ,   40.5  ,  201.7  ,  103.   ]])
```

The above code is assuming that your data file is delimited by commas.
If it's instead delimited by pipes (`"|"`), tabs (`"\t`), or anything else, specify that with the `delimiter` keyword argument.

`np.genfromtxt` does the same thing, but allows you to specify the data type of each incoming column for when you have rows with mixed data.
