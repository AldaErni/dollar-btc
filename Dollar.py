import requests
from bs4 import BeautifulSoup

DOLLAR_BT = 'https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&sxsrf=ALiCzsYJuTI5VmDHrabh98YmhXjyJyyDug%3A1656480868895&ei=ZOS7YuOlNozQqwGOw5PwDg&oq=%2Cbnrjby+d&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgQIABBDMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKOgQILhAnOgoILhDHARDRAxAnOgQIIxAnOgsIABCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6BQgAEIAEOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIAEEMcBENEDOgoILhDHARDRAxBDOgsIABCABBAKEAEQKjoJCAAQgAQQChABOgcIABCABBAKOgoIABCxAxCDARAKOgcIABCxAxAKSgQIQRgASgQIRhgAUABYog5ghiFoAHABeACAAYgBiAHdCJIBAzAuOZgBAKABAcABAQ&sclient=gws-wiz-serp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

full_page = requests.get(DOLLAR_BT, headers=headers)

#print(full_page.content)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "pclqee"})
print(convert)