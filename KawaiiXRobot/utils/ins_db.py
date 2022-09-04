from KawaiiXRobot.utils.db import DATABASE


class insDB(DATABASE):
    async def get_ins(self, chat_id: int):
        return [
            row[1]
            for row in await self.db.fetch_all(
                "select * from ins_db where chat_id = :chat_id", {"chat_id": chat_id}
            )
        ]

    async def add_ins(self, chat_id: int, user_id: int):
        if user_id in await self.get_ins(chat_id):
            return "already_become_ins"
        await self.db.execute(
            "insert into ins_db values (:chat_id, :user_id)",
            {"chat_id": chat_id, "user_id": user_id},
        )
        return "added_ins"

    async def del_ins(self, chat_id: int, user_id: int):
        if user_id not in await self.get_ins(chat_id):
            return "already_deleted_ins"
        await self.db.execute(
            "delete from ins_db where chat_id = :chat_id and user_id = :user_id",
            {"chat_id": chat_id, "user_id": user_id},
        )
        return "deleted_ins"



