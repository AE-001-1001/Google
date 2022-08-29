#include <stdlib.h>
#include <stdio.h>



int rangRange(int min, int max)
{
    return min + (int) (rand()/(double)(RAND_MAX + 1)*(max-min+1));
}


int num(long double x, long y)
{
    for (int i = 0; i < y; i++)
    {  
        printf("\t%ld\n",rangRange(x,y));
    }
return y+1;
}

int main() 
{
    printf("Hello, world!\n");
    printf("%i",num(1,18));
    printf("\t\t%i",num(18,38));
}
