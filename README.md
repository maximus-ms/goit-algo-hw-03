# GoITNeo Algo HW-3

## Task 1: Copy and sort files
Write a Python program that recursively copies files in the source directory, moves them to a new directory, and sorts them into subdirectories based on their file extensions.

### Solution
File FilesSortAndCopy.py

### Usage

 - Run the demo script
``` python
python FilesSortAndCopy.py <source_dir> [<destination_dir>]
```

 - Use as a module
```python
import FilesSortAndCopy

src  = "/any/src/dir"
dest = "/any/dest/dir"

# Sort and copy in constructor
FilesSortAndCopy(src, dest)

# Create an object, set src and dist (optional) and do sort_and_copy
files_sort_and_copy = FilesSortAndCopy()
files_sort_and_copy.src = src
files_sort_and_copy.dest = dest+"_set"
files_sort_and_copy()

# Can be called many times for different src or/and dest
files_sort_and_copy(dest=dest+"_call_1")
files_sort_and_copy(dest=dest+"_call_2")
```

### Additional info
 - If a file doesn't have an ending, it will be copied to dest+"/no_ending" dir.
 - A dot (".") at the beginning of the file name is part of the name but not an ending indicator.
 - The default destination path is '**<source_dir>/../dest**'


## Task 2: Koch snowflake
Write a Python program that uses recursion to generate a Koch snowflake fractal, with the condition that the user should be able to specify the recursion level.

### Solution
File KochSnowflake.py

### Usage
 - Run the demo script
```python
python KochSnowflake.py [<n> <size>]
```
 - Use as a module
```python
from KochSnowflake import koch_snowflake

window = turtle.Screen()

fraction_n = 4
length = 300
funny = True

koch_snowflake(n=fraction_n, l=length, funny=funny)

window.mainloop()
```
### Additional info
 - Function koch_snowflake has an extra parameter "funny:bool=False", it will add more drawing for a snowflake if enabled.
