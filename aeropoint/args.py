import argparse

from aeropoint.validate_input import is_valid_utc_iso8601

def get_and_validate_args():
    base_station_id, \
    start_datetime, \
    end_datetime = get_args()

    if(not is_valid_utc_iso8601(start_datetime)):
        raise Exception('start_datetime is not a UTC iso8601')

    if(not is_valid_utc_iso8601(end_datetime)):
        raise Exception('end_datetime is not a UTC iso8601')
    
    return base_station_id, start_datetime, end_datetime

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'base-station-id',
        type=str,
        help="base station id you want data from")

    parser.add_argument(
        'start-datetime',
        type=str,
        help="start datetime should be UTC iso8601")

    parser.add_argument(
        'end-datetime',
        type=str,
        help="end datetime should be UTC iso8601")

    args = vars(parser.parse_args())

    return args['base-station-id'], args['start-datetime'], args['end-datetime']