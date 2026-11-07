import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    unbanned = users[users['banned'] == 'No']['users_id']

    trips = trips[
        trips['client_id'].isin(unbanned) &
        trips['driver_id'].isin(unbanned)
    ]

    trips = trips[
        trips['request_at'].between('2013-10-01', '2013-10-03')
    ].copy()

    trips['cancelled'] = (trips['status'] != 'completed').astype(int)

    results = (
        trips.groupby('request_at')['cancelled']
        .mean()
        .round(2)
        .reset_index()
    )

    results.columns = ['Day', 'Cancellation Rate']

    return results