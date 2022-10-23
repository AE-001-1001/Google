#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
#include <ctype.h>
#include <ctime>
#include <array>
#include <vector>

using namespace std;

namespace base{
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
};



int RandModule(int argc, char* argv[])
{
    srand((unsigned) time(NULL));
    int random = 1 + (rand() % RAND_MAX);
    // Providing a seed value
    // print random 
    for (int i = 1; i < argc; i++){
        // Retrieve a random number between 1-75
        // Offset = 100
        // Range = 101
        int random = 75 + (rand() % 10);
        cout << "Random number: " << random << endl;
    }
    return random;
};

char Login()
{
    char username;
    int password;
    cout << "What is your username?" << endl;
    cin >> username;
    cout << "What is your password?" << endl;
    cin >> password;
    return '\n';
}

int keys(int argc){
    srand((unsigned) time(NULL));
    int random = 15 + (rand() % RAND_MAX);
    return 0;
};


int main(int argc, char* argv[])
{

for (int i = 1; i < 10; i++){
    cout << i << endl;
    };
    cout << keys(argc + 10);
    cout << '\n';
    cout << Login();
    cout << RandModule(argc+10, argv) << endl;
    return 0;
};
 
