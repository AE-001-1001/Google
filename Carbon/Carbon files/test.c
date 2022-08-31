#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>


void number(int x,int)
{
    printf("Number of elements Rendered: %d\t\n", (sizeof(int) + x));
}

void float_num(float x,float y)
{
    printf("Number of Floats rendered: %f\t\n",(sizeof(float) + x / y));
}


//Create a float representation of a number given by user
float float_processor(float x,int size,float precision)
{
    for (int x = 0; x < size; x++)
    {
        float_num(x,precision);
    }
    return 0;
};

float run_float(float x,int size,float precision)
{
float myfloat;
int Sizes;
float myprecision;
printf("Type Float[1] Value: %f\t");
scanf_s("%f",&myfloat);
printf("Size of Float[1] Value: %d\t\n",Sizes);
scanf_s("%d", &Sizes);
printf("Precision Value: %f\t\n");
scanf_s("%f",&myprecision);
float_processor(myfloat,Sizes,precision);
return 0;
}

// Creates a string representation of Numbers given by user
int num_processor(int x, int size, int precision)
{
    for (int x = 0; x < size; x++)
    {
    if (x % precision == 0)
        {
            number(x,size);
        }
    if (x >= 100)
        {
        size -=5;
        }
        printf("%d\t\n", size-x);
    }
    return 0;
}
//End

int run_processor(int x, int size){
int Mynum;
int num;
int precision;
printf("Type the Precision value[%i] : ");
scanf_s("%i", &precision);
printf("Type a number: \n");
scanf_s("%d", &Mynum);
printf("Your number is: %d\n", Mynum);
num_processor(num, Mynum,precision);
}


int main()
{
run_float(1,0.5429404,0.5479504);
run_processor(NULL,NULL);
}