from GetArgs   import getargs
from random    import randrange
from nice_json import json_get, json_print_pretty
from os.path   import isfile
from rules     import rules, logfile


'''
Summary:
 - def run()
 - def print_help()
 - def get_next_location(day, last_values)
 - def choose_random_location()
 - def save_to_log(location, day, log)
'''


def run():
    # set up terminal arguments
    myargs = getargs([
        '-d',    'day',
        '--day', 'day',
        '-h', '--help'
    ])
    args = myargs.getargs()


    log = json_get(logfile)['Log']          # load saved log file
    last_values = log[-1]['Current_Tally']  # get latest entry from log file

    if '-d' in args or '--day' in args:
        day      = args['day'].lower()
        location = get_next_location(day, last_values)
        save_to_log(location, day, log)
        print('Your practice will be held in {}!'.format(location))
    else:
        print_help()


def print_help():
    print('''

################################################################################

-d, --day  <day of week>  : Provide the day of the week to schedule practice
                          :
-h, --help                : Display this program's help screen
--------------------------------------------------------------------------------

Options:
 - To change people/locations/mileage, edit the 'rules.py' file.
 - To delete a practice that was illegitimate, simly remove the enry from
   the generated log file.
 - To change the log file file-name, change 'logfile' in 'rules.py'

################################################################################

''')


def get_next_location(day, last_values):
    # get list of day requirements
    keys = rules['Location_Requirements'].keys()
    for k in keys:
        if day == k.lower():
            # if a day matches requirements, skip mileage
            return rules['Location_Requirements'][k]

    # get location based on who has driven more in the past
    x    = 0
    user = 'none'
    keys = last_values.keys()
    for k in keys:
        value = last_values[k]
        if value > x:
            x    = value
            user = k

    if user != 'none':
        return rules['Users_Locations'][user]
    else:
        # incase of a tie, choose location randomly
        return choose_random_location()


def choose_random_location():
    keys = rules['Users_Locations'].keys()  # get list of users
    key = keys[randrange(len(keys))]        # randomly choose a user
    return rules['Users_Locations'][key]    # return location of chosen user


def save_to_log(location, day, log):
    last_values = log[-1]['Current_Tally']  # get latest log entry

    # generate the new log entry
    result = {
        'Location': location,
        'Day': day,
        'Current_Tally': {
            name: last_values[name] + rules[location][name]
            for name in rules['Users_Locations'].keys()
        }
    }

    new_log = { 'Log': log+[result] }       # create and save the new log

    with open(logfile, 'w') as f:
        f.write(json_print_pretty(new_log))


if __name__ == '__main__':
    # if log file doesnt exist, create it
    try:
        with open(logfile) as f: pass
    except:
        with open(logfile, 'w') as f:
            f.write('{ \"Log\": [ { \"Current_Tally\": { \"James\": 0, \"Jesse\": 0, \"Mitch\": 0 } } ] }')
    run()
