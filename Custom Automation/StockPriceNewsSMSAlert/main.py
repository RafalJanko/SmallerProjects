import requests
from datetime import date, timedelta
from newsapi import NewsApiClient
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "YOUR API"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
YESTERDAY = str(date.today() - timedelta(days=2))
DAY_BEFORE = str(date.today() - timedelta(days=3))
News_password = "YOUR PASSWROD"
NEWS_API = "YOUR API"
TWILIO_SID = "ACd04fc9e647f3665005608650236a3c22"
TWILIO_PASS = "YOUR PASSWORD"
TWILIO_AUTH_CODE = "YOUR CODE"

stocks_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API
}

response = requests.get(STOCK_ENDPOINT, params=stocks_params)
response.raise_for_status()
stock_data = response.json()

yesterday_stock_slice = stock_data["Time Series (Daily)"][YESTERDAY]["4. close"]
f_yesterday = float(yesterday_stock_slice)

day_before_stock_slice = stock_data["Time Series (Daily)"][DAY_BEFORE]["4. close"]
f_day_before_slice = float(day_before_stock_slice)

yesterdays_difference = (f_yesterday - f_day_before_slice)
updown = None
if yesterdays_difference > 0:
    updown = "🔺"
else:
    updown ="🔻"

percentage_difference_yesterday_day_before = round((f_yesterday - f_day_before_slice) / f_day_before_slice * 100)

news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME,
}

if abs(percentage_difference_yesterday_day_before) > 0.0001:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles_list = [f"{STOCK_NAME}{updown}{percentage_difference_yesterday_day_before}%\nHeadline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_CODE)
    for article in formatted_articles_list:
        message = client.messages.create(
            body=article,
            from_='YOUR SMS SERVICE PROVIDER NUMBER',
            to='YOUR PHONE NUMBER'
        )


