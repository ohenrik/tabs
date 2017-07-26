Basic concepts
==============

Tabs consists of two main classes.
  * Tabs
  * Table

Table
-----


Table is an abstract class used to define new tables. This ensures that all
tables has a minimum of shared functionality, like fetching a table or
describing it.

.. autoclass:: tabs.Table

Tabs
----

Tabs is the class used to load all tables defined in a package. This is the
class used for loading tables and gaining an overview of all tables defined in a
package.

.. autoclass:: tabs.Tabs
