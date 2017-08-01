import pickle

def crea_pickle(data, file):
	pickle_output = open(file, 'wb')
	# Pickle dictionary using protocol 0.
	pickle.dump(data, pickle_output)
	pickle_output.close()