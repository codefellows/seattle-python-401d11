# Working with Pandas

NumPy is a spectacular resource for organizing and running fast operations on a data set, but there are some limits in its simplicity.
As noted, NumPy arrays are not extendable, and every entry in the NumPy array must be of the same data type.
When reading data, you must always keep a reference to an explanation of the structure of the data available due to having no column names for your data.

The [Pandas](http://pandas.pydata.org/){:target="_blank"} library builds on top of the robustness and efficiency of the NumPy library, while adding data structures and functionality that allow much more natural interaction with your data sets.

## Getting Started

After running `pip install pandas`, you can import the Pandas library into your Jupyter notebook.

```python
>>> import pandas as pd
```

Most code that you see others use will abbreviate `pandas` as `pd`, though if you're fine with writing out the whole name you can use that.

Pandas has two main data structures to work with: the **Series** and the **DataFrame**.
We'll mostly be working with the latter, but in your travels you may see the former.
Let's see some information about them both.

## Pandas Series

A [Pandas Series](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html){:target="_blank"} is like a NumPy Array in that it takes one data type and is very fast with broadcasting operations across the data it holds.
It's also of a fixed size, unless you concatenate it with another Series.
Indeed, many of the built-in capabilities of the Pandas Series seem to take inspiration from NumPy.
For example:

- `Series.min()` & `Series.max()`
- `Series.argmin()` & `Series.argmax()`
- `Series.sum()`
- `Series.cumsum()` - performs a [cumulative sum](http://mathworld.wolfram.com/CumulativeSum.html){:target="_blank"} across all the values in the series, in order.

Given a Pandas Series, you can also do comparisons across the entire series and perform boolean filters using bracket notation and bitwise operators.

```python
>>> test_series = pd.Series([42, 70, 80, 3, 30, 48, 43, 74, 36, 0])
>>> test_series < 20
0    False
1    False
2    False
3     True
4    False
5    False
6    False
7    False
8    False
9     True
dtype: bool
>>> test_series[(test_series > 20) & (test_series < 60)]
0    42
4    30
5    48
6    43
8    36
dtype: int64
```

The output of the left column are the indices for which the criteria provided was `True`.
The right column contains the values associated with those indices.

Because real data is typically more complex than would be allowed in a one-dimensional array, the `Series` data type doesn't see *too* much use.
However, when you're inspecting individual columns in DataFrames, they'll be visible as Series objects.

## Pandas DataFrame

The most valuable asset of the Pandas package is the **DataFrame** object.
Within a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html){:target="_blank"}, data is organized as columns and rows.
Columns are accessible by name, with either dot notation (`dataframe.column_name`) for single-word names or bracket notation ('dataframe["column_name"]') for those and more complex names.
The rows are auto-incremented integers by default.

All data within a column must be of the same type, though not all data within the DataFrame need share that same restriction.
You can mix a DataFrame up to have a column of strings, another column of integers, another of floats, maybe some timestamps, etc.

Building a DataFrame from a dictionary is a straightforward process, so long as the dictionary's keys have iterables of data as their values.
Pandas will use the keys as column names, and the iterable of values as the data for those columns.

```python
>>> states_dict = {
...     "states": ["New York", "California", "Texas", "Florida", "New Jersey", "Washington"],
...     "capital": ["New York City", "Sacramento", "Austin", "Tallahassee", "Trenton", "Olympia"],
...     "population": [19750000, 38800000, 26960000, 19890000, 8938000, 7062000]
... }
>>> states_df = pd.DataFrame(states_dict)
>>> print(states_df)
         capital  population      states
0  New York City    19750000    New York
1     Sacramento    38800000  California
2         Austin    26960000       Texas
3    Tallahassee    19890000     Florida
4        Trenton     8938000  New Jersey
5        Olympia     7062000  Washington
```

Column names tend to get cast into alphabetical order, whether your dictionary keys existed that way or not.

### Selecting Columns and Rows in a DataFrame

As previously mentioned, columns can be selected by name using either bracket or dot notation.

```python
>>> states_df.states
0      New York
1    California
2         Texas
3       Florida
4    New Jersey
5    Washington
Name: states, dtype: object
>>> states_df['population']
0    19750000
1    38800000
2    26960000
3    19890000
4     8938000
5     7062000
Name: population, dtype: int64
```

Note that when you select one column it tells you what the data type is within that column.
Contrast this with what is returned when checking the `type()` of a given column.

```python
>>> type(states_df["capital"])
<class 'pandas.core.series.Series'>
```

All columns are Pandas Series objects, so anything you can do with a Series you can do with a column in a DataFrame.

Rows are not quite as simple to access, but aren't too bad.
The `.loc` property of a DataFrame is a Pandas indexer, allowing you to access rows by name when you use bracket notation.
In the default setup for a DataFrame, your row names are integers,s o you just provide the number of the row you want and get that data.
If you actually want the row at index 4, you can use the `.iloc` property.

### Setting a New Index

Often you'll find that the default indexing isn't very useful.
Looking at our DataFrame of information on states, each row represents one state.
It would be a lot easier if we could just reference a row by the name of the state that it's referring to.
Luckily, we can **reindex a DataFrame** using the `set_index("column_name")` method.

```python
>>> states_df.set_index("states")
states            capital  population
New York    New York City    19750000
California     Sacramento    38800000
Texas              Austin    26960000
Florida       Tallahassee    19890000
New Jersey        Trenton     8938000
Washington        Olympia     7062000
```

`set_index` returns a **new DataFrame**, where each row is indexed by the state's name.
It's important to note here that this, and most, DataFrame operations **do not mutate the DataFrame by default**.
Instead, if your transformation is successful then a copy is made of your DataFrame with whatever transformation you requested.

If you want to capture the transformation, assign it to a variable.
If you to modify the DataFrame itself, set the `inplace` keyword argument to `True`.
Most methods that would transform a DataFrame have this option available.

### Renaming Columns and Rows

Sometimes we have column names or row names that we don't like.
They may have been automatically generated from some data that we read in, or maybe we simply realized that the name we provided wasn't a good one.

Whatever the case may be, when you want to switch up some column or row names, use the `rename()` method.
It will take a dictionary for either the columns or the rows you want to name (or both!).
The dictionary you provide should have key names referring to the old column names and values corresponding to what you want the new names to be.

```python
>>> states_df.rename(index={
    "New York": "NY",
    "California": "CA",
    "Texas": "TX",
    "Florida": "FL",
    "New Jersey": "NJ",
    "Washington": "WA"
}, columns={
    "capital": "capital city"
})

states   capital city  population
NY      New York City    19750000
CA         Sacramento    38800000
TX             Austin    26960000
FL        Tallahassee    19890000
NJ            Trenton     8938000
WA            Olympia     7062000
```

If you provide key-value pairs that don't yet exist for either the `index` dict or the `columns` dict, they're simply ignored.

### Adding Columns and Rows

DataFrames are not themselves immutable objects.
Data can be modified within columns.
New rows and new columns can be added.
Much like with dictionaries, we can add a new column by assigning a value to a new column name.
The main caveat is that the column you add must have the same size as the other columns in the DataFrame.

```python
>>> states_df["time zone"] = ["EST", "PST", "CST", "EST", "EST", "PST"]
>>> states_df
states            capital  population time zone
New York    New York City    19750000       EST
California     Sacramento    38800000       PST
Texas              Austin    26960000       CST
Florida       Tallahassee    19890000       EST
New Jersey        Trenton     8938000       EST
Washington        Olympia     7062000       PST
```

Rows are a little harder to add.
You can only add rows in a handful of circumstances:

- New rows that are transformations of existing rows
- You are concatenating this DataFrame with another one.

In the later case, a new row (or rows) can be added like so:

```python
>>> georgia = pd.DataFrame({
... "states": ["GA"],
... "capital": ["Atlanta"],
... "population": [10100000],
... "time zone": ["EST"]
... }).set_index("states")
>>> states_df = pd.concat([states_df, georgia])
>>> states_df
                  capital  population time zone
states
New York    New York City    19750000       EST
California     Sacramento    38800000       PST
Texas              Austin    26960000       CST
Florida       Tallahassee    19890000       EST
New Jersey        Trenton     8938000       EST
Washington        Olympia     7062000       PST
GA                Atlanta    10100000       EST
```

### Reducing Columns and Rows

In the same way that you can select individual columns and rows, you can select multiple at once.
Any multiple column or row selection will return a DataFrame object containing only what you specified.
Using bracket notation, supply a list of column names for a subset a columns.
For a subset of rows, use `.loc` with a list of row names.

```python
>>> states_df[["capital", "time zone"]]
                  capital time zone
states
New York    New York City       EST
California     Sacramento       PST
Texas              Austin       CST
Florida       Tallahassee       EST
New Jersey        Trenton       EST
Washington        Olympia       PST
GA                Atlanta       EST

>>> states_df.loc[["New York", "Washington", "California"]]
                  capital  population time zone
states
New York    New York City    19750000       EST
Washington        Olympia     7062000       PST
California     Sacramento    38800000       PST

```

You can chain them together as well.
Keep in mind that each of these operations returns a DataFrame, and these methods and operations can be done on any DataFrame.
So when you're chaining methods together, what you're actually doing is generating a new DataFrame and using that DataFrame's method to produce yet another DataFrame.

```python
>>> one_step = states_df.loc[["New York", "Washington", "California"]]
>>> step_one = states_df.loc[["New York", "Washington", "California"]]
>>> step_two = step_one[["capital", "time zone"]]
>>>
>>> chained_result = states_df.loc[["New York", "Washington", "California"]][["capital", "time zone"]]
>>> chained_result == step_two
            capital  time zone
states
New York       True       True
Washington     True       True
California     True       True
```

### Operating Across Axes

Recall that every DataFrame column is a Series.
As such, you can broadcast operations across the values in that series.

```python
>>> states_df.population / 1E6
states
New York      19.750
California    38.800
Texas         26.960
Florida       19.890
New Jersey     8.938
Washington     7.062
GA            10.100
Name: population, dtype: float64
```

We can also apply the `.sum()` method to the DataFrame.
If we just take the sum of one column, the result is same as performing the sum across a Series.
If we apply the `.sum()` method to the entire DataFrame, it'll apply the sum function to **each column**.

```python
>>> states_df.sum()
capital       New York CitySacramentoAustinTallahasseeTrento...
population                                            131500000
time zone                                 ESTPSTCSTESTESTPSTEST
dtype: object
```

The sum here didn't work out too well because not every column is numerical.
However, you see that it applied the "`+`" operator to every value in the column, in order.

We also have the option to sum across rows instead of down columns.
We do this by providing the argument `axis=1`.
By default this argument is set to 0.
Let's see this at work with a fully-numerical DataFrame.

```python
>>> membership = {
...     "newly-enrolled 2016": [82, 20, 64, 25, 28, 23, 95, 1, 75, 1],
...     "newly-enrolled 2015": [22, 82, 47, 50, 39, 2, 67, 2, 61, 27],
...     "newly-enrolled 2014": [80, 27, 28, 17, 54, 29, 25, 56, 83, 82]
... }
>>> member_df = pd.DataFrame(membership)
>>> member_df.sum(axis=1)
0    184
1    129
2    139
3     92
4    121
5     54
6    187
7     59
8    219
9    110
dtype: int64
```

## Reading/Writing Data with Pandas

It's not often that you'll be building a Dataframe from scratch with a dictionary.
It can absolutely be done, but most times your data will come from an external source and be structured as a DataFrame through one of Pandas' built-in reading functions.

Once we work our Python magic on our data, we then often need to write that data to file.
Maybe we're sharing files amongst our team, preparing it for others to download remotely, or even exporting it as a table for a publication.
Either way, Pandas makes file I/O simple with a handful of well-documented methods.

### Reading Data

It's simple to read data with Pandas if you know the format of your data set.
These are the readong functions in the Pandas library:

```python
>>> [attr for attr in dir(pd) if attr.startswith('read_')]
['read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_msgpack', 'read_parquet', 'read_pickle', 'read_sas', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table']
```

We most often encounter CSV, Excel (`.xls` or `.xlsx`), and JSON files when handling data.
As an example, let's read in data about the Titanic.

```python
>>> titanic_data = pd.read_csv('titanic_data.csv')
>>> titanic_data
     PassengerId  Survived  Pclass  \
0              1         0       3
1              2         1       1
2              3         1       3
3              4         1       1
...
                                                  Name     Sex   Age  SibSp  \
0                              Braund, Mr. Owen Harris    male  22.0      1
1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1
2                               Heikkinen, Miss. Laina  female  26.0      0
3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1
...
     Parch            Ticket      Fare        Cabin Embarked
0        0         A/5 21171    7.2500          NaN        S
1        0          PC 17599   71.2833          C85        C
2        0  STON/O2. 3101282    7.9250          NaN        S
3        0            113803   53.1000         C123        S
...
```

Unless told to do otherwise, Pandas automatically generates column names based on the first line of data in the file.
As with the DataFrames we built from dicts, it auto-increments the index based on the number of rows that have been read.
It also makes assumptions about the data types in each column, settling for the most-applicable type across all values of that column.

We won't need to change the default parameters of `read_csv()` much, but one thing we might encounter is that our data is regularly separated by characters that are not commas.
Other common delimiters are `\t`, `';'`, and `|`.
Regardless of what the separator is, `read_csv()` can handle it.
Just supply the function with the delimiter on read.

```python
>>> pd.read_csv("some/data/file", sep="|")
```

### Badly Handling Null Values

Real world data is far from perfect, and the above data is no exception.

We'll talk later this week about more ways to handle bad data, but for now let's deal with the `NaN` values that populated our DataFrame when we read null values.

When data isn't available for a field (i.e. when the CSV file is empty in a given column), Pandas fills that space by default with a `NaN`.
`NaN` stands for "Not a Number", and so by definition they are not numbers.
They're not strings either, nor are they None.
They come from NumPy's `NaN` object, and if you check their type they are actually floats!

```python
>>> type(titanic_data.Cabin[0])
<class 'float'>
```

But you can't do any math with them.
Any operation involving a `NaN` just returns `NaN`

```python
>>> import numpy as np
>>> np.nan + 5
nan
```

These will make it harder for analysis down the line, so one way of handling them is to simply drop all rows with `NaN` data in any column.
Rather than do some complex filtering, Pandas provides us with a method on our DataFrames for this operation.
It's conveniently called `.dropna()`

```python
>>> len(titanic_data)
891

>>> titanic_data = titanic_data.dropna()
>>> len(titanic_data)
183
```

**WHY THIS IS BAD**

Blindly dropping any data that has any NaN value eliminates such a significant fraction of the data set that any results you pull from that set are seriously in question.
Here especially, dropping all rows with a `NaN` reduces our data set by over 79%!
If we just want to get our analysis pipeline going, this is fine.
However, when we want to report results we need to come up with a more intelligent way of dealing with `NaN` values.
Perhaps only drop rows with `NaN` values in important columns?
We can decide on that later.

### Writing Data

We may read data from some other format and do some transformations (or generate our own data from scratch) and want to share it with others, or save it for something else like input into a database.
Pandas makes this easier with its various file output methods.
Use the `.to_csv()` or `.to_json()` methods on Pandas DataFrames to print data to file.
Let Pandas handle the output for you!

`.to_csv()` takes a path to a file that you want to contain this data to start.
With the default parameters set, it will print out a well-structured CSV file with a column for index values and the first row being the column titles. Should you decide that you don't want to include the index numbers (I often do), you can enforce that like so.

```python
>>> titanic_data.to_csv("path/to/some/file.csv", index=False)
```

If you decide you want your data separated by something that's not a comma, specify that with the `sep` keyword argument

```python
>>> titanic_data.to_csv("path/to/some/file.csv", sep="\t")
```

The method for printing to JSON is a whole lot simpler.
Running the method with its defaults will turn all your column names into keys in the JSON object, properly formatted and all.
All of the column data will then be in an array attached to that key.

```python
>>> titanic_data.to_json("path/to/some/file.json")
```

Simple and clean.
