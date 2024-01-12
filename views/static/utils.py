import requests
from models.bucket import Bucket
from datetime import datetime

def convert(amount, from_currency, to_currency):
	"""
	Converts an amount from a currency to another.
	
	Params
	------
		:param amount: Amount to convert.
		:type amount: float
		:param from_currency: Currency to convert from.
		:type from_currency: str
		:param to_currency: Currency to convert to.
		:type to_currency: str
	
	Return
	------
		:return: Converted amount.
		:rtype: float
	"""
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
	"""
    Display the number with a specific format for thousands.
    
    Params
    ------
    	:param value: Value to format.
		:type value: float
  	
  	Return
  	------
  		:return: Formatted value.
  		:rtype: str
    """
	return f'{value:,.0f}'.replace(',', "'")

def format_date(value):
	"""
    Display the date with a specific format.
    
    Params
    ------
		:param value: Value to format.
		:type value: datetime
  	
  	Return
  	------
  		:return: Formatted value.
  		:rtype: str"""
	if value is None:
		return '-'
	return value.strftime('%d/%m/%Y')

def format_comment(value):
	"""
    Display '-' when there is no comment.
    
    Params
    ------
		:param value: Value to format.
		:type value: str
  	
  	Return
  	------
  		:return: Formatted value.
  		:rtype: str
    """
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
	free_money = float(user.balance)
	for allocation in allocations:
		free_money -= allocation.amount
	if not next_income:
		return round(free_money/30,2)
	while next_income.start_date < datetime.now():
		next_income.start_date += Bucket.valid_frequencies[next_income.frequency]
	if (next_income.start_date - datetime.now()).days:
		free_money /= (next_income.start_date - datetime.now()).days
	return round(free_money, 2)

if __name__ == '__main__':
	print(convert(100, 'CHF', 'USD'))
