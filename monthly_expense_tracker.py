import pandas as pd
# import numpy as np
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import calendar

columns=[
    'year', 'month', 'date',
    'money_spent_on_eating_out', 'money_spent_on_groceries', 'money_spent_entertainment_alcohol',
    'money_put_towards_retirement', 'money_saved_for_retirement', 'money_put_towards_house', 'money_saved_for_house', 'money_put_towards_portfolio', 'money_saved_in_portfolio'
]


def get_validated_input(prompt, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Please enter a value >= {min_value}")
        except ValueError:
            print("Please enter a valid number")

def new_month():
    date = datetime.datetime.today()
    year, month = date.year, date.month

    if input("Enter 'Y' if you're logging finances for the previous month: ").lower() == 'y':
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1

    prompts = {
        'money_spent_on_eating_out': "How much did you spend eating out? ",
        'money_spent_on_groceries': "How much did you spend on groceries? ",
        'money_spent_entertainment_alcohol': "How much did you spend on entertainment/alcohol? ",
        'money_put_towards_retirement': "How much did you put away for retirement? (Currently automated @ 105/paycheck) ",
        'money_saved_for_retirement': "How much do you currently have saved for retirement? ",
        'money_put_towards_house': "How much money did you put towards your first house? ",
        'money_saved_for_house': "How much do you currently have saved for a house? ",
        'money_put_towards_portfolio': "How much did you put towards your portfolio? ",
        'money_saved_in_portfolio': "How much is your portfolio currently worth? "
    }

    row = {
        'year': year,
        'month': month,
        'date': datetime.datetime(year, month, 1).date()
    }
    
    # Get all expense inputs with validation
    row.update({field: get_validated_input(prompt) for field, prompt in prompts.items()})
    
    # Read existing data and append new row
    try:
        df = pd.read_csv("data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=columns)
    
    pd.concat([df, pd.DataFrame([row])], ignore_index=True).to_csv("data.csv", index=False)

def generate_dummy_data():
    # Create the data as a list of dictionaries - more straightforward than creating temp dictionaries
    data = [
        {
            'year': 2025,
            'month': month,
            'date': f'2025-{month:02d}-{calendar.monthrange(2025, month)[1]}',
            'money_spent_on_eating_out': [200, 150, 250, 320, 100][month-1],
            'money_spent_on_groceries': [400, 350, 250, 300, 150][month-1],
            'money_spent_entertainment_alcohol': [100, 80, 200, 50, 150][month-1],
            'money_put_towards_retirement': 420,
            'money_saved_for_retirement': 10000 + (420 * (month-1)),
            'money_put_towards_house': 1200,
            'money_saved_for_house': 10000 + (1200 * (month-1)),
            'money_put_towards_portfolio': 100,
            'money_saved_in_portfolio': 500 + (100 * (month-1))
        }
        for month in range(1, 6)
    ]
    
    # Create DataFrame directly from list of dictionaries and save
    pd.DataFrame(data).to_csv('dummy_data.csv', index=False)


if __name__ == "__main__":
    new_month()
