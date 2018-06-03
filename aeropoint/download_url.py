import logging
from urllib.request import urlretrieve

from aeropoint.constants import DESTINATION

def download_url(url):
    logging.info('downloading file from url {}'.format(url))

    try:
        detailsOfDownloadedFile = urlretrieve(url, DESTINATION + url.split('/')[-1])
        nameOfDownloadedFile = detailsOfDownloadedFile[0]
    except Exception as e:
        logging.error('error downloading file from url {}'.format(url))
        raise e

    return nameOfDownloadedFile
