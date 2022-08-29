#include <stdio.h>
#include <string.h>
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

class number {
	private:
		//Private attr
		int num;
	public:
		//setter for salary
		void setnum(int s){
			num = s;
		}
		//getter for salary
		int getnum() {
            {
                cout << num << endl;
            } 
		return 0;
		}
};

int main()
{
number as;
as.setnum(22364);
as.getnum();
return 0;
};
