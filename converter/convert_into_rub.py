import osa
import math

def read_lines_from_file(input_path):
    with open(input_path) as input_file:
        return input_file.readlines()


def count_exp(input_path):
    url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.client.Client(url)
    sum_rub = 0
    file_lines = read_lines_from_file(input_path)
    for currency_line in file_lines:
        currency_amount = int(currency_line.split(" ")[1])
        currency_code = currency_line.split(" ")[2].strip()
        sum_rub += client.service.ConvertToNum(fromCurrency=currency_code, toCurrency='RUB', amount=currency_amount, rounding=True)
    print(math.ceil(sum_rub))
    return sum_rub

count_exp("/Users/crashover/PycharmProjects/Netology/converter/currencies.txt")