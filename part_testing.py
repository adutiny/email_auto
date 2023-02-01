import re
from typing import List, Any

#open the testing.txt file
with open('email.txt', 'r') as file:
    #read the file and extract the email addresses
    addresses = file.read().splitlines()


for address in addresses:
    result: list[Any] = re.findall(r'Email Address([^ ]*)', address)
    with open('email_sending.txt', 'a') as file:
        for result in result:
            file.write(str(result) + '\n')