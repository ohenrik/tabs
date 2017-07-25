# tabs

Tabs is a small framework created for organizing loading and processing
tables.

It's built to be used with Pandas but could be used with any library for loading
and handling tables.

## Basic concepts

Tabs consists of two main classes. Tables and Table.

### Table

Table is an abstract class used to define new tables. This ensures that all
tables has a minimum of shared functionality, like fetching a table or
describing it.

### Tables

Tables is the class used to load all tables defined in a package. This is the
class used for loading tables and gaining an overview of all tables defined in a
package.

## Usage

Usage of tabs is best shown through an example. In the following example the
project has this folder structure:

```
csv_files/
  |- example_file_one.csv
  |- example_file_one.csv
output/
table_definition.py
table_usage.py
```

### Table
Defining a table:

```python
# in /table_definition.py

import os
from datetime import datetime
from tabs.loaders import Table
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np

def drop_age_column(table):
    """Drops age from original dataframe because of wrong age """
    table.drop('age', 1, inplace=True)
    return table

def calculate_new_age(table):
    """Calculates new age and adds it to the dataframe"""
    date_now = datetime.now()
    def get_age(birthday):
        if birthday:
            return relativedelta(date_now, birthday).years
    table['age'] = table.apply(lambda birthday: get_age)
    return table

class TestTableOne(Table):
    """Table containing names, birthday and age of participants"""
    def input(self):
        input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  'csv_files',
                                  'test_table_one.csv')
        dtype = {
            'first': np.str,
            'last': np.str,
            'age': np.int
        }

        converters = {
            'birthday': pd.to_datetime,
        }

        return pd.read_csv(input_file, dtype=dtype, converters=converters)

    def output(self):
        output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                   'output',
                                   self.get_cached_filename('test_table_one', 'pkl')
                                  )
        return output_path

    @property
    def post_processors(self):
        return [
            drop_age_column,
            calculate_new_age
        ]
```

Here you should first pay attention to the class `TestTableOne`. This inherits
from the abstract class `Table` that requires `input`, `output` and
`post_processors` to be defined.

`input` is used to define how the table is loaded before any post processors are
applied.

`output` specifies where the table is stored and if it utilizes the
`get_cached_filename` method that applies a hash id based on  the content of
`input`, `output` and `post_processors`. This ensures that if the table is
modified either through input, output or post processors, the table is
regenerated.

`post_processors` is an array of functions that takes the complete table as an
input and returns a modified table. This is where you instruct what changes you
apply to your table and in what order.

### Tables

The Tables class can be used to load tables and getting an overview of which
tables are defined and how they are processed.

```python
package_path = os.path.dirname(os.path.realpath(__file__))
tables = Tables(package_path)
table = tables('TestTableOne').fetch()

len(table) # >>>> 100
list(table) # >>>> ['first', 'last', 'birthday', 'age']
table.head() # table is a normal pandas table

tables.describe_all(full=True) # This will print a list of all defined tables and their post porcessors.
```

### Table and Tables - Utility methods

#### describe

Is either used directly on defined tables (i.e. TestTableOne) or through Tables
and will print out a description of the table based on the `__doc__` defined in
the class. If `full=True` is provided the post processors and their description
will also be included.

**Example with TestTableOne:**
`TestTableOne().describe(full=True)`

**Example through Tables:**
`Tables(package_path)('TestTableOne').describe(full=True)`

#### describe_all

Does the same as `describe` but for all defined tables. Only exists on Tables.

#### fetch

Is either used directly on defined tables (i.e. TestTableOne) or through Tables
and is used to fetch the pandas table from the a defined table.

**Example with TestTableOne:**
`TestTableOne().fetch()`

**Example through Tables:**
`Tables(package_path)('TestTableOne').fetch()`

#### get_cached_filename

Is used inside the `output` method to add a hash id after the output filename.

`self.get_cached_filename('test_table_one', 'pkl')` will return something
similar to `test_table_one_1341423423fds23.pkl` based on what configurations
you have applied.

**Exmaple:**

```python
def output(self):
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'output',
                               self.get_cached_filename('test_table_one', 'pkl')
                              )
    return output_path
```
