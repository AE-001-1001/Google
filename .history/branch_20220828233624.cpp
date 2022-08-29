#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
#include <ctype.h>

using namespace std;



int stream(int a){
    for (int i=0; i<a; i++){
    if (a >= 12){
            a++;
    }
    if (a > 1337){
        a = a--;
        i = a/100;
    }
        cout << a << "\n" <<  i << "\n";

    }
    return a;
};

float strf(float k){
    for (float i=0; i<k; i++){
        if (k == i) {
            i++;
        }
        else
        if (k > 100.525){
            k = k--;
        }
    cout << i << "\t" << k << "\n";
}
    return 0;
};

int main()
{
    stream(2004);
    strf(2004.9050);
    return stream(15);
};


