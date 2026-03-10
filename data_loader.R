source("utils.R")
 
load_data <- function() {
  cat("Loading synthetic dataset...\n")
  
  x <- rnorm(100)
  y <- 2 * x + rnorm(100)
  
  data <- data.frame(x, y)
  
  log_message("Data loaded successfully")
  
  return(data)
}
