rules = {
    'Users_Locations': {
        'James': 'Providence',
        'Jesse': 'Wakefield',
        'Mitch': 'Middletown'
    },
    'Providence': {
        'James': 0,
        'Jesse': 65.6,      # total distance from work to prov to home
        'Mitch': 68.6,      # total distance from work to prov to home
    },
    'Wakefield': {
        'James': 68.9,      # total distance from work to wakefield to home
        'Jesse': 0,
        'Mitch': 57.1       # total distance from work to wakefield to home
    },
    'Middletown': {
        'James': 75.5,      # total distance from work to middletown to home
        'Jesse': 51.4,      # total distance from work to middletown to home
        'Mitch': 0,
    },
    'Location_Requirements': {
        'Tuesday': 'Middletown',
        'Wednesday': 'Middletown'
    }
}


logfile = 'history.log'
