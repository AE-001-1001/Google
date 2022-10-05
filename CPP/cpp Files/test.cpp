#include<iostream>
using namespace std;
int main()

{
int i=0, j=0, NUM=3;
for (i=-NUM; i<NUM; i++){
    for(j=0; j<NUM; j++){
    if (abs(i)+abs(j)<=NUM)
    {
        cout << "*";
    }
}
return 0;
}