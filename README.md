# Libstemmer-Fuzzer
A fuzzer in Python to attack the C implementation of the Snowball Stemming Module (Libstemmer.c).

This fuzzer either generates random malformed byte sequences, then passes them to the stemming module as if they were UTF8 encoded strings, or it can generate random sequences of valid english UTF8 characters. 

# Requirements:
1. Python 3
2. C compiler
3. libstemmer C source code. See instructions below.

# Compilation Instructions:
1. Clone this repo.
2. Download the libstemmer C source code from: (http://snowball.tartarus.org/download.html).
3. Extract the libstemmer_c tarball into the top level folder of this repo. The name needs to be "libstemmer_c" Ex. Your source code for libstemmer_c should reside in Libstemmer-Fuzzer/libstemmer_c/
4. Run "make" at the top level directory. 

# Execution Instructions:
1. Execute the command "python3 fuzz_libstemmer.py <number_random_strings_to_fuzz> <length_fuzzing_string> <strategy_for_chracter_generation>. These arguments are mandatory. The strategy argument should either be "E" for correctly formed english characters, or "M" for malformed input. The fuzzer also takes optional arguements of <-o output_file_path> and <--v>. The --v flag specifies verbose output. By default the fuzzer will only log errors, but with the verbose flag, it logs each string it stems, whether or not an error is encountered. Note: I've executed both strategies quite a few times and haven't seen any errors, so it's recommend to use the --v flag the first time or two you run it to ensure everything is working correctly.
2. If you specified a log file, the logs from the fuzzing run will be stored there. If not, the defualt log location is "logs/fuzz_logs_<timestamp>.txt. The logs are stored in a three column delimited text form. Because the strings that are tested are randomly generated, the delimiters are "\t,,\t". This is done so that random strings that contain a comma or other commonly used seperator won't throw off the file structure. The chances of a random string having the exact sequence of "\t,,\t" is quite low. 
