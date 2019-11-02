all:
	cp libstemmer_makefile libstemmer_c/Makefile
	cd libstemmer_c && $(MAKE)
clean:
	cd libstemmer_c && $(MAKE) clean
