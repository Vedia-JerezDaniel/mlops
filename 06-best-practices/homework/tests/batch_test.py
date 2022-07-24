import pandas as pd
from datetime import datetime

def dt(hour, minute, second=0):
    return datetime(2021, 1, 1, hour, minute, second)

data = [
    (None, None, dt(1, 2), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, 1, dt(1, 2, 0), dt(1, 2, 50)),
    (1, 1, dt(1, 2, 0), dt(2, 2, 1)),        
]

columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
df = pd.DataFrame(data, columns=columns)

df


df.to_parquet(
    'q3.parquet',
    engine='pyarrow',
    compression=None,
    index=False,
    # storage_options=options
)

options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
    }
}