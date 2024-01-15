import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import modules.load_utils as loader
import modules.plot_utils as plotter
import modules.train_utils as trainer

# Rest of your code

data = loader.load_csv("titanic/train.csv")

print(data.head())