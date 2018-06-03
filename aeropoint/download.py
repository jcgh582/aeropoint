from aeropoint.generate_urls import generate_urls
from aeropoint.download_url import download_url
from aeropoint.helpers import decompress_gz_file

def download(base_station_id, start_datetime, end_datetime):
    filenames = []
    for url in generate_urls(base_station_id, start_datetime, end_datetime):
        filename = download_url(url)
        filename = decompress_gz_file(filename)
        filenames.append(filename)
    
    return filenames