# Commsquare Python Programming Challenge


The main focus is on clear code that is easy to extend.


## Modules

### base.py 


Define abstract classes.

1. `DataReader` - reads log records from data source (cvs in implementation) and returns list of LogRecords.
2. `Calculator` - uses DataReader to read input data and does statistic calculation.
3. `DataWriter` - Save output of `Calculator` to 


### kpi1.py

Implemention of Calculator and DataWriter for kpi1 report

### kpi2.py

Implemention of Calculator and DataWriter for kpi2 report


### raw_log.py

Implementation of DataReader for reading cvs files from


### main.py

Create process workflows for kpi1 and kpi2 reports using DataReader, Calculator and DataWriter from corresponded module.
