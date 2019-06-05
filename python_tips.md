# Python Language - Tips & Tricks

Python is an interpreted, high level, general purpose programming language which was initially designed by Guido van Rossum in 1991. Python has evolved over the years and is one of the top 5 popular programming languages as of May 2019, as per [TIOBE index][6].  Code readability, simplified syntax, compatibility with many operating systems, robust libraries makes the language widely used for creating a great applications.

While Python is widely used nowadays, it's also better to know a language in terms of it's disadvantages as well. No language is perfect, some are better than others. 

## Weak spots of Python

1. Python is not a preferred language for mobile computing. The language is also not present in web development browsers. Python is hard to secure, and that's why it is not in browsers. Source: [Medium Article][7]

2. Susceptible to run time errors, since Python is dynamically typed language; it only translates and type-checks code it's executing on.  A programming language is said to be dynamically typed, or just 'dynamic', when the majority of its type checking is performed at run-time as opposed to at compile-time.

   > **Interpreted:** Code translated into machine language instructions on the fly, during execution
   >
   > **Typing:** This is process when data types are checked. Two categories:
   >
   > - **Static:** Data types checked before run time
   >
   > - **Dynamic:** Data types are checked on the fly, during execution

   ```python
def dynamic(a):
    if a > 0:
        print('Am dynamically typed')
     else:
        print("3"+5)
dynamic(2) # Calling function and passing value 2.
   ```


The above snippet demonstrates the weak side of dynamically typed languages. When the `dynamic` function is called with a value of `2`, as in the given example, the else section is not executed, and therefore not checked. Only when the value passed to the `dynamic` function is less than 1, in this example, the `else` block is executed and will raise an error as below:

   ```python
def dynamic(a):
    if a > 0:
        print('Am dynamically typed')
    else:
        print("3"+5)
dynamic(-1) # Calling function and passing value 2.
   
>>> python .\static_dynamic_typed.py
Traceback (most recent call last):
File ".\static_dynamic_typed.py", line 6, in <module>
  dynamic(-1) # Calling function and passing value 2
File ".\static_dynamic_typed.py", line 5, in dynamic
  print("3"+5)
   ```

   Making it simple, the type checking does not happen in Python until the line never executes.

3. Does not have access modifiers or by default all the variables and member functions of a class are `public` in Python. It is allowed to to access an instance variable from outside. Python uses single underscore prefix for a variable to denote a private method. It does not change the access privilege as in languages like JAVA or C#

4. Speed limitations because Python code is executed line by line. But when python is interpreted, it often results in slow execution than other popular languages.

5. Simplicity of Python programming language syntax makes programmer more of a Python person, because of which sometimes shifting to a new language will be harder

Having canvassed about the fine points and weak spots of Python, it's time to be thick with the language.

##  Python Bytes

Python is a programming language as well as scripting language. Some of the features of Python are listed below:

1. Object Oriented
2. Free ( Open Source)
3. Portable

> Quick Note: Python implementation consists of an interpreter. However, some Python implementations, do consist of just-in-time compiler that will compile Python byte code into native machine code.
> Source: [article][8]

Source code is translated into byte code, which is then run by a Python virtual machine. The code is automatically compiled, but then interpreted.

There are two major versions of Python : 2.x and 3.x. Both are quite different. The samples shown in this article are using 3.x version of Python.  3.x is non-backward compatible version of Python and hence it is recommended to use 3.x version of Python, when building a new application. Below is the most well known change between Python 2.x and 3.x:

```python
# Python 2.x syntax below:
>>> print 'Hello World'
# Python 3.x syntax below:
>>> print('Hello World')
```
> `print` is a statement in Python 2.x
>
> `print` is a function in Python 3.x

This article would discuss some of the useful stubs while working with Python language. It's assumed that readers have basic knowledge of programming and Python language. This article is focusing on writing readable and cleaner code. It is part of a planned series of articles.

## Tips & Tricks

Some of the tips & tricks while using Python language are as below:

### Built - Ins

The Python language has a set of functions readily available for use. These functions are called as **built-in** functions. Let's look at some of the important built-in functions that will come handy.

1. #### dir() function:

   This function returns a list of valid attributes for the given object. This is a great function to determine the available attributes of an object.

   The syntax of dir() function is `dir([object])`. It takes only one argument.

   ```python
   >>> x = 10
   >>> dir(x)
   ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
   >>> x.bit_length()
   4
   ```

   In the above window, for an integer value assigned to `x`, we get a list of methods that can be used for numeric operations. The output of the code below shows, for a string value assigned to `y`, we get a list of methods that can be used for string operations.

   ```python
   >>> y = 'Hello World'
   >>> dir(y)
   ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
   >>> y.upper()
   'HELLO WORLD'
   ```

