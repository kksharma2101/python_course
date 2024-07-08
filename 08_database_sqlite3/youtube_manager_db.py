import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor =  con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, name TEXT NOT NULL, time TEXT NOT NULL)
''')

def list_all_videos():
    cursor.execute("SELECT * FROM VIDEOS")

    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO VIDEOS (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    con.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Write a movie name: ")
            time = input("Write a movie duration: ")
            add_video(name, time)    
        elif choice == "3":
            video_id = input("Give the video id for update: ")
            name = input("Update movie name: ")
            time = input("Update movie duration: ")
            update_video(video_id, name, time)    
        elif choice == "4":
            video_id = input("Give the video id for delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice ")

 
    con.close()

if __name__ == "__main__":
    main()