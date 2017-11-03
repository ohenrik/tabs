# pylint: disable=C0111,C0103
import inspect
from tests.fixtures import example_table

def test_table_dependencies():
    assert example_table.TestTableOne == example_table.TestTableTwo.dependencies()[0].__class__

def test_table_dep_alias():
    assert example_table.TestTableOne == example_table.TestTableTwo.dep()[0].__class__

def test_table_dependencies_without_any_dep():
    assert example_table.TestTableOne.dependencies() == list()

def test_table_dependencies_length():
    assert len(example_table.TestTableTwo().dependencies()) == 2

def test_table_dep_alias_length():
    assert len(example_table.TestTableTwo().dep()) == 2

def test_table_one_prints_description(capfd):
    example_table.TestTableOne.describe()
    out, _ = capfd.readouterr()
    result = "\n".join([
        '================================================================================',
        'TestTableOne:',
        'Class for testing table loader',
        '================================================================================',
        '',
        ''
    ])
    assert result == out

def test_table_one_prints_full_description(capfd):
    result = example_table.TestTableOne.describe(full=True)
    out, _ = capfd.readouterr()
    result = "\n".join([
        '================================================================================',
        'TestTableOne:',
        'Class for testing table loader',
        '--------------------------------------------------------------------------------',
        'Post processors:',
        '--------------------------------------------------------------------------------',
        '>   drop_age_column:',
        '    Drops age from original dataframe because of wrong age ',
        '',
        '>   calculate_new_age:',
        '    Calculates new age and adds it to the dataframe',
        '',
        '================================================================================',
        '',
        ''
    ])
    assert result == out

def test_table_has_unique_hashe():
    hash_string = example_table.TestTableOne().get_hash()
    assert hash_string == 'bc938c008d11d31332c01879173b329a'

def test_table_two_has_unique_hash_dependent_on_kwargs():
    abc_hash = example_table.TestTableTwo(test_kwarg='abc').get_hash()
    bca_hash = example_table.TestTableTwo(test_kwarg='bca').get_hash()
    assert abc_hash == '93604166a6c1227e09eea06742e1e789'
    assert bca_hash == '2c13f87c74bf8e382e6c88dc0d18a09f'
