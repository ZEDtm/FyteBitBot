import datetime
from fb_bot.database.collection import users_db
from dataclasses import dataclass, asdict


@dataclass
class User:
    user_id: int
    ticket: int
    lang: str

    def __call__(self) -> dict:
        return asdict(self)

    @staticmethod
    async def get_user_on_ticket(ticket: int) -> dict:
        return users_db.find_one({'ticket': int(ticket)})

    @staticmethod
    async def set_ticket(ticket: int, user_id: int | str) -> None:
        users_db.update_one({'user_id': int(user_id)}, {'$set': {'ticket': ticket}})

    @staticmethod
    async def delete_ticket(user_id: int | str) -> None:
        users_db.update_one({'user_id': int(user_id)}, {'$set': {'ticket': 0}})

