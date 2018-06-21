#!/usr/bin/env python3


from flask import Flask, jsonify, render_template

import model


app = Flask(__name__)

@app.route("/lookup/<company_name>")
def serve_ticker_symbol(company_name):
	#return str(model.lookup_ticker_symbol(company_name))
	return render_template("lookup.html", \
				company_name=company_name, \
				ticker_symbol=model.lookup_ticker_symbol(company_name))

@app.route("/quote/<ticker_symbol>")
def serve_last_price(ticker_symbol):
	#return str(model.quote_last_price(ticker_symbol))
	return render_template("quote.html", \
				ticker_symbol=ticker_symbol, \
				last_price=model.quote_last_price(ticker_symbol))


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)
