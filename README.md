[![Data-Golf-API](https://github.com/coreyjs/data-golf-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/coreyjs/data-golf-api/actions/workflows/python-app.yml)
[![PyPI version](https://badge.fury.io/py/data_golf.svg)](https://badge.fury.io/py/data_golf)


# Data Golf API (Unofficial)

### An Unofficial API Library for DataGolf.com APIs

This is a Python library for interacting with the DataGolf APIs. DataGolf is a golf analytics platform that provides a wide range of data and analytics for golf tournaments, players, and courses.

**This is an unofficial API lib, and it is not affiliated with DataGolf in any way.**


This is being built to support some ML projects I am working on.  I will be 
continuing to add more endpoints as I need them.  If you have a specific endpoint you need, please open a ticket for submit a PR.



---
# Usage
(Currently this only supports JSON formats, CSV is in progress)

```python
pip install data_golf
```

```python
from data_golf import DataGolfClient

client = DataGolfClient(api_key="YOUR_API_KEY")

# For more request logging
client = DataGolfClient(api_key="YOUR_API_KEY", verbose=True)
```


# General APIs

```python
# Player List
players = client.general.player_list()

# Tour  Schedule
tour_schedule = client.general.tour_schedule()
```