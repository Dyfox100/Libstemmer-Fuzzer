#include <stdio.h>
#include <stdlib.h>


#include "../libstemmer_c/include/libstemmer.h"


unsigned char * stem_word(unsigned char * word, int length){

  struct sb_stemmer * stemmer;
  char * language = "english";
  char * charenc = NULL;
  unsigned char * stemmed_word = malloc(sizeof(unsigned char*) * length);

  stemmer = sb_stemmer_new(language, charenc);

  if (stemmer == 0){
    fprintf(stderr, "Error in english stemmer creation");
    exit(1);
  }

  stemmed_word = sb_stemmer_stem(stemmer, word, length);
  return stemmed_word;
}
