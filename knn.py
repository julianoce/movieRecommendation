import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors



#aqui a gente pega o ratings dos usuarios
movie_columns = ['user_id', 'movie_id', 'rating']

ratings = pd.read_csv('u.data', sep='\t', names=movie_columns, usecols=range(3))

#aqui a gente vai agrupar os filmes
movieGroup = ratings.groupby('movie_id')
movie_rating_counts = movieGroup.agg({'rating': [np.size, np.mean]})
movieNumRatings = pd.DataFrame(movie_rating_counts['rating']['size'])

movieDict = {}
with open('u.item', mode='r', encoding='UTF-8') as f:
    temp = ''

    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = list(map(int, genres))
        movieDict[movieID] = (name, genres, movieNumRatings.get('size'),
                              movie_rating_counts.get('mean'))
