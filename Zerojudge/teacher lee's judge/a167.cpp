#include<iostream>
using namespace std;
int main(){
    long long fib[75];
    int n, i;

    fib[0] = 1;
    fib[1] = 1;
    for(i=2; i<=70; i+=1 )
        fib[i] = fib[i-1] + fib[i-2];

    while(cin >> n){
        cout << fib[n] << endl;
    }

    return 0;
}
