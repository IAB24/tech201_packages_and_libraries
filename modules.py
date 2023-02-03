# Modules

#software that delivers some sort of functionality. eg reptile class in snake

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
