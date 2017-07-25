import os
import tempfile
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
    """Class for testing table loader"""
    def input(self):
        input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  'data',
                                  'test_table_one.csv')
        dtype = {
            'first': np.str,
            'last': np.str,
            # 'birthday': np.str
            'age': np.int
        }

        converters = {
            'birthday': pd.to_datetime,
        }

        return pd.read_csv(input_file, dtype=dtype, converters=converters)

    def output(self):
        output_path = os.path.join(tempfile.mkdtemp(),
                                   self.get_cached_filename('test_table_one', 'pkl')
                                  )
        return output_path

    @property
    def post_processors(self):
        return [
            drop_age_column,
            calculate_new_age
        ]

class TestTableTwo(Table):
    """Class for testing tables loader"""
    def input(self):
        input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  'data',
                                  'test_table_one.csv')
        dtype = {
            'first': np.str,
            'last': np.str,
            # 'birthday': np.str
            'age': np.int
        }

        converters = {
            'birthday': pd.to_datetime,
        }

        return pd.read_csv(input_file, dtype=dtype, converters=converters)

    def output(self):
        output_path = os.path.join(tempfile.mkdtemp(),
                                   'output',
                                   self.get_cached_filename('test_table_one', 'pkl')
                                  )
        return output_path

    @property
    def post_processors(self):
        return list()
