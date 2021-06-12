import requests
from csvparser import write_csv


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return list(response.json())
    else:
        return list()


all_photos = get_data('https://jsonplaceholder.typicode.com/photos')
write_csv('photos.csv', all_photos, all_photos[0].keys())
