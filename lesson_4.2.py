from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates(code):
    stroka = content.split('<Valute ID=')
    for i in stroka:
        if code.upper() in i:
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))

print(currency_rates("usd"))