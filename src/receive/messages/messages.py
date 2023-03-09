#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 10.03.2023, 01:00.

from src.receive.messages.location import MessageLocation


class ReceiveMessage:
    location = MessageLocation.run
