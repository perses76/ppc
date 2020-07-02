# Python Programming Challenge


## Install

```
python setup.py install
```

## Configuration

All application settings should be stored in settings.py file.
As settings.py can contain sensitive information (as password), the file is exluded from git.
Please copy `settings.py.exampl` to `settings.py` file and change necessary variables


## Tests

```
pytest
```

Attention: setup settings.py in `tests` folder.

## Run

```
python -m ppc.main
```

Attention: setup settings.py in `ppc` folder.


## Class diagram

[Class diagram](docs/class_diagram.svg)


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
