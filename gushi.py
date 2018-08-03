import requests
import re

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}

def parse_page(url):
    response = requests.get(url, headers=headers)

    text = response.text


def main():

    url='https://www.gushiwen.org/default_2.aspx'
    parse_page(url)
if __name__ == '__main__':
    main()
