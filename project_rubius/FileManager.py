from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass
class File:
    id: int
    author: str
    data: Iterable[str]


LIST_OF_FILES: Dict[int, File] = {}  # Dict[int, File] - указали, что Dict у нас от int и от File


def get_all_files() -> Iterable[File]:
    return LIST_OF_FILES.values()  # Метод .values() - вернуть все значения


def add_file(server: File):  # В скобках указываем то, что функция должная принять
    LIST_OF_FILES[server.id] = server  # [server.id], id - is key


def remove_file(file_id: int):  # file_id - назвали так, потому что в Python есть встроенная функция id/ Поэтому file_id
    del LIST_OF_FILES[file_id]  # del is key word


if __name__ == '__main__':
    add_file(File(0, "user_1", "file_1"))
    add_file(File(1, "user_1", "file_2"))

    print(get_all_files())

    remove_file(0)
    print(get_all_files())
