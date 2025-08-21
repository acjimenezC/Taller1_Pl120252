import pandas as pd 
import json

df = pd.read_csv('movies_initial.csv', encoding='utf-8')

df.to_json('movies.json', orient='records', force_ascii=False)

with open('movies.json', 'r', encoding='utf-8') as file:
    movies = json.load(file)

for i in range(100): 
    movie = movies[i]
    print(movie)
    break