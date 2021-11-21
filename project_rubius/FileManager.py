from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass
class File:
    id: int
    author: str
    data: Iterable[str]


LIST_OF_FILES: Dict[int, File] = {}


def get_all_files() -> Iterable[File]:
    return LIST_OF_FILES.values()


def add_file(server: File):
    LIST_OF_FILES[server.id] = server


def remove_file(file_id: int):
    del LIST_OF_FILES[file_id]


if __name__ == '__main__':
    add_file(File(0, "user_1", "file_1"))
    add_file(File(1, "user_1", "file_2"))

    print(get_all_files())

    remove_file(0)
    print(get_all_files())
