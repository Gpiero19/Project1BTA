from FileManager import FileManager
from HistoryMessages import HistoryMessages
import json
import requests

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        with open(self.hist_file_path, "a") as file:
            json.dumps(hist_dict)
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
    
        # self.file_manager 

    def get_exchange_rates(self):
        # Implement a process that sends a get request to the link 
        # and returns the resulting dictionary. 
        response = requests.get(LINK)
        if response.status_code == 200:
            exchange_rates = response.json()
            return exchange_rates
        else:
            print("Exchange rates not found")
            return None
    
    def exchange_currency(self, currency_from, currency_to, amount):
        # in case of a negative outcome, the history entry looks like this
        # - if currency_from or currency_to is specified incorrectly
        # - if amount is not a number
        # history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
        # self.write_to_history(history_message)

        try:
            amount = float(amount)

        except ValueError:
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None
        
        if currency_from not in self.exchange_rates or currency_to not in self.exchange_rates:
            # Log failure to history and return None if either currency is not supported
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None
        
        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency

        # with a positive outcome, the record of history looks like this 
        # history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        # self.write_to_history(history_message)

        converted_amount = amount / self.exchange_rates[currency_from] * self.exchange_rates[currency_to]
        history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        self.write_to_history(history_message)
        return converted_amount        