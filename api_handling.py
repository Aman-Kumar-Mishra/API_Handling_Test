#API handling with python
import requests
import json

#method for fetching data from API
def fetch_userdata():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    try:
        response = requests.get(url)
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise Exception("failed to decode JSON from API response!")
        if data['success'] and 'data' in data:
            api_file = 'api.txt'
            try:
                with open(api_file, 'r') as file:
                    json.load(file)
            except FileNotFoundError:
                print("new file created!")


            with open(api_file, 'w') as file:
                json.dump(data, file)

            username = data['data']['login']['username']
            country = data['data']['location']['country']
            return  username, country
        else:
            raise Exception("failed to get the response from API!")
    except Exception as e:
        print(f"an error occured: {e}")

def main():
    try:
        #calling method for fetching data from API
        username, country = fetch_userdata()
        print(f"username: {username}\ncountry: {country}")
    except TypeError:
        raise Exception("failed to return values!")


if __name__ == '__main__':
    main()

