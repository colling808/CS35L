#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void error_msg();

int frobcmp(void const *a, void const *b);

int main(int argc, char **argv) {

  char ch;
  int nchars = 0, nwords = 0;
  char **words = malloc(nwords*sizeof(char*));
  char *new_word = malloc(nchars*sizeof(char));

  if (!words || !new_word)
    error_msg();
    
  
  while((ch = getchar()) != EOF) {

    /*case in which input is leading spaces*/
    if(ch == ' ' && nwords == 0 && nchars == 0) 
         continue;

    /*if space, separate word*/
    else if (ch == ' ' && nwords >= 0) {
    
      nchars++;
      new_word = realloc(new_word, nchars*sizeof(char));
      if(!new_word)
	error_msg();

      new_word[nchars - 1] = ch;
      nwords++;
      words = realloc(words, nwords*sizeof(char*));
      if(!words)
	error_msg();

      words[nwords - 1] = new_word;
      nchars = 0;
      char *tmp = malloc(nchars*sizeof(char));
      new_word = tmp;
    }

    /*otherwise, add char to new_word*/
    else {

      nchars++;
      new_word = realloc(new_word, nchars*sizeof(char*));

      if(!new_word)
	error_msg();
      
      new_word[nchars - 1] = ch;
    }
  
  }

  /*case where input does not end in ' ', append a space*/
  if(nwords != 0 && new_word[nchars - 1] != ' ') {

    nchars++;
    new_word = realloc(new_word, nchars*sizeof(char*));

    if(!new_word)
      error_msg();

    new_word[nchars - 1] = ' ';
    nwords++;
    words = realloc(words, nwords*sizeof(char*));

    if(!words) 
      error_msg();

    words[nwords - 1] = new_word;
  }
 

  /*sort words in array*/
  qsort(words, nwords, sizeof(char*), frobcmp);
  

  /*print words array*/
  int i, j;
  for(i = 0; i < nwords; i++) {
    for(j = 0; words[i][j] != ' '; j++)
      printf("%c", words[i][j]);
    printf("%c", words[i][j]);
      
  }
  

  if(words) {
     /* Free memory allocated by words array*/
    int i;
    for(i = 0; i < nwords; i++)
      free(words[i]);
    free(words);
   
  } 

   exit(0);
  
}

void error_msg() {

  fprintf(stderr, "Memory allocation error.\n");
  exit(1);
  
}

int frobcmp(void const *a, void const*b) {

  /*pointers to words being compared*/
  const char *p1 = *((const char**) a);
  const char *p2 = *((const char**) b);
  
  int i1 = 0, i2 = 0;

  while (p1[i1] != ' ' && p2[i2] != ' ' && p1[i1] == p2[i2]) {
    i1++;
    i2++;
  }

  /*compare first two chars that aren't the same*/
  const char c1 = p1[i1];
  const char c2 = p2[i2];
  
  /*case that they are exact same word*/
  if (c1 == ' ' && c2 == ' ')
    return 0;
  else 
    return (c1 ^ 42) - (c2 ^ 42);
  
}
