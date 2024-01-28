from datetime import datetime
from os import getcwd
import os.path

import requests

from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print('The current date is', datetime.date(datetime.now()))

    url = 'https://media.licdn.com/dms/image/C4E22AQE7ghvrlEuQrw/' \
          'feedshare-shrink_800/0/1677625712135?e=2147483647&v=beta&t=' \
          '6EPmS0AY8nsKNYmMpZTbD1NvNY9p_R36B39HucgQxy0'
    data = requests.get(url)
    file_name = 'logo.png'
    if 200 <= data.status_code < 300:
        with open(file_name, 'wb') as f:
            f.write(data.content)
            print('The logo has been successfully saved in',
                  os.path.join(getcwd(), file_name))
    else:
        print(f'The error has occurred while trying to download {file_name} '
              f'from URL {url}')
