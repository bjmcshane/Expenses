import pandas as pd
# import numpy as np
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


if __name__ == "__main__":
    columns=[
        'year', 'month', 'date', 'money_put_towards_retirement', 'money_saved_for_retirement', 'money_put_towards_house', 'money_saved_for_house', 'money_put_towards_portfolio',
        'money_saved_in_portfolio'
    ]
    df = pd.DataFrame(columns=columns)
    for row in [
        [2025, 1, "2025-01-31",  420, 10000, 1200, 10000, 100, 500],
        [2025, 2, "2025-02-28",  420, 10420, 1200, 11200, 100, 600],
        [2025, 3, "2025-03-31",  420, 10840, 1200, 12400, 100, 700],
        [2025, 4, "2025-04-30",  420, 11080, 1200, 13600, 100, 800],
        [2025, 5, "2025-05-31",  420, 11500, 1200, 14800, 100, 900],
    ]:
        temp = {}
        for val, col in zip(row, columns):
            temp[col] = [val]

        df = pd.concat(
            [df, pd.DataFrame(temp)], axis=0, ignore_index=True
        )
    df.to_csv('dummy_data.csv', index=False)
    print(df.head())