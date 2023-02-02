# Sumário

1. [Basic Syntax](#basic-syntax)  
    1.1 [The Python Command Line](#11-the-python-command-line)
2. [Python Indentation](#2-python-indentation)
3. [Python Variables](#3-python-variables)  
    3.1. [Creating variables](#31-creating-variables)  
    3.2. [Casting](#32-casting)  
    3.3. [Multi Words Variable Names](#33-multi-words-variable-names)  
    3.4. [Many Values to Multiple Variables](#34-many-values-to-multiple-variables)  
    3.5. [One Value to Multiple Variables](#35-one-value-to-multiple-variables)  
    3.6. [Unpack a Collection](#36-unpack-a-collection)  
    3.7. [The global Keyword](#37-the-global-keyword)  
4.  [Comments](#4-comments)  
5.  [Built-in Data Types](#5-built-in-data-types)  
    5.1. [Get the Type](#51-get-the-type)  
    5.2. [Python numbers](#52-python-numbers)  
        5.2.1.  [Int](#521-int)  
        5.2.2.  [float](#522-float)  
        5.2.3.  [complex](#523-complex)  
    5.3.  [Type Conversion](#53-type-conversion)  

---

## 1. Basic Syntax

Python Syntax compared to other programming languages:
- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

```python
    print("Hello, World!")
```

[🔗🏆 learnxinyminutes](https://learnxinyminutes.com/docs/python/)


### 1.1. The Python Command Line

Type the following on command line:
```bash
    python3
```

From there you can write any python, I like this one:
```bash
    >>> import this
``` 

Producing a nice response:
```
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
```

Whenever you are done in the python command line, you can simply type:

```
    >>> exit()
```

### 2. Python Indentation

Python uses indentation to indicate a block of code.
```python
    if 5 > 2:
        print("Five is greater than two!")
```

### 3. Python Variables

In Python, variables are created when you assign a value to it.
Python has no command for declaring a variable.

```python
    x = 5
    y = "Hello, World!"
```

#### 3.1. Creating variables

Python han no commmand for declaring a variable.
Variables do not need to be declared with any particular type, and can even change type after they have been set.

Variable names are case-sensitive.

```python
    x = 4       # x is of type int
    x = "Sally" # x is now of type str
```

String variables can be declared either by using single or double quotes.

#### 3.2. Casting

If you want to specify the data type of a variable, this can be done with casting.
```python
    x = str(3)      # x will be '3'
    y = int(3)      # y will be 3
    z = float(3)    # z will be 3.0 
```

#### 3.3. Multi Words Variable Names

Python prefer Snake Case:
```python
    my_variable_name = "Jhon"
```

#### 3.4. Many Values to Multiple Variables

```python
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)    # Orange
    print(y)    # Banana
    print(z)    # Cherry
``` 

#### 3.5. One Value to Multiple Variables

```python
    x = y = z = "Orange"
    print(x)    # Orange
    print(y)    # Orange
    print(z)    # Orange
```

#### 3.6. Unpack a Collection

```python
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x, y, z)    # apple banana cherry
```

### 3.7.  The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
```python
    def myfunc():
        global x
        x = "fantastic"
    myfunc()
    print("Python is " + x) # Python is fantastic
```

Also, use the global keyword if you want to change a global variable inside a function.
```python
    x = "awasome"    
    def myfunc():
        global x
        x = "fantastic"
    myfunc()
    print("Python is " + x) # Python is fantastic
```

### 4. Comments

```python
    # This is a line comment
    """
    This is a comment
    written in 
    more than just one line
    """
```

### 5. Built-in Data Types

| | |
|-|-|
|Text Type|```str```|
|Numeric Types|```int```, ```float```, ```complex```|
|Sequence Types|```list```, ```tuple```, ```range```|
|Mapping Type|```dict```|
|Set Types|```set```, ```frozenset```|
|Boolean Type|```bool```|
|Binary Types|```bytes```, ```bytearray```, ```memoryview```|
|None Type|```NoneType```|

#### 5.1. Get the Type

Use ```type()``` function.
```python
    x = 5
    y = "Jhon"
    print(type(x))  # <class 'in'>
    print(type(y))  # <class 'str'>
```

#### 5.2.  Python numbers

There are three numeric types in Python: ```int```, ```float```, ```complex```
```python
    x = 1   # int
    y = 2.8 # float
    z = 1j  # complex
```

##### 5.2.1. Int

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
```python
    x = 1
    y = 35656222554887711
    z = -3255522

    print(type(x))  # <class 'int'>
    print(type(y))  # <class 'int'>
    print(type(z))  # <class 'int'>
```

##### 5.2.2. float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

```python
    x = 1.10
    y = 1.0
    z = -35.59
```

Float can also be scientific numbers with an "e" to indicate the power of 10.

```python
    x = 35e3
    y = 12E4
    z = -87.7e100

    print(type(x))  # <class 'float'>
    print(type(y))  # <class 'float'>
    print(type(z))  # <class 'float'>
```

##### 5.2.3. complex

Complex numbers are written with a "j" as the imaginary part:

```python
    x = 3+5j
    y = 5j
    z = -5j

    print(type(x))  # <class 'complex'>
    print(type(y))  # <class 'complex'>
    print(type(z))  # <class 'complex'>
```

#### 5.3. Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods:

```python
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

    #convert from int to float:
    a = float(x)

    #convert from float to int:
    b = int(y)

    #convert from int to complex:
    c = complex(x)

    print(a)    # 1.0
    print(b)    # 2
    print(c)    # (1+0j)

    print(type(a))  # <class 'float'>
    print(type(b))  # <class 'int'>
    print(type(c))  # <class 'complex'>
```





