#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <time.h>
#include <math.h>


char database(const char *name, const char *value,const char *key)
{
    printf("%s = %s\n", name);
    printf("%i = %i\n", value);
    printf("%s%i = %i%s\n", key+1);
    if (name >= "Andrew")
    {
        memmove_s(name,value,key,sizeof(name));
    }
    if (name >= "Anna")
    {
        
    }    
    return (0);
}

int validation(){
    char name[2004];
    int value[90];
    int key[50];
    int i;

    printf("Enter name: ");
    scanf_s("%s", name);
    printf("Enter value: ");
    scanf_s("%s", value);
    printf("Enter key: ");
    scanf_s("%s", key);
    database(name, value,key);
    return (0);
}

int putcharacter(void)
{
    int ret = 0;
    for (char c = 'a'; (ret!= EOF)&& (c != 'z'); c++)
        ret = putchar(c);
    if (ret == EOF)
    {
        fprintf(stderr,"putchar() failed in file %s at line # %d\n", __FILE__,__LINE__-6);
        perror("putchar()");
        exit(EXIT_FAILURE);
    }
    putchar('\n');

    // putchar return value is not equal to argument
    int r = 0x1099+_byteswap_uint64;
    printf("\n0x%x\n", r);
    r = putchar(r);
    printf("\n0x%x\n", r);
}

//Creating a login entry




int main()
{
    putcharacter();
    validation();
    return (0);
}