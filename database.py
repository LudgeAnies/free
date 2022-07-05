import sqlite3
import time


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.connection.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def mute_user(self, user_id):
        with self.connection:
            user = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchone()
            return int(user[2]) >= int(time.time())

    def add_mute_days(self, user_id, mute_time):
        with self.connection:
            return self.connection.execute(
                "UPDATE `users` SET `mute_time` = ? WHERE `user_id` = ?", (int(time.time()) + (
                        mute_time * 60 * 60 * 24
                ), user_id,)
            ) # мут в днях

    def add_mute_hours(self, user_id, mute_time):
        with self.connection:
            return self.connection.execute(
                "UPDATE `users` SET `mute_time` = ? WHERE `user_id` = ?", (int(time.time()) + (
                        mute_time * 60 * 60
                ), user_id,)
            ) # мут в часах

    def add_mute_minutes(self, user_id, mute_time):
        with self.connection:
            return self.connection.execute(
                "UPDATE `users` SET `mute_time` = ? WHERE `user_id` = ?", (int(time.time()) + (
                        mute_time * 60
                ), user_id,)
            ) # мут в минутах
