import requests
from datetime import datetime


class Message:
  def __init__(self, month, day):
    self.month = month
    self.day = day

  def quote_of_today(self):
    """Returns the quote related to today's date."""
    date_quote = requests.get(f"http://numbersapi.com/{self.month}/{self.day}/date").text
    return date_quote

  def random_math_quote(self):
    """Returns the random maths quote."""
    math_quote = requests.get(f"http://numbersapi.com/random/math").text
    return math_quote


if __name__ == "__main__":
  today = datetime.now()
  message = Message(today.month, today.day)
  print(message.random_math_quote())
