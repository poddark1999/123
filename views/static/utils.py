import requests
from models.bucket import Bucket
from datetime import datetime

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
	return f'{value:,.0f}'.replace(',', "'")

def format_date(value):
	if value is None:
		return '-'
	return value.strftime('%d/%m/%Y')

def format_comment(value):
	return value or '-'

def free_money_calculation(user, allocations, next_income):
    """
    Calculate the free money of a user.
    Params
    ------
		:param user: User for whom we want to calculate the free money.
		:type user: User
		:param allocations: List of allocations of the user.
		:type allocations: list
		:param next_income: Next income of the user.
		:type next_income: Income
  	
	Return
	------
		:return: Free money of the user.
		:rtype: float
   	"""
    free_money = user.balance
    for allocation in allocations:
        free_money -= allocation.amount
    while next_income.start_date < datetime.now():
        next_income.start_date += Bucket.valid_frequencies[next_income.frequency]
    free_money /= (next_income.start_date - datetime.now()).days
    return round(free_money, 2)

if __name__ == '__main__':
	print(convert(100, 'CHF', 'USD'))
