import logging

from aeropoint.args import get_and_validate_args
from aeropoint.runner import run

def setup_logging():
    logging.basicConfig(level=logging.INFO,
        format='%(asctime)s %(levelname)s %(module)s %(message)s')

def main():
    try:
        setup_logging()
        base_station_id, start_datetime, end_datetime = get_and_validate_args()
        run(base_station_id, start_datetime, end_datetime)
    except Exception as e:
        logging.error('fatal error!')
        logging.exception(e)

if __name__ == '__main__':
    main()
