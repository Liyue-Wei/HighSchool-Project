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
            cout << "獶借计" << endl;
        }
        else cout << "借计" << endl;
    }
}

/*
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
bool a[46342];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    vector <int> v;
    for (int j = 2; j < 46342; j++){
        if (!a[j]){
            v.push_back(j);
            for (int i = j * j; i < 46342; i += j){
                a[i] = true;
            }
        }
    }
    while (cin >> n){
        if (n > 46341){
            m = sqrt(n);
            bool flag = true;
            for (int i:v){
                if (n % i == 0){
                    flag = false;
                    cout << "獶借计\n";
                    break;
                }
            }
            if (flag) cout << "借计\n";
        }else{
            if (a[n]) cout << "獶借计\n";
            else cout << "借计\n";
        }
    }
    return 0;
}
*/
