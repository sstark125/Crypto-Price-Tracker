from bs4 import BeautifulSoup
import requests
import re
import urllib3
import os
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')
ConsoleClear()



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://coinmarketcap.com/"
result = requests.get(url, verify=False)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price


for coin, price in prices.items():
    print(f"{coin}: {price}")














# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all("input", type="text")
# for tag in tags:
#     tag['placeholder'] = "I changed you!"

# with open("changed.html", "w") as file:
#     file.write(str(doc))








# tags = doc.find_all(text = re.compile("\$.*"), limit=1)



















# # Get Website URL and set info to a variable
# url = 'https://www.newegg.com/gigabyte-geforce-rtx-4060-ti-gv-n406teagle-8gd/p/N82E16814932620?Description=gpu&cm_re=gpu-_-14-932-620-_-Product&quicklink=true'
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # 2. Set the results of the website to a variable
# result = requests.get(url, verify=False)

# # 3. Turn variable into text
# doc = BeautifulSoup(result.text, "html.parser")


# prices = doc.find_all(string = "$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)






