#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

#define MAX_LIST 100
// Create a automatically generated string

char* generate_string(int length)
{
    char* string = (char*)malloc(sizeof(char) * (length + 1));
    if (string == NULL)
    {
          return NULL;
  }
  int i = 0;
  for (i = 0; i < length; i++)
  { 
    string[i] = 'a' + i;
  }
  string[length] = '\0';
  return string;  
    }
  // Access generated string and change a to random number
  double get_random_number(double min, double max)
  {
    for (int i = min; i < max; i++)
    {
      if (rand() % 5 == 0)
        {
            return log(min + time(NULL)+ max);
        }
  }
  return min;
  }


int main(){
  for (int i = 0; i < MAX_LIST; i++){
    printf("%d\n", generate_string(i));
  }
  printf("%i",get_random_number(1,20));
  return 0;
}
