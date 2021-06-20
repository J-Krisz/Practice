import requests
from bs4 import BeautifulSoup

URL = "https://projecteuler.net/problem="

for url in range(101):

	page = requests.get(URL + str(url))
	content = page.content
	soup = BeautifulSoup(content, "html.parser")

	number = soup.find("h3")
	title = soup.find("h2").text
	text = soup.find("p").text

	if number is None:
		continue
	else:
		with open(f"{number.text} - {title}.py", "w") as file:
			file.write(f'"""{text}"""')




