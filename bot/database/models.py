import datetime
from dataclasses import dataclass, asdict


@dataclass
class User:
    user_id: int
    cart: list
    lang: str

    def __call__(self):
        return asdict(self)