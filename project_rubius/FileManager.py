from dataclasses import dataclass
from typing import Iterable

# Тут я храню данные
@dataclass  # Если класс не занят ничем, кроме как хранением данных, то сразу его делам dataclass
class File:  # Класс это некоторое описание типа. Этот класс объединяет функции, которые ссылаются на него. Далее мы можем порождать экземпляры этого класса. Класс содержит набор связанных с ним функций.
    id: int
    author: str
    data: str


class ReadOnlyStorage:
    def __init__(self, folder: str):
        self._files = {}
        self. __folder = folder  # одни папки будут храниться в других папках

    def get_all(self) -> Iterable[File]:
        return self._files.values()  # Метод .values() - вернуть все значения

    def get_one(self, file_id) -> File | None:
        return self._files.get(file_id)


# Этот класс занимается хранением файлов
class Storage(ReadOnlyStorage):
    def put_one(self,
                file: File):  # Тут указали только server, т.к. по дефолту знаем свой объект. (server: File) В скобках указываем то, что функция должная принять на вход. server - это своего рода ссылка на собственный объект. File - это подсказка на тип объекта.
        self._files[file.id] = file  # [server.id], id - is key

    def delete_one(self,
                   file_id: int):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
        del self._files[file_id]  # del is key word


# Этот класс занимается управлением файлами(добавить, удалить и т.д.).
class FileManager:
    def __init__(self, name: str, storage: Storage):
        self.__name = name
        self.__storage = storage

    def get_all_files(self):
        return self.__storage.get_all()  # Метод .values() - вернуть все значения

    def add_file(self, file):  # Тут указали только server, т.к. по дефолту знаем свой объект. (server: File) В скобках указываем то, что функция должная принять на вход. server - это своего рода ссылка на собственный объект. File - это подсказка на тип объекта.
        self.__storage.put_one(file)  # [server.id], id - is key

    def remove_file(self,
                    file_id):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
        self.__storage.delete_one(file_id)  # del is key word


if __name__ == '__main__':
    main_storage: ReadOnlyStorage = Storage("~/data_storage")

    personal_file_manager = FileManager('personal', main_storage)
    personal_file_manager.add_file(File(0, "user_1", "file_1"))
    personal_file_manager.add_file(File(1, "user_2", "file_2"))
    print(personal_file_manager.get_all_files())

    work_files_manager = FileManager('work', main_storage)

    f = File(1, "user_1", "file_2")
    print(f.data)
    work_files_manager.add_file(f)
    print(work_files_manager.get_all_files())

    # Тесты
    tmp_storage = ReadOnlyStorage("/tmp/tests/data_storage")
    # assert len(tmp_storage.get_all()) == 0
    tmp_storage.get_one(1)
    # tmp_storage.delete_one(1)
