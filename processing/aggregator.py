def hourly_averages(df):
    df['hour'] = df['timestamp'].dt.floor('H')
    hourly_avg = df.groupby('hour')['value'].mean().reset_index()
    hourly_avg.columns = ['timestamp', 'average']
    return hourly_avg
