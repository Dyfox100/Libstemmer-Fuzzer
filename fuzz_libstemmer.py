import os
import argparse
from datetime import datetime
import json

from harness.harness import libstemmer_harness
from fuzzer.fuzzer_base_class.string_fuzzer import String_Fuzzer
from fuzzer.fuzzing_strategies.english_valid_UTF8_strategy import English_Valid_UTF8_Strategy
from fuzzer.fuzzing_strategies.random_non_valid_utf8 import Random_Non_Valid_UTF8_Strategy


def main(num_runs, length_string, strategy, output, verbose):
    libstemmer_harness_fpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "harness/stem_word.so")
    harness = libstemmer_harness(libstemmer_harness_fpath)

    result_file = open(output, 'w+')
    result_file.write('String,C_Error_Number,Process_Exit_Code')

    try:
        fuzzing_strategy = None
        if strategy == 'E':
            fuzzing_strategy = English_Valid_UTF8_Strategy()
        elif strategy == 'M':
            fuzzing_strategy = Random_Non_Valid_UTF8_Strategy()

        fuzzer = String_Fuzzer(fuzzing_strategy)

        for __ in range(num_runs):
            word = fuzzer.generate_fuzzy_string(length_string)
            fuzz_result = harness.test_word(word)
            if verbose:
                result_file.write()
            else:
                if fuzz_result[word]["C_error_number"] != 0 or fuzz_result[word]["process_exit_code"] != 0:
                    result_file.write(word.decode('utf-8', 'backslashreplace') + ',' + str(fuzz_result[word]["C_error_number"]) + ',' + str(fuzz_result[word]["process_exit_code"]) )

    except Exception as e:
        result_file.close()
        raise(e)

    result_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Libstemmer Fuzzer')
    parser.add_argument('num_runs',type=int, help='Number of Random Strings To Test')
    parser.add_argument('length_string', type=int, help='Length of Random String To Test')
    parser.add_argument('strategy', choices=['E', 'M'], help='Strategy to fuzz with, either E for english valid utf8 or M for malformed utf8')
    parser.add_argument('-output', help='output file location', default=None)
    parser.add_argument('--v', action='store_true', help='Verbose, output all results, not just errors')


    args = parser.parse_args()

    if args.output == None:
        args.output = 'fuzz_logs_' + datetime.now().strftime("%m-%d-%Y,%H:%M:%S") + '.txt'

    main(args.num_runs, args.length_string, args.strategy, args.output, args.v)
