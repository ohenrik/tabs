# Tabs

Tabs is a small framework for defining and loading tables in a consistent way.
The goal is to make data science projects more maintainable by
improving code readability.

Tabs comes with support for caching processed tables based on the current
configuration resulting in shorter loading of tables that have already been
compiled once.

Read full documentation here: http://tabs.readthedocs.io/en/latest/index.html


## Basic concepts

Tabs consists of two main classes.
  * Tabs
  * Table

[But the usage section of the documentation provides a better introduction
to these classes.](http://tabs.readthedocs.io/en/latest/quick_start.html)

### Table


Table is an abstract class used to define new tables. This ensures that all
tables has a minimum of shared functionality, like fetching a table or
describing it.

### Tabs

Tabs is the class used to load all tables defined in a package. This is the
class used for loading tables and gaining an overview of all tables defined in a
package.
