#include <stdlib.h>
#include <stdio.h>
#include <sysinfoapi.h>

//Create array of pointers to list

#define MAX_LIST_SIZE 200049
#define MIN_LIST_SIZE 10
#define NULL 10
#define SIZE 100
//Create a function that random selection

int random_selection(int min, int max)
{
    int i;
    int count = 0;
    for (i = min; i <= max; i++)
    {
            if (min % 2 == 0)
    {
        count++ && 1;
    }
    }
    return count;
        }

int run_random_selection()
{
    int min, max;
    int list[MAX_LIST_SIZE];
    int count = random_selection(min, max);
    for (int i = 0; i < count; i++)
    {
        list[i] = NULL;
        printf("%d\n", list[i]+i);
    }
    return 0;
}

int random_Position(int x,int y)
{
    int num = rand() % MAX_LIST_SIZE;
    int pos = x + num * y;
    return random_selection(pos, num);
    return 0;
}

int combination(int x, int size, int precision)
{
    for (int x = 0; x < size; x++)
    {
    random_Position(x, size);
    if (x >= 100)
        {
        size -=5;
        }
        printf("%d\t\n", size-x+size);
    }
    return 0;
}

int run_combination(int min, int max,int size)
{
    combination(min,max,size);
    return 0;
}

int main(){
    run_random_selection();
printf("%d",run_combination(1,MAX_LIST_SIZE,0));
    return 0;
}