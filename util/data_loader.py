import pandas as pd
import os

def load_all_data(data_dir):
    data = {}
    for key in ['users', 'properties', 'bookings', 'likes', 'reviews']:
        path = os.path.join(data_dir, f"{key}.csv")
        if os.path.exists(path):
            data[key] = pd.read_csv(path)
        else:
            data[key] = pd.DataFrame()
    return data