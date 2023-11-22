from bs4 import BeautifulSoup
import requests

# List of query words
query_texts = [
"旅順",
"促して",
"蒲鉾",
"女連",
"結城紬",
"所々",
"師走",
"ポカポカ殴る",
"べんべら",
"年の暮れ",
"羽織",
"紋付羽織",
"転じる",
"偏屈",
"格子",
"迂遠",
"傍らに",
"端書",
"春着",
"エピクテタス",
"詰腹",
"突きつける",
"顧みる",
"対句",
"でんぷん質",
"死骸",
"焦げ爛れた",
"代えて",
"雑煮",
"お櫃",
"甞める",
"吹聴",
"仕付",
"間食"
]

# Iterate over the query words
for i in range(len(query_texts)):
    url = "https://www.weblio.jp/content/" + query_texts[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the main content div
    content_div = soup.find('div', class_='kijiWrp')
    try:
        # Extract the text from the content div
        content_text = content_div.get_text()

        print(content_text)

    except:
        print(query_texts[i]+"not found")
