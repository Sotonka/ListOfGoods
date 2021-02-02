import os
import pathlib


class LogsProcessor:
    """
    Класс для раоты с файлом данных (товаров)
    Свойства:
        self.logs_path - путь до файла с логами
    Методы:
        __init__(self)
        select_logs_path(self, mode='user': str)
        get_dict_config(self)
    """

    def __init__(self):
        self.logs_path = ''

    def select_logs_path(self, mode='user'):
        """
        Получает путь до файла с логами, если файла нет - создает его
        :param mode: str, 'user' or 'test'
        :return: list
        """

        if mode == 'user':

            print('Введите директорию для логов:')
            self.logs_path = str(input())

            self.logs_path = self.logs_path.strip(" ' ")
            self.logs_path = self.logs_path.strip(' " ')

            self.logs_path = os.path.abspath(self.logs_path)

        elif mode == 'test':

            self.logs_path = '../ListOfGoods/'

        if os.path.exists(os.path.join(self.logs_path, 'logs.log')):

            print('Указанный файл с логами существует: {}'
                  .format(self.logs_path))

        else:

            pathlib.Path(self.logs_path).mkdir(parents=True, exist_ok=True)
            open(os.path.join(self.logs_path, 'logs.log'), 'tw',
                 encoding='utf-8').close()

    def get_dict_config(self):
        """
        Возвращает конфигурацию для логгирования
        :return: dict
        """

        dict_log_config = {
            "version": 1,
            "handlers": {
                "fileHandler": {
                    "class": "logging.FileHandler",
                    "formatter": "myFormatter",
                    "filename": os.path.join(self.logs_path, 'logs.log'),
                    "encoding": "utf-8"
                }
            },
            "loggers": {
                "loggerApp": {
                    "handlers": ["fileHandler"],
                    "level": "INFO",
                }
            },
            "formatters": {
                "myFormatter": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                }
            }
        }
        return dict_log_config
