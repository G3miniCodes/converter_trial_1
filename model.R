train_model <- function(data) {
  cat("Training Linear Regression Model...\n")
  
  model <- lm(y ~ x, data=data)
  
  return(model)
}
