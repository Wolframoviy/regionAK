from cs50 import SQL

open("app/database.db", "w").close()
db = SQL("sqlite:///app/database.db")

db.execute("""
CREATE TABLE "posts" (
                    "id"	INTEGER NOT NULL UNIQUE,
                    "title"	TEXT,
                    "content"	TEXT,
                    "image"	TEXT,
                    "author_id"	INTEGER,
                    "pdate"	INTEGER,
                    "source"	TEXT,
                    PRIMARY KEY("id" AUTOINCREMENT)
)""")

db.execute("""
CREATE TABLE "users" (
                    "id"	INTEGER NOT NULL UNIQUE,
                    "email"	TEXT(60) NOT NULL,
                    "username"	TEXT(16) NOT NULL,
                    "passwordhash"	TEXT,
                    "image"	TEXT,
                    "realname"	TEXT,
                    "rank"	INTEGER NOT NULL DEFAULT 0,
                    PRIMARY KEY("id" AUTOINCREMENT)
)
""")
