---
title: "Accessing Data With Queries"
teaching: 30
exercises: 5
questions:
- "How do I write a basic query in SQL?"
objectives:
- "Write and build queries."
- "Filter data given various criteria."
- "Sort the results of a query."
keypoints:
- "It is useful to apply conventions when writing SQL queries to aid readability."
- "Use logical connectors such as AND or OR to create more complex queries."
- "Calculations using mathematical symbols can also be performed on SQL queries."
- "Adding comments in SQL helps keep complex queries understandable."
---

## Writing my first query

Let's start by using the **matches** table. Here we have data on every world cup game that was played from 1930 to 2014: the outcome of every game, goals at half time, host city, attendance, etc.

Let’s write an SQL query that selects all of the columns in the matches table. SQL queries can be written in the box located under the "Execute SQL" tab. Click on the right arrow above the query box to execute the query. (You can also use the keyboard shortcut "Cmd-Enter" on a Mac or "Ctrl-Enter" on a Windows machine to execute a query.) The results are displayed in the box below your query. If you want to display all of the columns in a table, use the wildcard *.

    SELECT *
    FROM matches;

We have capitalized the words SELECT and FROM because they are SQL keywords.
SQL is case insensitive, but it helps for readability, and is good style.

If we want to select a single column, we can type the column name instead of the wildcard *.

    SELECT year
    FROM matches;

If we want more information, we can add more columns to the list of fields,
right after SELECT:

    SELECT year, datetime, city
    FROM matches;

### Limiting results

Sometimes you don't want to see all the results, you just want to get a sense of what's being returned. In that case, you can use the `LIMIT` command. In particular, you would want to do this if you were working with large databases.

    SELECT *
    FROM matches
    LIMIT 10; 

### Unique values

If we want only the unique values so that we can quickly see what species have
been sampled we use `DISTINCT` 

    SELECT DISTINCT species_id
    FROM matches;

If we select more than one column, then the distinct pairs of values are
returned

    SELECT DISTINCT year, species_id
    FROM matches;

### Calculated values

We can also do calculations with the values in a query.
For example, if we wanted to look at the mass of each individual
on different dates, but we needed it in kg instead of g we would use

    SELECT year, month, day, weight/1000
    FROM matches;

When we run the query, the expression `weight / 1000` is evaluated for each
row and appended to that row, in a new column. If we used the `INTEGER` data type
for the weight field then integer division would have been done, to obtain the
correct results in that case divide by `1000.0`. Expressions can use any fields,
any arithmetic operators (`+`, `-`, `*`, and `/`) and a variety of built-in
functions. For example, we could round the values to make them easier to read.

    SELECT plot_id, species_id, sex, weight, ROUND(weight / 1000, 2)
    FROM matches;

> ## Challenge
>
> - Write a query that returns the Year, Datetime, Stage, Stadium, Home team name, Away team name and, MatchID
>
> > ## Solution
> > ~~~
> > SELECT Year, Datetime, Stage, Stadium, Home team name, Away team name and, MatchID
> > FROM matches;
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}

## Filtering

Databases can also filter data – selecting only the data meeting certain
criteria.  For example, let’s say we only want data for final games, which has "Final" as Stage name.  We need to add a
`WHERE` clause to our query:

    SELECT *
    FROM matches
    WHERE Stage='Final';

We can do the same thing with numbers.
Here, we only want the data since 1992:

    SELECT * FROM matches
    WHERE Year >= 1992;

If we used the `TEXT` data type for the year, the `WHERE` clause should
be `year >= '1992'`. 

We can use more sophisticated conditions by combining tests
with `AND` and `OR`.  For example, suppose we want the data on finals
starting in the year 1992:

    SELECT *
    FROM matches
    WHERE (year >= 1992) AND (Stage = 'Final');

Note that the parentheses are not needed, but again, they help with
readability.  They also ensure that the computer combines `AND` and `OR`
in the way that we intend.

If we wanted to get data for any of the Quarter-final, Semi-final and Final games, which have
Stage names `Quarter-finals`, `Semi-finals`, and `Final`, we could combine the tests using OR:

    SELECT *
    FROM matches
    WHERE (Stage = 'Quarter-finals') OR (Stage = 'Semi-finals') OR (Stage = 'Final');

> ## Challenge
>
> - Produce a table listing the data for all individuals in Plot 1 
> that had anattendance of more than 50000 people, telling us the date, MatchID, and Stadium. 
>
> > ## Solution
> > ~~~
> > SELECT Datetime, MatchID, Attendance
> > FROM matches
> > WHERE (plot_id = 1) AND (Attendance > 50000);
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}

