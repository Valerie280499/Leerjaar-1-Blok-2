import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)


'''
import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

dit mosse in un niej bestand zetten.
alse dan ein print van de data duis kriegse de dictionary dea in dit bestand steit
de mos er wal veur zurge desse dit bestand iers oetvoers um un data.pickle aan te maken


'''
