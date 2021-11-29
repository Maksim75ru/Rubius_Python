from dataclasses import dataclass


# Тут я храню данные
@dataclass  # Если класс не занят ничем, кроме как хранением данных, то сразу его делам dataclass
class File:
    id: int
    author: str
    data: str
