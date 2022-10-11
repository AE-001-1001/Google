#include <stdio.h>
#include <iostream>
#include <cmath>
#include <array>
using namespace std;

class Key {
	private:
	//Private attr
		float key;
        int index;

    public:

    //setter for key
	    void setKey(float k){
        key = k;
    }
    
    //getter for key
    int getKey() {
        cout << key << endl;
	return 0;
	}
};

int test(int x,int y,int z,int w,int h){
    // Print output
    //create a for loop    
    for(int i = 0; i < 10; i++)
    {
    x = x + i; y = y + i; z = z + i;w = w + i; h = h + i;
    cout <<" "<< " "<< h << endl; 
    cout <<" "<< x << " "<< " " << endl;
    cout <<" "<< " " << " " << y << " " << endl;
    cout <<" "<< " " << " " << " " << z << " " << endl;
    cout <<" "<< " " << " " << y << " " << endl;
    cout <<" "<< x << " " << " " << endl;
    cout <<" "<< " " << w << endl;
    cout <<" "<< y+i << " ";
    cout <<" "<< x+i << " "<< endl;
    }
    return 0;
};

int reversetest(int x, int y, int z){
    for (int i = 0; i < 10; i++)
    {
        x = x+ i;y=y+i;z=z+i;
        cout <<"\t"<< " " << x << " " << " " << endl;
        cout <<"\t"<< " " << " " << y << endl ;
        cout <<"\t"<< " " << z << " "<< " " << endl;
    }
    printf("<<<ID>>>:%c" "\nDream Rendered!");
    return x/rand()+y+z;
};

char wordCheck(string k){
    Key gg;
    gg.setKey(k.length()*1.2);
    cout << endl << k;
    return gg.getKey();
};

float test(int x,float y)
{
    Key Num;
    Num.setKey(x/y);
    return Num.getKey();
};

int Init(int argc, int argv, float y, float x){
    char c = wordCheck("Sadness");
    char d = wordCheck("Life");
    char e = wordCheck("Savior\n");
    int f = test(argc,y);
    int f1 = test(argv,x);
    int array[] = {c,d,e,f,f1};
    return printf("%c%f\n" ,array);
}

int main(){
    int a = test(1,2,3,4,5);
    int b = reversetest(1,4,3);
    int table[] = {Init(a,2,3.14,1.43),Init(b,4,1.43,1.34),Init(a+b,2.45,4.13,1.4)};
    return printf("%c%i\n" , table);
};