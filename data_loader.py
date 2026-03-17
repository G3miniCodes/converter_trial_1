import numpy as np
import pandas as pd
from utils import log_message


def load_data():
    print("Loading synthetic dataset...")
    
    x = np.random.normal(size=100)
    y = 2 * x + np.random.normal(size=100)
    
    data = pd.DataFrame({'x': x, 'y': y})
    
    log_message("Data loaded successfully")
    
    return data

if __name__ == "__main__":
    load_data()
