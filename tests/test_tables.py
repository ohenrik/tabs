# pylint: disable=C0111,C0103
from tests.fixtures import example_table

def test_table_dependencies():
    assert example_table.TestTableOne in example_table.TestTableTwo().dependencies()

def test_table_dependencies_length():
    assert len(example_table.TestTableTwo().dependencies()) == 2
