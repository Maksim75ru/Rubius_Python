from dataclasses import dataclass
from typing import List
from enum import Enum  # Для установки статуса команд. Проверять успешна ли выполнилась команда или нет.


class Status(Enum):  # Нужно расписать подробнее и указывать какие именно ошибки получаем.(Пример: PermissionError(Ошибка разрешения))
    Ok = 0,
    Error = 1


@dataclass  # Это декоратор, красивая обертка. Доп.логику пишет за нас. Определяет за нас __init__, __str__.
class Response:
    status: Status
    response: str


@dataclass
class Command:
    command: str
    parameters: List[str]


# Мой протокол. Мой сервер знает следующие команды:
GLOBAL_COMMANDS = [
    Command("GET_ALL_FILES", []),
    Command("GET FILE", ['filename']),
    Command("GET_CONTENT", ['filename']),
    Command("REMOVE-FILE", ['filename'])
]


def get_all_files():  # Эта функция занимается логикой
    return ["file_1.txt", "file_2.txt"]  # Тут харкодим. Нужно исправить/сделать ссылки на возврат файлов.


def send_command(command: Command) -> Response:  # Эта функция занимается обработкой
    if command.command == GLOBAL_COMMANDS[0].command:  # Написать норм код сюда нужно.Это для образца.Тут ничего не send'им, а просто определяем статус
        return Response(Status.Ok, ':' .join(get_all_files()))

    return Response(Status.Error, 'Unknown command')


# Написать функцию process(обработка)
if __name__ == '__main__':
    pass
