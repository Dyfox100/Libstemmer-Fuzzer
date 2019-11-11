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

    def _stem_word_and_get_error_number(self, word, result, queue):
        buffer = ctypes.create_string_buffer(len(word))
        buffer.value = word
        result[word]['stemmed_word'] = self._stem_word(buffer, len(word))
        #Libstemmer couldn't stem word, check for C Error Number.
        if result[word]['stemmed_word'] == b"":
            result[word]["C_error_number"] = ctypes.get_errno()

        queue.put(result)

    def test_word(self, word):
        queue = Queue()
        result = {
            word:{
                "stemmed_word": "",
                "C_error_number": 0,
                "process_exit_code": 0
                }
        }
        stem_process = Process(target=self._stem_word_and_get_error_number, args=(word, result, queue,))
        stem_process.start()
        stem_process.join()
        #If stemming the word crashed the process, exit code will not equal 0.
        #So create ad hoc error report
        proc_exit_code = stem_process.exitcode
        if proc_exit_code != 0:
            result[word]['process_exit_code'] = -proc_exit_code
            return result
        else:
            return queue.get()

if __name__ == "__main__":
    libstemmer_harness_fpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "stem_word.so")
    harness = libstemmer_harness(libstemmer_harness_fpath)
    print(harness.test_word(b"\x54\x65\x73\x74\x69\x6e\x67"))
    print(harness.test_word(b"\x00\x00\x00\x17"))
