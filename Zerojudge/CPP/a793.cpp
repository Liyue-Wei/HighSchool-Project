#include <iostream>
using namespace std;
int main(void){
    int i,n;
    while(cin >> i >> n){
        while(i!=0 && n!=0){
            int t=i%n;
            i=n;
            n=t;
        }
        cout << i << endl;
    }
    return 0;
}

