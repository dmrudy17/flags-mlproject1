import numpy as np
import pandas as pd

input_file = "agaricus-lepiota.data"

mushrooms = pd.read_csv(input_file, header=None)

print(mushrooms)