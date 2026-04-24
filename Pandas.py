
import kagglehub


df = kagglehub.dataset_download("artheon/pulse-2026-music-evolution-and-viral-analytics")

import pandas as pd 

data=pd.read_csv('Music_Evolution_2026_Pulse.csv')
print(data.head(5))

print(data.describe())

print(data.shape)