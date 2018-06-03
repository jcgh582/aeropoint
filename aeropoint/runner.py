import logging

from aeropoint.merge import merge
from aeropoint.download import download

def run(base_station_id, start_datetime, end_datetime):
    logging.info('running..')
    logging.info('base_station_id {}'.format(base_station_id))
    logging.info('start_datetime {}'.format(start_datetime))
    logging.info('end_datetime {}'.format(end_datetime))

    filenames = download(base_station_id, start_datetime, end_datetime)
    merge(filenames)