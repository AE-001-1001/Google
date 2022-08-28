#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
#include <ctype.h>
#include <ctime>
#include <array>
using namespace std;
//Classes for Encapsulation
class Citizen {
	private:
		//Private attr
		int id;

	public:
		//setter for salary
		void setSalary(int s){
			id = s;
		}
		//getter for salary
		int getSalary() {
			cout << "\t" << id;
		return 0;
		}
};
//End of Citizen class

// Money Class
class Money {
	private:
	//Private attr
		float key;
	public:
	//setter for key
	void setKey(float k){
            key = k;
        }
    //getter for key
        int getKey() {
            cout << "\t" << key;
	return 0;
	}
};

//End of Classes

//MATH FOR THE AGE GIVEN BY USER	
void math(){
	Citizen Num;
	Num.setSalary(45);
	int x;
	double f;
	cout << "Type Your Age: ";
	char a = x + 3, b = x + 7, c = x + (1*exp(x));
	cin >> x;
	if (x < 16){cout << "NOT OLD ENOUGH TO USE TOOL" << "\n";}
	if (x <= 13){cout << "Your age is: "<< x / 3 * x + (log(x)+log(x)) << "\n";cout << "Death Age is: "<< 3*(log(x)+(log(x)+Num.getSalary())) << "\n";}
	if (x >= 16){cout << "Your Age is: " << x / 3 * x - log(x)-log(x+x) <<"\n";cout << "Death Age is: "<< x + log(x/3*sqrt(x-1)+log(x+3*sqrt(x)+round(x))) << "\n";}
}
//End

//ADDR POINTER FOR EACH LETTER BELOW
void pointeraddr(int x){
	Money gg;
	gg.setKey(x);
	cout << "Pointer Address " << gg.getKey();
	char a = 'A';char b = 'L';char c = 'J';char d = 'F';char e = 'H';char f = 'B';char g = 'O';char h = 'S';char S = 'Q';char A = 'I';
	int i;
	int array[] = {a,b,c,d,e,f,g,h,S,A};
	for (i=0;i<10;i++){printf("%p%i%c\n",array[i],'\n');//printf("%c%p\n",array[i]);
	}
};
	//End
	
//LOGIN AREA	
bool login(bool x)
	{
	bool ISLOGGED = x;
	if (ISLOGGED == false){ // Unverfied
		cout << "Unverfied Login Attempt"; 
	}
	if (ISLOGGED == true)
	{ // Verified Sign
	//Char Shuffle
	cout << "Verified Login Attempt\n";
	char a='S';char l='O';char j='B';char w='H';char d='F';char s='J';char f='L';char h='A';char b='N';char k ='P';char p = 'O';char O = 'N';char N = 'Y';char E = 'F';
	int t;
	int har[] = {a,l,j,w,d,s,f,h,b,k,p,O,N,E};
	//Loop for har (10) is the amount of objects above1
	for (t=0;t<15;t++){
			printf("%c%i",(har[t+1]+rand()%21));
			printf("%i\n",(har[t-1]+rand()%3));
	}
	}
	return ISLOGGED==false;
};	
//End

//Strings for Message
void strings () {
	int i;
	char str[]="Livingishard....";
	i=0;
	while (isalnum(str[i])) i++;
	printf("\nThe first %i characters are alphanumeric.\n",i);
}
//End

// Sens Data
void sensdata(float x){
	x = x;
	//Objects
	Citizen Life;
	Citizen Death;
	Life.setSalary(204);
	Death.setSalary(745);
	//Set Objects from above
	cout << "Life Salary:" <<Life.getSalary()+x*log(x-log(x+204)) <<"\n"<<"Death Salary: "<<Death.getSalary()+x*log(x) << "\n" << "Difference: " << Death.getSalary()+-Life.getSalary();
}
//End

float Floating(float xk)
{
	cout << "What is the number you want to choose?" << endl;
	cin >> xk;
	if (xk > 5){
		cout << xk - 5 << endl;
	}
	printf("%f\n",xk*xk);
	return 0;
}

// Start of Counter
int counter(int x,int y)
{
	cout << x << endl;
	for (x=-3; x<10; x++){
		cout << x*x << endl;
	}
	for (y=-5; y<x*2; y++){
		cout << y*x << endl;
	}
return 0;
};
// End of Counter

int Arr(int x,int y)
{
	//Array
	cout << x << endl;
    for (x=-3; x<10; x++){
        printf("%d ",)
    }

};

//Entry to Main
int main()
{
	counter(-1,2);
	Floating(1.67);
	sensdata(2004.0905);
	strings();
	math();
	pointeraddr(1.80025);
	login(1);
	return Arr(1,5);
};
//End of Main
