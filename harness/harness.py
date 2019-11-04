import ctypes
from os import path

class libstemmer_harness():

    def __init__(self, libstemmer_file_path):
        if not path.exists(libstemmer_file_path):
            raise("Libstemmer File Path Invalid!")
        self._libstemmer_functions = ctypes.CDLL(libstemmer_file_path)
        self._stemmer = self._libstemmer_functions.sb_stemmer_new("english", None)
        self._libstemmer_functions.sb_stemmer_new.restype = ctypes.c_char_p

    def stem_word(self, word):
        self._buffer = ctypes.create_string_buffer(len(word))
        self._buffer.value = bytes(word, 'utf-8')
        self._libstemmer_functions.sb_stemmer_stem(self._stemmer, self._buffer, len(word))

if __name__ == "__main__":
    harness = libstemmer_harness("../libstemmer_c/libstemmer.so")
    harness.stem_word("testing")
