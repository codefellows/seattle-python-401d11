# Python and Jupyter Notebook

The vast majority (if not the entirety) of our work this week will be performed in the [Jupyter Notebook](http://jupyter.org/){:target="_blank"} ecosystem.
Jupyter is an amazing tool for experimenting with code and including annotations.
Much work in data science and machine learning, as well as plenty of work in the academic sciences, is done inside of and shared via Jupyter Notebooks.
If we were artists, this would be our canvas.

## What is Data Science?
Data Science or Data Analytics is a process of analyzing large sets of data points to generate answers to questions related to that data set.

It's common to follow what's considered a Scientific Process for working with data sets, so we'll talk quickly about one process to support our workflow.
1. Ask an interesting question. (simple!)
    - You may already have a data set identified at this point, and it's common to do so.
    - If that's the case you may put pen to paper and consider a series of questions that you would like to evaluate through this analysis.
2. Get the data!
    - There are vast amounts of data online through the use of APIs, direct downloads, and other web portals.
3. Explore the data
    - Start working through small incremental steps to determine in what capacity you can work with the data.
    - If you're ready, you can start answering such questions that you've already identified.
5. Communicate and Visualize the results
    - This is the primary point at which we start documenting our data results through the use of code and associated tools.

## Getting Started
Start a new environment and install Jupyter just like any other Python package.

```
$ python3 -m venv ENV
$ source ENV/bin/activate
(ENV) $ pip install jupyter
```

**Hey Instructor!** Those steps above are different than I'm expecting.  **_What is the meaning of this???_**.

Starting a Jupyter Notebook is fairly straightforward.
The notebook environment is initialized from the command line:

```
(ENV) $ jupyter notebook
```

When we invoke that shell command we get the following written to our terminal:

```
[I 15:15:00.270 NotebookApp] Serving notebooks from local directory: /current/directory/path/
[I 15:15:00.270 NotebookApp] 0 active kernels
[I 15:15:00.270 NotebookApp] The Jupyter Notebook is running at:
[I 15:15:00.270 NotebookApp] http://localhost:8888/?token=6cee8197d9a06ee4c37d3ce9d55c7c7c88f4a082265e8e71
[I 15:15:00.270 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 15:15:00.274 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=6cee8197d9a06ee4c37d3ce9d55c7c7c88f4a082265e8e71
0:97: execution error: "http://localhost:8888/tree?token=956b3764b24e2c9a9fde218047cb7fce1445c5f03471fdba" doesn’t understand the “open location” message. (-1708)
```

Of this output, here's what's important:

- Jupyter started a local server (more on this next week) on your machine for running its notebooks
- If you want to see anything involving the notebooks while it's running, visit `http://localhost:8888/?token=somelongstringthatisyourlogin`, as that's where Jupyter is serving up the notebook files

Once these messages are posted, Jupyter will open a new tab in your browser at the `localhost` address.
If your browser isn't open, it'll open your browser with a tab pointing at that URL.

Within the `/tree` tab there's an interface with its own menu:

- Files (currently in use)
- Running
- Clusters

For our purposes, we'll only be worried about the `Files` tab.
If in the future you're handling any multithreaded computations, you'll need an awareness of the `Clusters` tab.

In the `Files` tab, you'll see a listing of the directories and files within your current working directory.
To actually create a new notebook, click the `New` button and choose `Python 3`

## Using Jupyter Notebook

Once a new notebook opens, you'll see what looks like an `iPython` prompt, as well as a couple of menus and a few other things.

- The title of the notebook (currently "Untitled")
- The `File/Edit/View/Insert/Cell/Kernal/Help` menu
- A sub-menu for copying, pasting, saving, and navigating the notebook
- A dropdown menu (currently selecting "Code"), allowing you to change what inputs are rendered in the notebook.

After about 2 minutes, you'll see a new message or two in your terminal.
Notebook files autosave if there's been no previous save within the last two minutes.
Your notebook will currently be saved as `Untitled.ipynb`, taking the name of the file from the title of the notebook.
Changing the title changes the file's name.
The file extension is `.ipynb` because when Jupyter was first started it was known as "IPython Notebook".

### Write Some Code

Opening a new notebook started us off with an empty cell.
Within this cell you write code as you would at the command line or in a script.
Syntax highlighting is automatic.
Execute code within a cell with `Shift + Enter`

```python
In [1]: print("Hello World")
Hello World
```

If executed, code prints to "Standard Out" (`stdout`), which in this case is just the notebook itself.
Any output going to `stdout` appears below the cell that generated it.
You can also write multiple lines of code in the same cell and code blocks, with Jupyter providing auto-indentation.

Because it's based on iPython, the same commands work for checking documentation.

```python
In [2]: sum?
```

Jupyter pops up a mini-window containing the top-level documentation.
You can also get more detailed documentation with `help`.

```python
In [3]: help(sum)
```

Jupyter prints the detailed documentation below that cell in a scrollable field.

One of the largest differences between Jupyter and the iPython shell is visual code order vs executed code order.
In the iPython shell you're always progressing forward going down, line-by-line.

With Jupyter, every cell is editable and executable at any time.
This can trip you up when you've been experimenting with a lot of code.
For example, if our notebook has cells like this:

```python
In [1]: a = 3
```

```python
In [2]: b = 4
```

```python
In [3]: a + b
7
```

If we change the value of `a`, nothing else changes until executed.

```python
In [4]: a = 12
```

```python
In [2]: b = 4
```

```python
In [3]: a + b
7
```

If we then use the new value further on down in the notebook, it can start to cause confusion.

```python
In [4]: a = 3
```

```python
In [2]: b = 4
```

```python
In [3]: a + b
7
```

```python
In [5]: a + b
16
```

In order for that change to propagate through the rest of your code and get numbering in sequential order, you'll need to re-run your notebook.
To do this without quitting out, you'll want to select `Restart and Run All` from the `Kernel` dropdown menu.

Because these notebooks were modeled after how scientists write and think in their own lab books, you have the option of being able to write text and/or Markdown in cells amongst your code.

This is accomplished via the dropdown menu at the top currently entitled `Code`.
Select a cell, click on that menu, and change the cell's format to `Markdown`.
Then you can write code in Markdown as you please, and render that Markdown when you execute the cell.
This is handy for writing down thoughts as you try out code, or creating sections in your code with various headings.
We'll be using it to write whatever we want!

Glossing over it here, but be sure to check out the notebook keystrokes in the `Help` dropdown menu.
Keystrokes will make your notebooking life so much easier, with commands allowing you to do things like create/delete cells on the fly.
