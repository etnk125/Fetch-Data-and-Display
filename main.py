from fetch import fetch_data
from bnk_manager import BNKManager
URL = 'https://jsonkeeper.com/b/I316'


def main():
    data = fetch_data(URL)
    manager = BNKManager(data['members'])
    # manager.display_name(reverse=True, lang='en')
    manager.display_month()


if __name__ == '__main__':
    main()