2. #### type() function:

   This function returns the type of an object.

   Syntax: `type(object)`

	```python
	>>> type(x)
	<class 'int'>
	>>> type(y)
	<class 'str'>
	```

​	It's a useful function, if we want to process only specific type of elements.

3. ####  help() function:

   This function is used to get the documentation of specified module, class, functions. This method is generally used with Python interpreter console.

   Syntax: `help([object])`

   ```python
   >>> help()

   Welcome to Python 3.7's help utility!

   If this is your first time using Python, you should definitely check out
   the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

   Enter the name of any module, keyword, or topic to get help on writing
   Python programs and using Python modules.  To quit this help utility and
   return to the interpreter, just type "quit".

   To get a list of available modules, keywords, symbols, or topics, type
   "modules", "keywords", "symbols", or "topics".  Each module also comes
   with a one-line summary of what it does; to list the modules whose name
   or summary contain a given string such as "spam", type "modules spam".

   help>
   # Observe the prompt have changed from `>>>` to 'help>'

   help> keywords

   Here is a list of the Python keywords.  Enter any keyword to get more help.

   False               class               from                or
   None                continue            global              pass
   True                def                 if                  raise
   and                 del                 import              return
   as                  elif                in                  try
   assert              else                is                  while
   async               except              lambda              with
   await               finally             nonlocal            yield
   break               for                 not

   #type `quit` to come out of help window
   ```

   We can also get the help documentation directly from the Python console by passing parameter to **help()** function.

   ```python
   >>> help(print)
   Help on built-in function print in module builtins:

   print(...)
       print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

       Prints the values to a stream, or to sys.stdout by default.
       Optional keyword arguments:
       file:  a file-like object (stream); defaults to the current sys.stdout.
       sep:   string inserted between values, default a space.
       end:   string appended after the last value, default a newline.
       flush: whether to forcibly flush the stream.
   ```

### Opening and Closing files in Python

Python supports file handling and allow users to read and write to files , along with many other file operations. File handling in Python requires no importing of modules.

Syntax: `open('<name of file>','mode')`

```python
fileObj = open('test.txt') # Default open mode is read
fileObj.close() # Once you open the file, you have to close
```

It is really important to close the file, once the action on the file is completed. This makes that there no further problems like resource leaks and may cause the system to slow down and crash.

In Python, this can be brought to fruition using  **context managers**, which can automatically release resources after use. The sample code snippet is as below:

```python
with open('test.txt','r') as file:
    print(file.read())
```

In simple terms, Python calls  `__enter__ ` and `__exit__` methods to an object, which functions as context manager. These methods will be called by Python at the right time, during the resource management.

Different file opening modes are as follows:

| Mode | Comments                                          |
| ---- | ------------------------------------------------- |
| r    | Read mode, no write possible                      |
| w    | Write mode, Truncate the contents of the file     |
| a    | Append only, no overwriting, no read              |
| r+   | Read and write, retain the content                |
| w+   | Write and read, Truncate the contents of the file |
| a+   | Append and read, does not overwrite               |
| rw   | Read and Write, will not create a file            |



1. #### seek() and tell() function:

   When file is opened for reading in Python, the file handle points to the beginning of the file. As we read the first line the pointer always points to the place where we ended the reading and the next read will start from there.

   This happens unless we tell the file handler to move.

   The `tell()` function will return the current location of the pointer and the `seek()` function will move the pointer.

   Syntax: `seek(offset,whence)`

   **Offset** :  Can take negative, 0 or positive values. A positive offset will move the file pointer forward, a negative offset will move the file pointer backward.

   **Whence**: This argument is optional and takes the below values:

    	1. 0 (default ): Beginning of file
    	2. 1 : Current file position
    	3. 2 : End of file

   Syntax: `tell()`

   ```python
   fileobj = open('test.txt')
   x = fileobj.tell()  
   print(fileobj.tell())
   line = fileobj.readline()
   while line:
     print(line)
     #print(fileobj.seek(x))
     fileobj.seek(x)
     print(fileobj.readline())
     #print(line)
     x = fileobj.tell()  
     print(fileobj.tell())
     line = fileobj.readline()
   fileobj.close()
   ```



   The above code snippet reads a file and uses `tell()` and `seek()` functions to play around with file handler positions. The program is hosted in an open source editor to experiment with saved as [main.py][1].

