---
title: "Introducing Databases and SQL"
teaching: 60
exercises: 5
questions:
- "What is a relational database and why should I use it?"
- "What is SQL?"
objectives:
- "Describe why relational databases are useful."
- "Create and populate a database from a text file."
- "Define SQLite data types."
keypoints:
- "SQL allows us to select and group subsets of data, do math and other calculations, and combine data."
- "A relational database is made up of tables which are related to each other by shared keys."
- "Different database management systems (DBMS) use slightly different vocabulary, but they are all based on the same ideas."
---


## Setup-C

_Note: this should have been done by participants before the start of the workshop._

We use [DB Browser for SQLite](http://sqlitebrowser.org/) and the
[Portal Project dataset](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459)
throughout this lesson. See [Setup](../setup.html) for
instructions on how to download the data, and also how to install DB Browser for SQLite.

# Motivation

To start, let's orient ourselves in our project workflow.  Previously,
we used Excel and OpenRefine to go from messy, human created data
to cleaned, computer-readable data.  Now we're going to move to the next piece
of the data workflow, using the computer to read in our data, and then
use it for analysis and visualization.

## What is SQL?

SQL stands for Structured Query Language. SQL allows us to interact with relational databases through queries.
These queries can allow you to perform a number of actions such as: insert, select, update and delete information in a database.


## Dataset Description

The data we will be using contains historical world cup information from 1930 to 2018. This is a real and complete dataset that includes dates and times of matches, countries that were playing, winners, losers, winning conditions, players, attendance, referees, assistants, etc.,  as well as the player data for each match played in the world cup (minute in which the player scored, got substituted, got a yellow or a red card, etc.)

## Questions

Let's look at some of the cleaned spreadsheets you downloaded during [Setup](../setup.html) to complete this challenge. You'll need the following two files:

* `matches.csv`
* `players.csv`

> ## Challenge
>
> Open each of these csv files and explore them.
> What information is contained in each file?  Specifically, if I had
> the following research questions:
>
> * Does players height affect their performance during the games?
> * Does the attendance number affect the outcome of the host countrly?
> * What information can I learn about WorldCup outcomes from 1930, over time?
>
> What would I need to answer these questions?  Which files have the data I need? What
> operations would I need to perform if I were doing these analyses by hand?
{: .challenge}

## Goals

In order to answer the questions described above, we'll need to do the
following basic data operations:

* select subsets of the data (rows and columns)
* group subsets of data
* do math and other calculations
* combine data across spreadsheets

In addition, we don't want to do this manually!  Instead of searching
for the right pieces of data ourselves, or clicking between spreadsheets,
or manually sorting columns, we want to make the computer do the work.

In particular, we want to use a tool where it's easy to repeat our analysis
in case our data changes. We also want to do all this searching without
actually modifying our source data.

Putting our data into a relational database and using SQL will help us achieve these goals.

> ## Definition: *Relational Database*
>
> A relational database stores data in *relations* made up of *records* with *fields*.
> The relations are usually represented as *tables*;
> each record is usually shown as a row, and the fields as columns.
> In most cases, each record will have a unique identifier, called a *key*,
> which is stored as one of its fields.
> Records may also contain keys that refer to records in other tables,
> which enables us to combine information from two or more sources.
{: .callout}

# Databases-D

## Why use relational databases

Using a relational database serves several purposes.

* It keeps your data separate from your analysis.
    * This means there's no risk of accidentally changing data when you analyze it.
    * If we get new data we can rerun the query.
* It's fast, even for large amounts of data.
* It improves quality control of data entry (type constraints and use of forms in MS Access, Filemaker, Oracle Application Express etc.)
* The concepts of relational database querying are core to understanding how to do similar things using programming languages such as R or Python.

## Database Management Systems

There are different database management systems to work with relational databases
such as SQLite, MySQL, Potsgresql, MSSQL Server, and many more. Each of them differ
mainly based on their scalability, but they all share the same core principles of
relational databases. In this lesson, we use SQLite to introduce you to SQL and
data retrieval from a relational database.

## Relational databases

You can see the tables in the database by looking at the left hand side of the
screen under Database Structure tab. Here you will see a list under "Tables." Each item listed here corresponds to one of the `csv` files
we were exploring earlier. To see the contents of any table, click on it, and
then click the “Browse Data” tab next to the "Database Structure" tab. This will
give us a view that we're used to - a copy of the table. Hopefully this
helps to show that a database is, in some sense, just a collection of tables,
where there's some value in the tables that allows them to be connected to each
other (the "related" part of "relational database").

The "Database Structure" tab also provides some metadata about each table. If you click on the down arrow next to a table name, you will see information about the columns, which in databases are referred to as "fields," and their assigned data types.
(The rows of a database table
are called *records*.) Each field contains
one variety or type of data, often numbers or text. You can see in the
`players` table that most fields contain numbers (INT) while the `matches`
table is entirely made up of text fields.

The "Execute SQL" tab is blank now - this is where we'll be typing our queries
to retrieve information from the database tables.

To summarize:

* Relational databases store data in tables with fields (columns) and records
  (rows)
* Data in tables has types, and all values in a field have
  the same type ([list of data types](#datatypes))
* Queries let us look up data or make calculations based on columns

## Database Design

* Every row-column combination contains a single *atomic* value, i.e., not
   containing parts we might want to work with separately.
* One field per type of information
* No redundant information
    * Split into separate tables with one table per class of information
    * Needs an identifier in common between tables – shared column - to
       reconnect (known as a *foreign key*).

## Import-C

Before we get started with writing our own queries, we'll create our own
database.  We'll be creating this database from the two sv` files
we downloaded earlier.  To create a new database with the two csv files, we need to follow these stepps:

1. Start a New Database
    - Click the **New Database** button
    - Give a name and click Save to create the database in the opened folder
    - In the "Edit table definition" window that pops up, click cancel as we will be importing tables, not creating them from scratch
2. Select **File >> Import >> Table from CSV file...**
3. Choose `matches.csv` from the data folder we downloaded and click **Open**.
4. Give the table a name that matches the file name (`matches`), or use the default
5. If the first row has column headings, be sure to check the box next to "Column names in first line".
6. Be sure the field separator and quotation options are correct. If you're not sure which options are correct, test some of the options until the preview at the bottom of the window looks right.
7. Press **OK**, you should subsequently get a message that the table was imported.
9. Back on the Database Structure tab, you should now see the table listed. Right click on the table name and choose **Modify Table**, or click on the **Modify Table** button just under the tabs and above the table list.
10. Click **Save** if asked to save all pending changes.
11. In the center panel of the window that appears, set the data types for each field using the suggestions in the table below (this includes fields from the `plots` and `species` tables also):

| Field                | Data Type      | Motivation                                                                       | Table(s)          |
|----------------------|:---------------|----------------------------------------------------------------------------------|-------------------|
| Year                 | INTEGER        | Having data as numeric allows for meaningful arithmetic and comparisons          | matches           |
| Datetime             | TEXT           | Field contains text data                                                 	       | matches           |
| Stage                | TEXT           | Field contains text data                                                         | matches           |
| Stadium              | TEXT           | Field contains text data                                                         | matches           |
| City                 | TEXT           | Field contains text data	    					                                      	 | matches           |
| Home Team Name       | TEXT           | Field contains text data                                                       	 | matches           |
| Home Team Goals      | INTEGER        | Field contains numerical data 			                      	                     | matches           |
| Away Team Goals      | INTEGER        | Field contains numerical data                                                    | matches           |
| Away Team Name       | TEXT           | Field contains text data								                                         | matches           |
| Win conditions       | TEXT           | Field contains text data                                                 	       | matches           |
| Attendance           | INTEGER        | Field contains numerical data                         	                         | matches           |
| Half-time Home goals | INTEGER        | Field contains numerical data                                                    | matches           |
| Half-time Away Goals | INTEGER        | Field contains numerical data                                                    | matches           |
| Referee              | TEXT           | Field contains text data                                                         | matches           |
| Assisstant 1         | TEXT           | Field contains text data                                                         | matches           |
| Assisstant 2         | TEXT           | Field contains text data                                                         | matches           |
| RoundID              | INTEGER        | Field contains numerical data                                                    | matches, players  |
| MatchID              | INTEGER        | Field contains numerical data                                                    | matches, players  |
| Home Team Initials   | TEXT           | Field contains text data                                                         | matches           |
| Away Team Initials   | TEXT           | Field contains text data                                                         | matches           |



12. Finally, click **OK** one more time to confirm the operation. Then click the **Write Changes** button to save the database.


> ## Challenge
>
> - Import the `matches` and `players` tables
{: .challenge}

You can also use this same approach to append new fields to an existing table.

## Adding fields to existing tables

1. Go to the "Database Structure" tab, right click on the table you'd like to add data to, and choose **Modify Table**, or click on the **Modify Table** just under the tabs and above the table.
2. Click the **Add Field** button to add a new field and assign it a data type.


## <a name="datatypes"></a> Data types

| Data type                          | Description                                                                                              |
|------------------------------------|:---------------------------------------------------------------------------------------------------------|
| CHARACTER(n)                       | Character string. Fixed-length n                                                                         |
| VARCHAR(n) or CHARACTER VARYING(n) | Character string. Variable length. Maximum length n                                                      |
| BINARY(n)                          | Binary string. Fixed-length n                                                                            |
| BOOLEAN                            | Stores TRUE or FALSE values                                                                              |
| VARBINARY(n) or BINARY VARYING(n)  | Binary string. Variable length. Maximum length n                                                         |
| INTEGER(p)                         | Integer numerical (no decimal).                                                                          |
| SMALLINT                           | Integer numerical (no decimal).                                                                          |
| INTEGER                            | Integer numerical (no decimal).                                                                          |
| BIGINT                             | Integer numerical (no decimal).                                                                          |
| DECIMAL(p,s)                       | Exact numerical, precision p, scale s.                                                                   |
| NUMERIC(p,s)                       | Exact numerical, precision p, scale s. (Same as DECIMAL)                                                 |
| FLOAT(p)                           | Approximate numerical, mantissa precision p. A floating number in base 10 exponential notation.          |
| REAL                               | Approximate numerical                                                                                    |
| FLOAT                              | Approximate numerical                                                                                    |
| DOUBLE PRECISION                   | Approximate numerical                                                                                    |
| DATE                               | Stores year, month, and day values                                                                       |
| TIME                               | Stores hour, minute, and second values                                                                   |
| TIMESTAMP                          | Stores year, month, day, hour, minute, and second values                                                 |
| INTERVAL                           | Composed of a number of integer fields, representing a period of time, depending on the type of interval |
| ARRAY                              | A set-length and ordered collection of elements                                                          |
| MULTISET                           | A variable-length and unordered collection of elements                                                   |
| XML                                | Stores XML data                                                                                          |


## <a name="datatypediffs"></a> SQL Data Type Quick Reference

Different databases offer different choices for the data type definition.

The following table shows some of the common names of data types between the various database platforms:

| Data type                                               | Access                    | SQLServer            | Oracle             | MySQL          | PostgreSQL    |
|:--------------------------------------------------------|:--------------------------|:---------------------|:-------------------|:---------------|:--------------|
| boolean                                                 | Yes/No                    | Bit                  | Byte               | N/A            | Boolean       |
| integer                                                 | Number (integer)          | Int                  | Number             | Int / Integer  | Int / Integer |
| float                                                   | Number (single)           | Float / Real         | Number             | Float          | Numeric       |
| currency                                                | Currency                  | Money                | N/A                | N/A            | Money         |
| string (fixed)                                          | N/A                       | Char                 | Char               | Char           | Char          |
| string (variable)                                       | Text (<256) / Memo (65k+) | Varchar              | Varchar2 | Varchar        | Varchar       |
| binary object	OLE Object Memo	Binary (fixed up to 8K)   | Varbinary (<8K)           | Image (<2GB)	Long | Raw	Blob          | Text	Binary | Varbinary     |
