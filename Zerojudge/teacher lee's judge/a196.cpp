#include <bits/stdc++.h>
using namespace std;
int main(){
    int s, e, b, k, i, n;
    i=0;
    while(cin >> s >> e >> b >> k){
        for(n=s; n<=e+1; n++){
            if(n%10==b or n%b==0){
                i+=1;
            }
            else if((n/10)%10==b){
                i+=1;
            }
            if(i==k){
                break;
            }
        }
        if(i<k){
            cout << -1 << '/n';
        }
        else{
            cout << n << '/n';
        }
    }

    return 0;
}
