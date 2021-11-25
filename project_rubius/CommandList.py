from dataclasses import dataclass
from typing import List
from enum import Enum  # Для установки статуса команд. Проверять успешна ли выполнилась команда или нет.


class Status(Enum):  # Нужно расписать подробнее и указывать какие именно ошибки получаем.(Пример: PermissionError(Ошибка разрешения))
    Ok = 0,
    Error = 1


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


def send_command(command: Command) -> Status:
    if command.command == GLOBAL_COMMANDS[0].command:  # Написать норм код сюда нужно.Это для образца.Тут ничего не send'им, а просто определяем статус
        return Status.Ok

    return Status.Error


# Написать функцию process(обработка)
if __name__ == '__main__':
    pass
