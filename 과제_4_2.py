import requests

def get_random_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data['name']
    else:
        print(f"Failed to get data for user_id={user_id}. Status code: {response.status_code}")
        return None
    if __name__ == "__main__":
        dummy_data = []

        for user_id in range(1, 11):
            name = get_random_user_data(user_id)
            if name is not None:
                dummy_data.append(name)

        print(dummy_data)