## Building more complex queries

Now, let's combine the above queries to get data for the Quarter-finals, Semifinals and Final stages from
the year 1992 on.  This time, let’s use IN as one way to make the query easier
to understand.  It is equivalent to saying `WHERE (Stage = 'Quarter-finals') OR (Stage
= 'Semi-finals') OR (Stage = 'Final')`, but reads more neatly:

    SELECT *
    FROM matches
    WHERE (Attendance >= 50000) AND (Stage IN ('Quarter-finals', 'Semi-finals', 'Final'));

We started with something simple, then added more clauses one by one, testing
their effects as we went along.  For complex queries, this is a good strategy,
to make sure you are getting what you want.  Sometimes it might help to take a
subset of the data that you can easily see in a temporary database to practice
your queries on before working on a larger or more complicated database.

When the queries become more complex, it can be useful to add comments. In SQL,
comments are started by `--`, and end at the end of the line. For example, a
commented version of the above query can be written as:

    -- Get post 50000 data on Quarter-finals, Semifinals and Final stages
    -- These are in the matches table, and we are interested in all columns
    SELECT * FROM matches
    -- Sampling year is in the column `Attendance`, and we want to include 1992
    WHERE (Attendance >= 1992)
    -- Quarter-finals, Semi-finals and Final stages have the `Stage` names Quarter-finals, Semi-finals and Final
    AND (Stage IN ('Quarter-finals', 'Semi-finals', 'Final'));

Although SQL queries often read like plain English, it is *always* useful to add
comments; this is especially true of more complex queries.

## Sorting

We can also sort the results of our queries by using `ORDER BY`.
For simplicity, let’s go back to the **WorldCupPlayers** table and alphabetize it by taxa.

First, let's look at what's in the **WorldCupPlayers** table. It's a table of the RoundID and MatchID, names and players' information for every game. Having this in a separate table is nice, because we didn't need to include all
this information in our main **Matches** table.

    SELECT *
    FROM WorldCupPlayers;

Now let's order it by Player Name.

    SELECT *
    FROM WorldCupPlayers
    ORDER BY Player Name ASC;

The keyword `ASC` tells us to order it in ascending order.
We could alternately use `DESC` to get descending order.

    SELECT *
    FROM WorldCupPlayers
    ORDER BY Player Name DESC;

`ASC` is the default.

We can also sort on several fields at once.
To truly be alphabetical, we might want to order by MatchID then Team Initials.

    SELECT *
    FROM WorldCupPlayers
    ORDER BY MatchID ASC, Team Initials ASC;

> ## Challenge
>
> - Write a query that returns Year, MatchID, and attendance from
> the matches table, sorted with the largest attendance at the top.
>
> > ## Solution
> > ~~~
> > SELECT Year, MatchID, attendance
> > FROM matches
> > ORDER BY Attendance DESC;
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}

## Order of execution

Another note for ordering. We don’t actually have to display a column to sort by
it.  For example, let’s say we want to order the Team Initials FRA by their MatchID, but
we only want to see Player Name and Shirt Number.

    SELECT Player Name, Shirt Number
    FROM WorldCupPlayers
    WHERE Team Initials = 'FRA'
    ORDER BY MatchID ASC;

We can do this because sorting occurs earlier in the computational pipeline than
field selection.

The computer is basically doing this:

1. Filtering rows according to WHERE
2. Sorting results according to ORDER BY
3. Displaying requested columns or expressions.

Clauses are written in a fixed order: `SELECT`, `FROM`, `WHERE`, then `ORDER
BY`. It is possible to write a query as a single line, but for readability,
we recommend to put each clause on its own line.

> ## Challenge
>
> - Let's try to combine what we've learned so far in a single
> query. Using the matches table, write a query to display the three date fields,
> `MatchesID`, Home Team Name and Away Team Name, for
> games in 1999, ordered alphabetically by the `Home Team Name`.
> - Write the query as a single line, then put each clause on its own line, and
> see how more legible the query becomes!
>
> > ## Solution
> > ~~~
> > SELECT Year, MatchID, Home Team Name, Away Team Name, Home Team Goals and Away Team Goals
> > FROM matches
> > WHERE year = 1999
> > ORDER BY Home Team Name;
> > ~~~
> > {: .sql}
> {: .solution}
{: .challenge}
