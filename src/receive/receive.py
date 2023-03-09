#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 09.03.2023, 23:37.

from src.receive.commands.commands import ReceiveCommand
from src.receive.messages.messages import ReceiveMessage


class Receive:
    command = ReceiveCommand
    message = ReceiveMessage
