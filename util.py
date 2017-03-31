import os

RESULTS_FOLDER='results'

def save_csv(itemset, filename):
	output = ''
	for i in itemset:
		output += ','.join(str(s) for s in i[1])
		output += '\n'

	f = open(filename, 'w')
	f.write(output)
	f.close()

def get_films_id_from_output(s):
	tmp = s[s.index('(')+1:s.index(')')]
	if tmp[-1] == ',': tmp = tmp[:-1]
	return [int(x.split('\'')[1]) for x in tmp.split(',')]

def save_result_apriori(movies, txt, support, confidence):
	final_str = ''
	lines = txt[txt.index('RULES')+7:len(txt)-1].split('\n')
	if(lines[0] == ''): return

	for line in lines:
		aux = line.split(' , ')
		confidence_value = aux[1]

		aux = aux[0].split(' ==> ')
		A = get_films_id_from_output(aux[0])
		B = get_films_id_from_output(aux[1])

		movies_A = ''
		movies_B = ''
		for i in A: movies_A += movies[i] + ','
		for i in B: movies_B += movies[i] + ','
		movies_A = movies_A[:-1]
		movies_B = movies_B[:-1]

		final_str = movies_A + ';' + movies_B + ';' + confidence_value + '\n' + final_str


	f = open(os.path.join(RESULTS_FOLDER, 'apriori_' + str(support) + '_' + str(confidence) + '.csv'), 'w')
	f.write(final_str)
	f.close()

	print final_str
		