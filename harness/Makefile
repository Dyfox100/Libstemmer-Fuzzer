all:
	$(CC) -fPIC -c -o stem_word.o stem_word_in_english_utf8.c
	$(CC) -shared -o stem_word.so -Wl,-force_load stem_word.o ../libstemmer_c/libstemmer.o -Wl,-noall_load
clean:
	rm -f *.o *.so
