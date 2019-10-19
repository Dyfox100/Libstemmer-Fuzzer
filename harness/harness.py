import ctypes
from os import path

class libstemmer_harness():

    def __init__(self, libstemmer_file_path):
        if not path.exists(libstemmer_file_path):
            raise("Libstemmer File Path Invalid!")
        self._libstemmer_functions = ctypes.CDLL(libstemmer_file_path)
        self._stemmer = _libstemmer_functions.sb_stemmer_new("english", None)


    def stem_word(word):
        raise("Not Implemented")

if __name__ == "__main__":
    libstemmer_harness("../../libstemmer_c/libstemmer.so")
