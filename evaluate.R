evaluate_model <- function(model, data) {
  cat("Evaluating model...\n")
  
  predictions <- predict(model, data)
  
  mse <- mean((predictions - data$y)^2)
  
  cat("Mean Squared Error:", mse, "\n")
}
