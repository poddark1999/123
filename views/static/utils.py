import requests

def convert(amount, from_currency, to_currency):
	params = {'apikey':'8DHHULP93X9V4YF',
			  'function':'CURRENCY_EXCHANGE_RATE',
			  'from_currency':from_currency,
			  'to_currency':to_currency}

	url = 'https://www.alphavantage.co/query'
	response = requests.get(url, params=params)
	data = response.json()
	rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
	return float(rate) * amount

def format_thousands(value):
    return f'{value:,}'.replace(',', "'")

def format_date(value):
    return value.strftime('%d/%m/%Y')

if __name__ == '__main__':
	print(convert(100, 'CHF', 'USD'))
