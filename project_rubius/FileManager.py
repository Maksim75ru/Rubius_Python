from Storage import *


# Этот класс занимается управлением файлами(добавить, удалить и т.д.).
class FileManager:
    def __init__(self, name: str, storage: ReadWriteStorage):
        self.__name = name
        self.__storage = storage

    def get_all_files(self):
        return self.__storage.get_all()  # Метод .values() - вернуть все значения

    def add_file(self, file):  # Тут указали только server, т.к. по дефолту знаем свой объект. (server: File) В скобках указываем то, что функция должная принять на вход. server - это своего рода ссылка на собственный объект. File - это подсказка на тип объекта.
        self.__storage.put_one(file)  # [server.id], id - is key

    def remove_file(self,
                    file_id):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
        self.__storage.delete_one(file_id)  # del is key word
