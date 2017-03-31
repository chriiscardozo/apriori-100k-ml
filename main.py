import preprocess as pp
import apriori
import util
import subprocess
import sys

ITEMSET_FILE='itemset.csv'

min_support=0.5
min_confidence=0.7

def run_apriori(min_support, min_confidence):
	command = 'python apriori.py -f ' + ITEMSET_FILE + ' -s ' + str(min_support) + ' -c ' + str(min_confidence)
	
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	output = proc.stdout.read()

	return output

def main():
	if(len(sys.argv) == 3):
		min_support=float(sys.argv[1])
		min_confidence=float(sys.argv[2])
	else:
		min_support=0.5
		min_confidence=0.7

	movies = pp.extract_movies_info()
	dataset = pp.extract_dataset()
	itemset = dataset.items()

	util.save_csv(itemset, ITEMSET_FILE)
	output = run_apriori(min_support, min_confidence)
	util.save_result_apriori(movies, output, min_support, min_confidence)

main()