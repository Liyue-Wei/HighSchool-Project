#include <bits/stdc++.h>
using namespace std;
int main(){
    int i;
    while(cin >> i){
        if(i % 4 == 0 && i % 100 != 0){
                cout << "閏年\n";
        }
        else if(i % 400 == 0){
                cout << "閏年\n";
        }
        else{
            cout << "平年\n";
        }
    }
    return 0;
}
