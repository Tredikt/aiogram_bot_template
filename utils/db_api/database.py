from sqlite3 import connect


class DataBase:
    def __init__(self, db_name):
        self.conn = connect(database=db_name)
        self.cur = self.conn.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                tg_id INTEGER PRIMARY KEY,
                username TEXT,
                fullname TEXT
            )
            """
        )

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS beginning_time(
                tg_id INTEGER PRIMARY KEY,
                time TEXT,
                is_begin INTEGER
            )
            """
        )

        self.conn.commit()

    def get_users(self):
        users_id = self.cur.execute(
            """
            SELECT tg_id FROM users
            """
        ).fetchall()

        return [elem[0] for elem in users_id] if users_id else []

    def add_user(self, tg_id: int, username: str, fullname: str):
        self.cur.execute(
            """
            INSERT OR REPLACE INTO users
            (tg_id, username, fullname)
            VALUES
            (?, ?, ?)
            """,
            (tg_id, username, fullname)
        )

        self.conn.commit()

    def get_user(self, tg_id: int):
        user_info = self.cur.execute(
            """
            SELECT username, fullname FROM users
            WHERE tg_id = ?
            """,
            (tg_id,)
        ).fetchone()

        return user_info if user_info else ()

    def add_beginning_time(self, tg_id: int, beginning_time: str, is_begin: int):
        self.cur.execute(
            """
            INSERT INTO beginning_time
            (tg_id, time, is_begin)
            VALUES
            (?, ?, ?)
            """,
            (tg_id, beginning_time, is_begin)
        )

        self.conn.commit()

    def get_beginning_time(self, tg_id: int):
        beginning_time = self.cur.execute(
            """
            SELECT time FROM beginning_time
            WHERE tg_id = ?
            """,
            (tg_id,)
        ).fetchone()

        return beginning_time[0] if beginning_time else "0_0_0"

    def get_is_begin(self, tg_id: int):
        is_begin = self.cur.execute(
            """
            SELECT is_begin FROM beginning_time
            WHERE tg_id = ?
            """,
            (tg_id,)
        ).fetchone()

        return is_begin[0] if is_begin else 0