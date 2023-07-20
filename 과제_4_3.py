import requests

def get_random_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data)  # Add this line to check the received data
        return {
            'name': user_data['name'],
            'lat': float(user_data['address']['geo']['lat']),
            'lng': float(user_data['address']['geo']['lng']),
            'company': user_data['company']['name']
        }
    else:
        print(f"Failed to get data for user_id={user_id}. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    dummy_data = []

    for user_id in range(1, 11):
        user_info = get_random_user_data(user_id)
        if user_info is not None:
            lat, lng = user_info['lat'], user_info['lng']
            if -80 < lat < 80 and -80 < lng < 80:
                dummy_data.append(user_info)

    print(dummy_data)