import requests
import re

result = requests.get("https://www.baidu.com")
print(result.status_code)
print(result.cookies)

