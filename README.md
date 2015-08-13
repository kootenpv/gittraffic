# gittraffic

#### Save your gittrafic data so it won't get lost!

Currently it is not possible to gather traffic data from github. The traffic will only show info from the 2 weeks. Using a cronjob with this tool, you'll be able to keep track from which websites your traffic comes from (and how many of them).

### Installation

Best way is to use pip to install:

```python
pip install gittraffic    # for python 2
pip3 install gittraffic   # for python 3
```

Now you have `gittraffic` as a python executable available on your system.

Upgrades can be done by giving the -U flag; `pip3 install -U gittraffic`.

### Command line usage

                1          2          3          4+
    Usage: <username> <password> <save_path> <package_name_1> <package_name_2> <etc>

### Roadmap

Insights, insights, insights:

First we need to save the data, afterwards, we will need to be able to do a simple analysis on it (e.g. per day stats, aggregates etc).

Tests, tests, tests:

I'll have to immediately notify me when github changes the traffic page, and push an update.
