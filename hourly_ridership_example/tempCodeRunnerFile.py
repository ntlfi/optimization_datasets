grouped = df.groupby(["station_id"]).sum()
grouped.reset_index(inplace=True)