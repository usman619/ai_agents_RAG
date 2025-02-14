import os
import pandas as pd

population_path = os.path.join('data', 'world_population_23.csv')
population_df = pd.read_csv(population_path)

print(population_df.head())