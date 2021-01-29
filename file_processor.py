import os
import shutil
import logging


class FileProcessor:
    """
    Класс для раоты с файлом данных (товаров)
    Свойства:
        self.file_path - путь до файла с данными
        self.data - содержимое файла с данными
    Методы:
        __init__(self)
        select_path(self, mode='user': str)
        save_file(self)
    """

    def __init__(self):
        self.file_path = ''
        self.data = None

    def select_path(self, mode='user', path=''):
        """
        Получает путь до файла с данными, открывает его и возвращает список,
        сформированный из этого файла, либо пустой список при неудаче
        :param mode: str, 'user' or 'test'
        :param path: str, only for test mode
        :return: list
        """

        logger = logging.getLogger('FileProcessor.select_path_file')

        if mode == 'user':

            print('Введите путь до файла с товарами:')
            self.file_path = str(input())

        elif mode == 'test':

            if not path:
                self.file_path = 'data/goods.info'
            else:
                self.file_path = path

        self.file_path = self.file_path.strip(" ' ")
        self.file_path = self.file_path.strip(' " ')

        self.file_path = os.path.abspath(self.file_path)

        if os.path.isfile(self.file_path) \
                and os.path.exists(self.file_path):

            with open(self.file_path, 'r',
                      encoding="utf-8") as self.data:
                data_list = self.data.readlines()
                return data_list

        else:
            print('Не удалось открыть файл: {}'.format(self.file_path))
            logger.error('Не удалось открыть файл: {}'.format(self.file_path))
            return []

    def save_file(self):
        """
        Сохраняет файл в указанную директорию
        return: bool
        """

        logger = logging.getLogger('FileProcessor.save_file')

        if self.data is None:
            print('Невозможно сохранить файл')
            logger.error('Невозможно сохранить файл')
            return False

        print('Укажите директорию сохранения:')

        saving_dir = str(input())
        saving_dir = saving_dir.strip(" ' ")
        saving_dir = saving_dir.strip(' " ')
        saving_dir = os.path.abspath(saving_dir)

        if os.path.isfile(saving_dir):
            print('Неверно указана директория {}'.format(saving_dir))
            logger.error('Неверно указана директория {}'.format(saving_dir))
            return False

        if not os.path.exists(saving_dir):
            os.makedirs(saving_dir)
            shutil.copy(self.file_path, saving_dir)
        else:
            filename = os.path.basename(self.file_path)
            saving_path = os.path.join(saving_dir, filename)

            if self.file_path == saving_path:
                print('Директории совпадают')
                logger.error('Директории совпадают')
                return False
            else:
                shutil.copy(self.file_path, saving_dir)
                return True
