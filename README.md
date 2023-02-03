# tech201_packages_and_libraries
tech201_packages_and_libraries

## Packages and libraries

### Packages and pip
- Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names. 
- pip is python's packet manager and installer


````python
- Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.

import requests

request_bbc = requests.get("https://www.bbc.co.uk") #get data from a url

print(request_bbc.status_code)
print(request_bbc.content)

# packages structure programs so that they can be reused by other programs
````

### Modules

- This is a software that delivers some sort of functionality for example the reptile class for a snake.
- A module’s contents are accessed the same way in all three cases: with the import statement.
- All you need to do is create a file that contains legitimate Python code and then give the file a name with a .py extension.
````python

import os # operating system dependent
import math,datetime,sys

working_directory = os.getcwd()
print(working_directory)

# module is referencing file, library = multiple files and folders

#modules used for scripting - important in DevOps

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today())

print((sys.path))

print(math.remainder(1, 5))

# When building a program it's really important to think whether you need to make a class/object or simply a function. You may not even need to make a dunction yourself, if there is a module that has what you are looking for already.

# Built in functions
# https://docs.python.org/3/library/functions.html
````
### Libraries
A library is an umbrella term referring to a reusable chunk of code. Usually, a Python library contains a collection of related modules and packages. Actually, this term is often used interchangeably with “Python package” because packages can also contain modules and other packages (subpackages). However, it is often assumed that while a package is a collection of modules, a library is a collection of packages.

````python
Python Libraries
import random
from random import random
import math

print(random.random())
print(random())

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
````