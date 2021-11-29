from typing import Iterable
from File import File


class BaseStorage(object):
    def __init__(self, folder: str):
        self._files = {}
        self.__folder = folder  # одни папки будут храниться в других папках


class ReadOnlyStorage(BaseStorage):
    def get_all(self) -> Iterable[File]:
        return self._files.values()  # Метод .values() - вернуть все значения

    def get_one(self, file_id) -> File | None:
        return self._files.get(file_id)


class WriteOnlyStorage(BaseStorage):
    def put_one(self, file: File):
        self._files[file.id] = file  # [.id], id - is key

    def delete_one(self,
                   file_id: int):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
        del self._files[file_id]  # del is key word для удаления


# Этот класс занимается хранением файлов
class ReadWriteStorage(ReadOnlyStorage, WriteOnlyStorage):
    pass
