<h1 align='center'>
Algorithmic Complexity
</h1>

#### Task 1.

Build an application that looks at how fast some standard library functions run.
 - ``last``, ``reverse``, ``shuffle``, ``sort``.
> if you are generating an array from a range, don't forget to shuffle it first to not bias the results
 
- Create some code that returns the time needed to execute a function. 
- What if you make the array passed into the functions 10, 100, 1000, 10000 times bigger?
- In order to get further, we'll need to create graphs to compare different pieces of code. You will transform your code into a timing framework. It should:

- Create arrays of different sizes (try 5000 to 100000 in steps of 5000)
- Run the code to time on each
- Print the size and corresponding time.
- From there, you should use a spreadsheet utility to plot the results into a curve (time spent over input size).
- For more pointers on how to time code, here's a more detailed document. It also addresses a few of the the common problems you may experience.

<h1 align='center'>
How To Run Algorithim.
</h1>

- ``fork`` and ``clone`` this repo.
- You mignt need to create a ``virtual env``. [Look Here](https://virtualenv.pypa.io/en/latest/userguide/).
- pip install ``pytest``.
- cd into ``app``.
- To run test type ``pytest``.

```python

def build_list_of_size(self, list_size):
        if type(list_size) is str: return []

        built_list_size = []
        for i in range(1, list_size):
            built_list_size.append(i)
        return built_list_size
```

This method takes a ``list_size`` which is basically an ``integer`` and generates an list that has a size of the ``integer``.

```python
  def cal_time(self, a_list, algorithm):
        start_time = datetime.now()
        algorithm(a_list)
        return(datetime.now() - start_time)
```

The cal_time method takes a ``list of numbers``, ``[2,3,4,5,7]``, an algorithm and then run the algorithm on that method. After running the algorithm on the method it returns the ``time`` it took to run the algorithm.

Currently, I have only found ``two`` in built methods for python that meets the specifications. ``reverse`` and ``sort``. For this reason, I have only created two methods for the ``Algorithm class``.

```python
    def do_reverse(self, list_input):
        list_input.reverse()

    def do_sort(self, list_input):
        list_input.sort()
```

<h1 align='center'>
Challenges.
</h1>

- Testing with Pytest has been a ``struggle`` so far. I still need a bit of time with it to fully understand how it operates.
- Learning how to ``mock`` and ``stub`` objects using pytest has been a challenge.
- Pytest can't seem to find my ``app`` path. This is the error that i get.

<img width="1277" alt="Screen Shot 2019-06-07 at 15 31 26" src="https://user-images.githubusercontent.com/37377831/59111716-817b6680-8939-11e9-808b-69ef00bc6e23.png">

> After a bit of research and talking to to ``Mike`` a coach at Makers, we came to a conclusion that it had something to to with the path. when this line, ``from algorithms import Algorithms`` is changed to ``from lib.algorithms import Algorithms`` pytest worked fine but currently it is not.



