import ctypes
from ctypes import util
import errno
import os
from multiprocessing import Process


class libstemmer_harness():

    def __init__(self, harness_file_path):

        if not os.path.isfile(harness_file_path):
            raise(FileNotFoundError(
                errno.ENOENT, "C Test Harness .so file does not exist, or it's path is invalid."
                + " Maybe run make at the top level? File name", harness_file))
        #libstemmer harness function ctypes definition
        self._libstemmer_functions = ctypes.CDLL(harness_file_path, use_errno=True)
        self._stem_word = self._libstemmer_functions.stem_word
        self._stem_word.argtypes = [ctypes.c_char_p]
        self._stem_word.restype = ctypes.c_char_p

    def stem_word_and_get_error_number(self, word):
        buffer = ctypes.create_string_buffer(len(word))
        buffer.value = bytes(word, 'utf-8')

        _result = self._stem_word(buffer, len(word))

        result = {}
        if _result == None:
            result[word] = ctypes.get_errno()
        return result

if __name__ == "__main__":
    libstemmer_harness_fpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "stem_word.so")
    harness = libstemmer_harness(libstemmer_harness_fpath)
    print(harness.stem_word_and_get_error_number("testing"))
