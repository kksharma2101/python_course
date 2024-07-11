from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()



try:
    client = MongoClient(os.getenv('MONGODB_URL'),tlsAllowInvalidCertificates=True)

    db = client["ytmanager"]

    video_collections = db["videos"]

    def list_all_video():
        for video in video_collections.find():
            print(f"video_id: {video["_id"]}, Name: {video['name']}, Time: {video['time']}")

    def add_video(name, time):
        video_collections.insert_one({"name": name, "time": time})

    def update_video(name, time, video_id):
        video_collections.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": name, "time": time}})

    def delete_video(video_id):
        video_collections.delete_one({"_id": ObjectId(video_id)})


    def main():
        while True:
            print("\n youtube manager app")
            print("1. Youtube video list")
            print("2. Add videos")
            print("3. Update a videos")
            print("4. Delete a videos")
            print("5. Exit")
            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    list_all_video()
                case "2":
                    name = input("Write video name: ")
                    time = input("Write video time: ")
                    add_video(name, time)
                case "3":
                    video_id = input("Write video id: ")
                    name = input("Write updated video name: ")
                    time = input("Write updated video time: ")
                    update_video(name, time, video_id)
                case "4":
                    video_id = input("Choose deleted video ID: ")
                    delete_video(video_id)
                case "5":
                    break

    if __name__ == "__main__":
        main()

except Exception as e:
    raise Exception("The following error occurred: ", e)
