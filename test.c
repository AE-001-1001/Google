#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>


void number(int x,int)
{
    printf("Number of elements: %d\n", (int) (sizeof(int) + x));
}

// Creates a string representation of Numbers given by user
int num_processor(int x, int size)
{
    for (int x = 0; x < size; x++)
    {
        if (x % 5 == 0)
        {
            number(x,size);
        }
        printf("%d\t", size-x);
    }
    return 1;
}
//End

int main()
{
int Mynum;
int num;
printf("Type a number: \n");
scanf_s("%d", &Mynum);
printf("Your number is: %d\n", Mynum);
num_processor(num, Mynum);
}