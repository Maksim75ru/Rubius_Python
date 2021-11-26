# Тут я храню данные
class File:  # Класс это некоторое описание типа. Этот класс объединяет функции, которые ссылаются на него. Далее мы можем порождать экземпляры этого класса. Класс содержит набор связанных с ним функций.

    def __init__(self, file_id: int, author: str, data: str):
        self.__disk = {
            'id': file_id,
            'author': author,
            'data': data,
        }

    def __repr__(self) -> str:
        return f'File(id={self.id}, author={self.__disk["author"]}, data={self.__disk})'

    @property
    def id(self) -> int:
        return self.__disk['id']

    @property
    def data(self) -> str:
        return self.__disk['data']

    @data.setter
    def data(self, data: str):
        self.__disk['data'] = data

# Этот класс занимается управлением файлами(добавить, удалить и т.д.).
class FileManager:
    def __init__(self, name: str):
        self.__name = name
        self.__files = {}

    def get_all_files(self):
        return self.__files.values()  # Метод .values() - вернуть все значения

    def add_file(self,
                 file):  # Тут указали только server, т.к. по дефолту знаем свой объект. (server: File) В скобках указываем то, что функция должная принять на вход. server - это своего рода ссылка на собственный объект. File - это подсказка на тип объекта.
        self.__files[file.id] = file  # [server.id], id - is key

    def remove_file(self,
                    file_id):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
        del self.__files[file_id]  # del is key word


if __name__ == '__main__':
    personal_file_manager = FileManager('personal')
    personal_file_manager.add_file(File(0, "user_1", "file_1"))
    personal_file_manager.add_file(File(1, "user_2", "file_2"))
    print(personal_file_manager.get_all_files())

    work_files_manager = FileManager('work')

    file = File(1, "user_1", "file_2")
    print(file.data)
    work_files_manager.add_file(file)
    print(work_files_manager.get_all_files())
