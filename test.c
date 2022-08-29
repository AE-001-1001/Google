#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>


void number(int x)
{
    printf("Number of elements: %d\n", (int) (sizeof(int) * x));
}


int num_processor(int x, int size)
{
    for (int x = 0; x < size; x++)
    {
        printf("%d\t", size-x);
    }
    return 0;
}


int main()
{
int Mynum;
printf("Type a number: \n");
scanf_s("%d", &Mynum);
printf("Your number is: %d\n", Mynum);
num_processor(1, Mynum);
}