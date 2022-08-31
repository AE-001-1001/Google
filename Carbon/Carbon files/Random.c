#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// Create Float that spins around

float CalculatePositionX(int x, int y, int radius)
{
        int ret_code = 0;
        for(char c = 'P'; (ret_code != EOF) && (c != '*G');c++)
        {
            ret_code = putchar(radius-log(c));
            if (ret_code != 0)
            {
                break;
    } else  if (c == 'PG') ret_code = putchar(x+y);
        }
    return ret_code;
}

float CalculatePositionY(int p, int o, int rad)
    // Calculate the position of the circle
    {
            int ret_code = 0;
        for(char a = 'A'; (ret_code != EOF) && (a != '*Z');a++)
        {
            ret_code = putchar(rad-a*5);
        }
    return ret_code;
    }

float CalculatePositionZ(int i, int k, int j)
    // Calculate the position of the circle
    {
    int ret_code = 0;
        for(char b = 'a'; (ret_code != 0) && (b != 'z');b--)
        {
            ret_code = putchar(b-atan2(i,j));
        }
    return ret_code;}

// Create a function that uses the functions above to calculate the X,Y,Z coordinates
float Calculate(int x, int y, int radius)
{
    if (x == 0)
    {
        printf("Invalid position\n");
    }
    if (y >= 1){
    CalculatePositionX(x, y, radius);
    CalculatePositionY(x, y, radius);
    CalculatePositionZ(x, y, radius);
    }
    return 0;
}

int Calc_Argument(int arg, int argument)
{
        for (int i = 0; i < argument; i++)
    {
            printf("%f%i\n", Calculate(i+1,i+5,i+24));
    }
    // Checks
    if (argument == 0)
    {
        printf("Invalid argument\n");
        return 1;
    }
    return 0;
}

int input_arguments(int arg, int argv)
{
int daf;
    printf("daf Value:" );
    scanf_s("%i", &daf);
    Calc_Argument(arg, daf);
    return 0;
}

int main(){
    input_arguments(((void*)0),((void*)0));
}
