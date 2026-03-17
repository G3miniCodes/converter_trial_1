def train_model(data):
    print("Training Linear Regression Model...")
    
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(data[['x']], data['y'])
    
    return model
