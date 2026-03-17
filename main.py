import data_loader
import preprocess
import model
import evaluate

print("Starting ML Pipeline...")

data = data_loader.load_data()

processed = preprocess.preprocess_data(data)

model = model.train_model(processed)

evaluate.evaluate_model(model, processed)
