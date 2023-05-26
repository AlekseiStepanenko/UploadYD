import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token


    def upload_file_to_disk(self, disk_file_path, filename):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        response_data = response.json()

        href = response_data['href']

        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    yd = YandexDisk(token=TOKEN)
    print(yd.upload_file_to_disk('DZ.txt', 'DZ.txt'))

