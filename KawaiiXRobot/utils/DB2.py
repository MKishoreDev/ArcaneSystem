from utils import Database


class Db:
    def __init__(self):
        self.db = Database("sqlite+aiosqlite:///solidmusic.db")

    async def connect(self):
        return await self.db.connect()

    async def disconnect(self):
        return await self.db.disconnect()


        await self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS ins_db
            (
                chat_id integer,
                user_id integer
            )
            """
        )


db = Db()
