include mkinc.mak
CFLAGS=-O2 -Iinclude -fPIC
all: libstemmer.o

libstemmer.o: $(snowball_sources:.c=.o)
	$(AR) -cru $@ $^
	$(CC) -shared -o libstemmer.so -Wl,-force_load libstemmer.o -Wl,-noall_load

clean:
	rm -f src_c/*.o runtime/*.o libstemmer/*.o *.so *.o
