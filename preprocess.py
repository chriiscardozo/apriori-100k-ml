import os

DIR='ml-100k'
MOVIE_FILE='u.item'
DATA_FILE='u.data'

def extract_movies_info():
	movies = {}
	f = open(os.path.join(DIR, MOVIE_FILE))
	for line in f:
		infos = line.split('|')
		movies[int(infos[0])] = infos[1]
	f.close()
	return movies

def extract_dataset():
	dataset = {}

	f = open(os.path.join(DIR, DATA_FILE))
	for line in f:
		infos = line.split('\t')

		user_id = int(infos[0])
		movie_id = int(infos[1])

		if user_id not in dataset:
			dataset[user_id] = []

		dataset[user_id].append(movie_id)

	f.close()
	return dataset
