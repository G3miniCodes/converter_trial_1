def evaluate_model(model, data):
    print("Evaluating model...")
    predictions = model.predict(data)
    mse = ((predictions - data['y']) ** 2).mean()
    print("Mean Squared Error:", mse)
