source("data_loader.R")
source("preprocess.R")
source("model.R")
source("evaluate.R")
 
cat("Starting ML Pipeline...\n")
 
data <- load_data()
 
processed <- preprocess_data(data)
 
model <- train_model(processed)
 
evaluate_model(model, processed)
