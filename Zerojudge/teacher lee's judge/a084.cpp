#include<iostream>
using namespace std;

int main(){
    long long fib[120];
    int n, i;

    fib[1] = 2;
    fib[2] = 2;
    for(i=3; i<=70; i=i+1){
        fib[i] = fib[i-1] + fib[i-2];
    }

    while(cin >> n){
        cout << fib[n] << endl;
    }

    return 0;
}
