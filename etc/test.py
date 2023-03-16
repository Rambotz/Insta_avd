from urllib.parse import urlencode

import re

# url = "http://api.getsmscode.com/do.php?"

# payload = {
#     "action": "getmobile",
#     "username": "pay@noborders.net",
#     "token": "cfca2f0dd0be35a82de94e038ad2a7e8",
#     "pid": '8',
#     "cocode":'hk'
# }

# full_url = url + payload
# print(full_url)

# country_code =str(852)
# mobile_number = str(85265930975)
# pattern = "^" + re.escape(country_code)
# print(re.sub(pattern, "", mobile_number))
# import re

# message = "1|340 987 is your Instagram code. Don‘t share it. #ig"

# # Use regular expressions to extract the code
# match = message.split('|')
# message = match[1]
# code = re.search(r"\d{3}\s*\d{3}", message).group().replace(" ", "")
# print(code)
# if match:
#     code = match.group()
#     print(code)
# else:
#     print("Code not found in message.")
# from faker import Faker
# fake = Faker()
# name = fake.name()
# name_li = str(name).split(' ')
# fname = name_li[0]
# lname = name_li[-1]
# print(name,fname, lname)


# with open('accounts_cred/all_accounts.txt', 'a+') as f:
#     f.write('asdasdsdasd')
#     f.close()
import requests
url = "https://source.unsplash.com/random"

file_name = '/media/rk/0B29CA554279F37D/Workspace/New_Insta/AVD_setup-main/prof_img/Screenshot from 2023-01-27 18-15-07.png'
with open(file_name, "wb") as file:
    response = requests.get(url)
    file.write(response.content)
    