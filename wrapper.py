import httpx

client = httpx.Client()
user_token = ""
base_url = "https://discordapp.com/api/v9"

class Wrapper:
    def set_token(token):
        global user_token
        user_token = token

    def get_token():
        global user_token
        return user_token

    def send_request(method, url, headers={}, data={}):
        return client.request(method, url, headers=headers, data=data)

    def send_discord_request(method, endpoint, headers={}, data={}):
        global user_token

        headers["Authorization"] = f"{user_token}"
        headers["Content-Type"] = "application/json"
        
        return client.request(method, base_url + endpoint, headers=headers, data=data)
