import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor =  con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, name TEXT NOT NULL, time TEXT NOT NULL)
''')


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if


if __name__ == "main":
    main()