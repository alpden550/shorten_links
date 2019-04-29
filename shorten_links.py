import os
import argparse
import requests
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('api_key')
BITLY_API_URL = 'https://api-ssl.bitly.com/v4/bitlinks'
HEADERS = {
    'Authorization': 'Bearer {}'.format(TOKEN),
}


def shorten_url(user_url, token=TOKEN):
    data = {
        'long_url': user_url,
    }

    response = requests.post(BITLY_API_URL, json=data, headers=HEADERS)
    response.raise_for_status()

    return response.json().get('link')


def count_clicks(bitlink, token=TOKEN):
    url = '{}/{}/clicks/summary'.format(BITLY_API_URL, bitlink)

    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    return response.json().get('total_clicks')


def check_link(url, token=TOKEN):
    url = '{}/{}'.format(BITLY_API_URL, url)

    response = requests.get(url, headers=HEADERS)
    return response


def create_parser():
    parser = argparse.ArgumentParser(description='This util shorten a link via bit.ly')
    parser.add_argument('url', help='Input valid link')
    return parser.parse_args()


if __name__ == '__main__':
    parser = create_parser()
    link = check_link(parser.url)

    if link:
        try:
            print(f'Количество переходов по ссылке битли: {count_clicks(parser.url)}')
        except requests.exceptions.HTTPError:
            print('You been inputted invalid bitly link')
    else:
        try:
            print(f'Для {parser.url} создана короткая ссылка:\n{shorten_url(parser.url)}')
        except requests.exceptions.HTTPError:
            print('You have to input correct and full url for shorteter')
