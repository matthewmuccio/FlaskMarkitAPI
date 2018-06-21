#!/usr/bin/env python3


import json

import requests


def lookup_ticker_symbol(company_name):
	endpoint = "http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input="
	return json.loads(requests.get(endpoint + company_name).text)[0]["Symbol"]

def quote_last_price(ticker_symbol):
	endpoint = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
	return json.loads(requests.get(endpoint + ticker_symbol).text)["LastPrice"]


if __name__ == "__main__":
	# Tests
	print(lookup_ticker_symbol("tesla"))
	print(quote_last_price("tsla"))
