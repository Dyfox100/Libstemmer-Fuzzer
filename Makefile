all:
	cp libstemmer_makefile libstemmer_c/Makefile
	cd libstemmer_c && $(MAKE)
	cd harness && $(MAKE)
clean:
	cd libstemmer_c && $(MAKE) clean
	cd harness && $(MAKE) clean
