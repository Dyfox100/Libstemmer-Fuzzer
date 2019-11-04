import ctypes
from ctypes import util
import errno
import os
from multiprocessing import Process, Queue


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

    def _stem_word_and_get_error_number(self, word, queue):
        buffer = ctypes.create_string_buffer(len(word))
        buffer.value = bytes(word, 'utf-8')
        stemmed_word = self._stem_word(buffer, len(word))

        result = None
        #libstemmer returns NULL upon error, which is None in python.
        if stemmed_word == None:
            result = {}
            result[word] = "Stemming Returned Error No: " + str(ctypes.get_errno())
        queue.put(result)

    def test_word(self, word):
        queue = Queue()
        stem_process = Process(target=self._stem_word_and_get_error_number, args=(word, queue,))
        stem_process.start()
        stem_process.join()
        #stemming the word crashed the process. Report which signal caused crash
        proc_exit_code = stem_process.exitcode
        if proc_exit_code != 0:
            return {word: "Stemming Process Crashed with Signal: " + str(-proc_exit_code)}
        #stemming process finished, but errors maybe present in c errorno.
        else:
            return queue.get()

if __name__ == "__main__":
    libstemmer_harness_fpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "stem_word.so")
    harness = libstemmer_harness(libstemmer_harness_fpath)
    print(harness.test_word("testing"))
    print(harness.test_word("testing122222"))
