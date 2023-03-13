import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException('Указаны одинаковые валюты.')

        try:
            quote_ticker, base_ticker = keys[quote], keys[base]
        except KeyError:
            raise APIException('Не удалось обработать одну из валют')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException('Не удалось обработать количество')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base