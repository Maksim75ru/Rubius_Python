from typing import Dict
from dataclasses import dataclass

@dataclass
class File:  # Класс это некоторое описание типа. Этот класс объединяет функции, которые ссылаются на него. Далее мы можем порождать экземпляры этого класса. Класс содержит набор связанных с ним функций.
    def __init__(self, file_id: int, author: str, data: str):  # self в скобка в начале - это некое общее наименование. Функция init позволяет правильно проинициализировать содержимое класса.
        self.id = file_id  # self указывает на то, что мы присваиваем id конкретно своему полю id. Так же это означает принадлежность к какому-то объекту.
        self.author = author
        self.data = data

# Функция находящаяся внутри класса называется метод.
    def get_data(self) -> str:  # Ссылка на текущий объект.
        return self.data

    @staticmethod  # Чтобы можно было легко сослаться. Например: print(file.get_all_files())
    def get_all_files():
        return LIST_OF_FILES.values()  # Метод .values() - вернуть все значения

    @staticmethod
    def add_file(file):  # Тут указали только server, т.к. по дефолту знаем свой объект. (server: File) В скобках указываем то, что функция должная принять на вход. server - это своего рода ссылка на собственный объект. File - это подсказка на тип объекта.
        LIST_OF_FILES[file.id] = file  # [server.id], id - is key

    @staticmethod
    def remove_file(file_id):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
        del LIST_OF_FILES[file_id]  # del is key word


LIST_OF_FILES: Dict[int, File] = {}  # Dict[int, File] - указали, что Dict у нас от int и от File


if __name__ == '__main__':
    # File(0, "user_1", "file_1")
    # File(1, "user_1", "file_2")
    #
    # print(get_all_files())
    File.add_file(File(0, "user_1", "file_1"))
    File.add_file(File(1, "user_2", "file_2"))
    file = File(1, "user_1", "file_2")
    print(file.get_data())  # file.get_data() file - означает объект который мы вызываем, выше в классе он обозначается как self. Функция get_data, которая находится внутри класса называется МЕТОД.
    print(File.get_all_files())


    File.remove_file(0)
    print(File.get_all_files())
