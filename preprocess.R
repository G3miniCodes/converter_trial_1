normalize <- function(column) {
  return((column - min(column)) / (max(column) - min(column)))
}
 
preprocess_data <- function(data) {
  cat("Preprocessing data...\n")
  
  data$x <- normalize(data$x)
  
  return(data)
}
