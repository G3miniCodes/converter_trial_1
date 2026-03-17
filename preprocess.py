def normalize(column):
    return (column - min(column)) / (max(column) - min(column))


def preprocess_data(data):
    print("Preprocessing data...")
    data['x'] = normalize(data['x'])
    return data
