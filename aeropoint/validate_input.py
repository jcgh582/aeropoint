import dateutil.parser
import re

def is_valid_utc_iso8601(string_):
    try:            
        datetime = dateutil.parser.parse(string_)
        result = True
    except:
        result = False

    if (string_[-1] != 'Z'):
        result = False

    return result