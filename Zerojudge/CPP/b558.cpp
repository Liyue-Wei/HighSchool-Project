#include <iostream>
using namespace std;
int main(){
    int i, n, t;
    while(cin >> i){
        t = 1;
        for(n=0;  n<i; n++){
            t+=n;
        }
        cout << t << '\n';
    }
    return 0;
}
