import dateutil.parser
import gzip
import shutil

HOUR_TO_LETTER_MAP = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    '3': 'd',
    '4': 'e',
    '5': 'f',
    '6': 'g',
    '7': 'h',
    '8': 'i',
    '9': 'j',
    '10': 'k',
    '11': 'l',
    '12': 'm',
    '13': 'n',
    '14': 'o',
    '15': 'p',
    '16': 'q',
    '17': 'r',
    '18': 's',
    '19': 't',
    '20': 'u',
    '21': 'v',
    '22': 'w',
    '23': 'x'}

def get_year_as_string(datetime_):
    return str(datetime_.year)

def get_day_of_year_as_string(datetime_):
    return str(datetime_.timetuple().tm_yday)

def get_day_of_year_as_string(datetime_):
    return str(datetime_.timetuple().tm_yday)

def get_hour_as_string(datetime_):
    return str(datetime_.hour)

def get_year_shorthand_as_string(datetime_):
    return get_year_as_string(datetime_)[2:]

def convert_hour_to_letter(hour):
    return HOUR_TO_LETTER_MAP[hour]

def convert_iso8601_to_datetime(iso8601_datetime):
    return dateutil.parser.parse(iso8601_datetime)

def write_to_file(content, filename):
    with open(filename, "wb") as f:
        f.write(content)

def decompress_gz_file(filename):
    with gzip.open(filename, 'rb') as f_in:
        with open(filename[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    return filename[:-3]