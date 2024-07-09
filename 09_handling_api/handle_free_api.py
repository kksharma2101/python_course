import requests

def fetch_random_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data['success'] and 'data' in data:
        user_data = data['data']
        gender = user_data['gender']
        title = user_data['location']['city']
        print(f"Gender: {gender}\n City: {title}")
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        fetch_random_freeapi()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()