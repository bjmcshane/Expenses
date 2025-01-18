import pandas as pd
# import numpy as np
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime

columns=[
    'year', 'month', 'date',
    'money_spent_on_eating_out', 'money_spent_on_groceries', 'money_spent_entertainment_alcohol',
    'money_put_towards_retirement', 'money_saved_for_retirement', 'money_put_towards_house', 'money_saved_for_house', 'money_put_towards_portfolio', 'money_saved_in_portfolio'
]


def new_month():
    date = datetime.datetime.today()
    year, month = date.year, date.month
    if input("Enter `Y` if you're logging finances for the previous month") in ("Y", 'y'):
        month -= 1

    row = {
        "year": date.year,
        "month": date.month,
        "date": date,
        "money_spent_eating_out": int(input("How much did you spend eating out? ")),
        "money_on_groceries": int(input("How much did you spend on groceries? ")),
        "money_spent_on_entertainment_alcohol": int(input("How much did you spend on entertainment/alcohol? ")),
        "month_put_towards_retirement": int(input("How much did you put away for your retirement? (Currently automated @ 105/paycheck) ")),
        "money_saved_for_retirement": int(input("How much do you currently have saved for retirement? ")),
        "money_put_towards_house": int(input("How much money did you put towards your first house? ")),
        "money_saved_towards_house": int(input("How much do you currently have saved for a house? ")),
        "money_put_towards_portfolio": int(input("How much did you put towards your portfolio? ")),
        "money_saved_in_portfolio": int(input("How much is your portfolio currently worth? ")),
    }

    pd.concat(
        [pd.read_csv("data.csv"), pd.DataFrame(row)],
        axis=0,
        ignore_index=True
    ).to_csv("data.csv", index=False)

def generate_dummy_data():
    df = pd.DataFrame(columns=columns)
    for row in [
        [2025, 1, "2025-01-31",  200, 400, 100, 420, 10000, 1200, 10000, 100, 500],
        [2025, 2, "2025-02-28",  150, 350, 80, 420, 10420, 1200, 11200, 100, 600],
        [2025, 3, "2025-03-31",  250, 250, 200, 420, 10840, 1200, 12400, 100, 700],
        [2025, 4, "2025-04-30",  320, 300, 50, 420, 11080, 1200, 13600, 100, 800],
        [2025, 5, "2025-05-31",  100, 150, 150, 420, 11500, 1200, 14800, 100, 900],
    ]:
        temp = {}
        for val, col in zip(row, columns):
            temp[col] = [val]

        df = pd.concat(
            [df, pd.DataFrame(temp)], axis=0, ignore_index=True
        )
    df.to_csv('dummy_data.csv', index=False)


if __name__ == "__main__":
    new_month()