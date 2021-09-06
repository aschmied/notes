# Data Exploration with Pandas

These notes give examples of some basic data visualizations using Pandas. The examples are adapted from the blog posts in the references section below. The input data comes from Statistics Canada and is linked in the references.

## Prerequisites

* Python. I used 3.9.6
* Pandas. I used 1.3.2
* iPython (optional). I used 7.26.0

## Getting Data

* I used [Incident-based crime](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701) and [Police personnel](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510007601) statistics from Statistics Canada
* I collected data for 5 provinces as follows:
    * Select a province using the "Geography" dropdown
    * Click "apply"
    * Click "download options"
    * Choose "CSV (for database loading)"
* The files are included here so the examples continue to work if Statistics Canada changes their schema

## Loading the Data

* Start Python and import Pandas:

        ipython
        import pandas as pd

* Use [`read_csv`](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.read_csv.html) to parse the CSV files and keep only the columns we are interested in:

        police_nb = pd.read_csv('3510007601_databaseLoadingData_NB.csv', usecols=['REF_DATE', 'GEO', 'Statistics', 'VALUE'])

    This gives:

        In [17]: police_nb
        Out[17]:
             REF_DATE            GEO                     Statistics    VALUE
        0        1998  New Brunswick  Total number of all personnel  1603.00
        1        1999  New Brunswick  Total number of all personnel  1635.00
        2        2000  New Brunswick  Total number of all personnel  1606.00
        3        2001  New Brunswick  Total number of all personnel  1661.00
        4        2002  New Brunswick  Total number of all personnel  1621.00
        ..        ...            ...                            ...      ...
        259      2015  New Brunswick        Weighted clearance rate    36.81
        260      2016  New Brunswick        Weighted clearance rate    41.64
        261      2017  New Brunswick        Weighted clearance rate    37.40
        262      2018  New Brunswick        Weighted clearance rate    35.41
        263      2019  New Brunswick        Weighted clearance rate    33.31

* Select the rows we care about: police officers/100,000 population. The syntax looks a bit weird here. `==` returns a array of bools where `True` means a row is returned and `False` means it is not:

        index = (police_nb["Statistics"] == "Police officers per 100,000 population")
        police_nb = police_nb[index]

    Now we have:

        In [20]: police_nb
        Out[20]:
             REF_DATE            GEO                              Statistics  VALUE
        132      1998  New Brunswick  Police officers per 100,000 population  170.9
        133      1999  New Brunswick  Police officers per 100,000 population  171.9
        134      2000  New Brunswick  Police officers per 100,000 population  174.0
        135      2001  New Brunswick  Police officers per 100,000 population  175.6
        136      2002  New Brunswick  Police officers per 100,000 population  174.3
        137      2003  New Brunswick  Police officers per 100,000 population  170.8
        138      2004  New Brunswick  Police officers per 100,000 population  173.7
        139      2005  New Brunswick  Police officers per 100,000 population  173.4
        140      2006  New Brunswick  Police officers per 100,000 population  173.1
        141      2007  New Brunswick  Police officers per 100,000 population  177.9
        142      2008  New Brunswick  Police officers per 100,000 population  181.4
        143      2009  New Brunswick  Police officers per 100,000 population  181.9
        144      2010  New Brunswick  Police officers per 100,000 population  185.6
        145      2011  New Brunswick  Police officers per 100,000 population  182.2
        146      2012  New Brunswick  Police officers per 100,000 population  179.9
        147      2013  New Brunswick  Police officers per 100,000 population  177.2
        148      2014  New Brunswick  Police officers per 100,000 population  170.0
        149      2015  New Brunswick  Police officers per 100,000 population  168.4
        150      2016  New Brunswick  Police officers per 100,000 population  168.3
        151      2017  New Brunswick  Police officers per 100,000 population  160.9
        152      2018  New Brunswick  Police officers per 100,000 population  159.5
        153      2019  New Brunswick  Police officers per 100,000 population  161.0

