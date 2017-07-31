# pylint: disable=C0111,C0103
from tests.fixtures import example_table

def test_table_dependencies():
    assert example_table.TestTableOne in example_table.TestTableTwo.dependencies()

def test_table_dep_alias():
    assert example_table.TestTableOne in example_table.TestTableTwo.dep()

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
