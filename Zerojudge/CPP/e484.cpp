#include<cmath>
#include<iostream>
using namespace std;
int isPrime(int x) {
	int ret = 1;
	int i;
	if (x == 1 || (x%2==0&&x!=2)) ret = 0;
	for (i = 3;i < sqrt(x);i+=2) {
		if (x % i == 0) {
			ret = 0;
			break;
		}
	}
	return ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int num;
    while(cin >> num){
        if(isPrime(num)==0){
            cout << "非質數" << endl;
        }
        else cout << "質數" << endl;
    }
}