* Do a [pivot](https://pandas.pydata.org/docs/user_guide/reshaping.html) to reshape the data for subsequent display:

        police_nb = police_nb.pivot(index='REF_DATE', columns='GEO', values='VALUE')

    Now we have:

        In [46]: police_nb
        Out[46]:
        GEO       New Brunswick
        REF_DATE
        1998              170.9
        1999              171.9
        2000              174.0
        2001              175.6
        2002              174.3
        2003              170.8
        2004              173.7
        2005              173.4
        2006              173.1
        2007              177.9
        2008              181.4
        2009              181.9
        2010              185.6
        2011              182.2
        2012              179.9
        2013              177.2
        2014              170.0
        2015              168.4
        2016              168.3
        2017              160.9
        2018              159.5
        2019              161.0

* Repeat this for all of the police CSVs then [`concat`](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) them into a single `DataFrame`. For example, here is how to do the first two:

        police = pd.concat([police_nb, police_nl], axis=1)

    Giving:

        In [47]: police
        Out[47]:
        GEO       New Brunswick  Newfoundland and Labrador
        REF_DATE
        1998              170.9                      143.7
        1999              171.9                      143.8
        2000              174.0                      146.2
        2001              175.6                      146.9
        2002              174.3                      149.9
        2003              170.8                      148.1
        2004              173.7                      148.0
        2005              173.4                      150.9
        2006              173.1                      156.5
        2007              177.9                      164.6
        2008              181.4                      172.8
        2009              181.9                      177.5
        2010              185.6                      179.9
        2011              182.2                      178.1
        2012              179.9                      175.9
        2013              177.2                      174.0
        2014              170.0                      169.5
        2015              168.4                      168.3
        2016              168.3                      171.9
        2017              160.9                      172.4
        2018              159.5                      171.2
        2019              161.0                      172.9

* Repeat this whole process to load the crime data into a `DataFrame` named `crime`

* There is a complication with province names in the crime data: they have a number at the end like "New Brunswick [13]." We want them to be the same as in police, use [`rename`](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename) to rename the columns

* I wrote a "load_data.py" scrip to do this all for you. In iPython you can run it with `%run`:

        In [51]: %run load_data.py

        In [52]: police
        Out[52]:
        GEO       New Brunswick  Newfoundland and Labrador  Nova Scotia  Ontario  Prince Edward Island  Quebec
        REF_DATE
        1998              170.9                      143.7        170.5    179.9                 149.5   186.9
        1999              171.9                      143.8        169.4    182.7                 144.5   187.8
        2000              174.0                      146.2        171.3    185.2                 150.2   188.1
        2001              175.6                      146.9        169.6    186.4                 148.5   188.3
        2002              174.3                      149.9        170.3    187.1                 156.3   194.0
        2003              170.8                      148.1        171.5    189.8                 158.9   192.0
        2004              173.7                      148.0        171.9    187.4                 150.4   191.4
        2005              173.4                      150.9        173.1    186.9                 154.3   194.6
        2006              173.1                      156.5        177.7    187.6                 159.6   197.8
        2007              177.9                      164.6        188.0    191.6                 164.8   198.0
        2008              181.4                      172.8        199.2    193.6                 166.5   198.5
        2009              181.9                      177.5        200.1    196.6                 167.3   198.0
        2010              185.6                      179.9        203.0    200.3                 168.0   196.6
        2011              182.2                      178.1        202.7    199.0                 169.5   197.4
        2012              179.9                      175.9        205.0    196.1                 170.9   198.2
        2013              177.2                      174.0        201.5    195.1                 161.0   197.3
        2014              170.0                      169.5        200.7    192.0                 163.6   198.7
        2015              168.4                      168.3        198.1    191.2                 156.4   195.9
        2016              168.3                      171.9        193.3    188.6                 154.5   194.0
        2017              160.9                      172.4        192.7    184.6                 147.5   191.4
        2018              159.5                      171.2        193.9    176.9                 140.6   189.0
        2019              161.0                      172.9        190.7    174.0                 136.7   184.1


# References

* [Pedro Marcelino "Comprehensive data exploration with Python" Feb 2017](https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python)
* [neelutiwari "How To Perform Data Visualization with Pandas" Jul 2021](https://www.analyticsvidhya.com/blog/2021/07/how-to-perform-data-visualization-with-pandas/)
* [Soner Yıldırım "Data Visualization with Pandas" Feb 2021](https://towardsdatascience.com/data-visualization-with-pandas-1571bbc541c8)
* [Statistics Canada "Incident-based crime statistics, by detailed violations, Canada, provinces, territories and Census Metropolitan Areas (Table  35-10-0177-01)" Jul 2017](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)
* [Statistics Canada "Police personnel and selected crime statistics (Table: 35-10-0076-01)" Dec 2020](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510007601)