#### Ternary Conditional Operators

These are operators that evaluate something based on a condition being true or false. This simply allows to test a condition in **single line** replacing the multiline if-else statement making code short and readable.

Syntax: `[on_true] if [expression] else [on_false] `

Let's look at a sample code snippet with if-else condition:

```python
a,b = 10, 20
if a < b:
    min = a
else:
    min = b
print(min)
# this would return the output of 10
```
The above code can be written in a single line as below:

```python
a,b = 10, 20
min = a if a < b else b
print(min)
# this would return the output of 10
```

#### Enumerate() Function

This function is used to iterate through a list while keep tracking of the items' indices.  Usually the code to print the indices of the items in the list is as below:

```python
pets = ('Dogs', 'Cats', 'Turtles', 'Rabbits')
index = 0
for pet in pets:
    print(index,pet)
    index += 1
# the output is as follows:
0 Dogs
1 Cats
2 Turtles
3 Rabbits    
```

The above code can be re-written with `enumerate` function as follows:

```python
pets = ('Dogs', 'Cats', 'Turtles', 'Rabbits')
for i, pet in enumerate(pets):
	print (i, pet)
# the output is as follows:
0 Dogs
1 Cats
2 Turtles
3 Rabbits
```

The output not only print out contents of the tuple, but also their index orders. You can also pass in a start value, if you don't want to start the index from 0.

#### zip() function

This function take in a pair of streams and gives a pair of streams.  It stops when the shortest sequence is exhausted. Like a Ziploc in the real world `zip()` function acts as a container to hold values. It evaluates from left to right.

The following code snippet gives more information on `zip()` function:

```python
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
for num,alpha in zip(numbers,letters):
    print('{} number is related to {}'.format(num,alpha))
# the output is as follows
1 number is related to a
2 number is related to b
3 number is related to c
4 number is related to d
5 number is related to e
```

#### Single underscore "_" variable

Sometime "_" ( single underscore ) is used as a variable name in Python. This denotes it's a throwaway variable and will not be used in the Python programs. It is mainly used to ignore a value when unpacking.

```python
a, _ = (1,2)
#Tuple unpacking
print(a)
# the output will be
1
```

In the above case, if the values are unpacked in the form of  `a, b = (1, 2) ` and variable `b` is never used in the program, some IDE's will complain with an information message `Variable declared, but not used` . Declaring a single underscore variable solves this issue.

"_" ( single underscore ) is also used after a variable name, this is to avoid conflict between a Python keyword and variable we use.

Different scenarios of unpacking values are as follow:

```python
# Too many values to unpack
>>> a, b = (1,2,3,4,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

In the above case we have two options:

1. Assign first two values to a and b and rest to c as below:

   ```python
   >>> a, b, *c = (1,2,3,4,5)
   >>> print(a)
   1
   >>> print(b)
   2
   >>> print(c)
   [3, 4, 5]
   ```

2. Ignore the rest of the values using single underscore:

   ```python
   >>> a, b, *_ = (1,2,3,4,5)
   >>> print(a)
   1
   >>> print(b)
   2
   ```

3. Saving the first two values in `a` and `b`, rest of the values up to the last one in `c` and the last value in `d`

   ```python
   >>> a, b, *c, d = (1,2,3,4,5)
   >>> print(a)
   1
   >>> print(b)
   2
   >>> print(c)
   [3, 4, 5]
   >>> print(d)
   5
   # ignore the rest of the values up to `d`
   >>> a, b, *_, d = (1,2,3,4,5)
   ```

## Conclusion

Though there are lot of life hacks, when using Python programming this article tried to cover some of them. More information on these great life hacks can be accessed at below sites:

1. [Real Python][2]
2. [10 Python tips and tricks][3]

Use the below sites for trying out Python code samples online:

1. [Repl it][4]
2. [Katacoda Python Playground][5]

[ 1 ]: <https://midnightbluespottedprofessionals.suniljacob.repl.run/>
[ 2 ]: <https://realpython.com/>
[ 3 ]: https://www.youtube.com/watch?v=C-gEQdGVXbk&feature=youtu.be
[ 4 ]: https://repl.it
[ 5 ]: <https://www.katacoda.com/courses/python/playground>
[ 6 ]: <https://www.tiobe.com/tiobe-index/>

[ 7 ]: <https://medium.com/@mindfiresolutions.usa/advantages-and-disadvantages-of-python-programming-language-fd0b394f2121>

[ 8 ]: <https://www.quora.com/Is-Python-compiled-or-interpreted-or-both>

