# BandScheduler
Simple terminal app to pick the location of a band's next practice.

## How to Use
```terminal
$ python2.7 main.py -d monday
Your practice will be held in Providence!
```

## Customization
### Users, mileage, and Locations 
To change users, mileage, locations, and demand specific locations for specific days, open the `rules.py` and change:
```python
# to edit user locations
rules = {
    # to edit users and their locations
    'Users_Locations': {
        'UserName1': 'Location1',
        'UserName2': 'Location2',
        'UserName3': 'Location3'
    }

    # to edit mileage to locations
    'Location1': {
        'UserName1': 0,
        'UserName2': 23.1,   # Total travel distance, including both to and from
        'UserName2': 45.2    # Total travel distance, including both to and from
    }

    # to edit required days/locations
    'Location_Requirements': {
        'Tuesday': 'Location3',
        'Wednesday': 'Location3',
    }
}

# and lastly, to edit the name of the log file
logfile = 'your_logfile_name_here.log'  # default 'history.log'
```

### Modify, Change, Delete Past Log Entries
To modify, change, and delete past events, simply make changes and/or delete entries from the saved logfile

## For Additional Help
```terminal
$ python2.7 main.py --help
```

## Rights
All rights and posession legally, credit-abily or otherwise, belongs to a Mr. James Boynton of Providence, RI
