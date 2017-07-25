# pylint: disable=C0111,C0103
import os
import pytest
from tabs import Tabs

def test_tabs_finds_test_table_one():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tabs = Tabs(package_path)
    assert 'TestTableOne' in tabs.tabs

def test_tabs_finds_test_table_two():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tabs = Tabs(package_path)
    assert 'TestTableTwo' in tabs.tabs

def test_tabs_finds_two_tables():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tabs = Tabs(package_path)
    assert len(tabs.tabs) == 2


def test_table_one_has_description():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tabs = Tabs(package_path)
    result = tabs('TestTableOne').describe(full=True)
    assert result == [
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
        ''
    ]

def test_tabs_loads_test_table_one():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tables = Tabs(package_path)
    assert len(tables('TestTableOne').fetch()) == 100

def test_tabs_iter_returns_a_list_of_table_names():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tabs = Tabs(package_path)
    assert 'TestTableOne' in list(tabs)

def test_throws_assert_error_if_table_name_not_found():
    package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'fixtures')
    tabs = Tabs(package_path)
    with pytest.raises(AssertionError) as excinfo:
        tabs('TestTableShouldNotExist')
    assert excinfo.match(r'Table not avaiable\. Avaiable tables: .*')
