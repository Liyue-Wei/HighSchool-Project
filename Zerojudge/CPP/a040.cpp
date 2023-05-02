/*待解*/

#include <iostream>
#include <math.h>
using namespace std;
 

int len(int n){
int ans = 0;
while(n != 0){
n /= 10;
ans++;
}
return ans;
}
 

int main(){
int first = 0;
int last = 0;
int count = 0;
cin >> first >> last;
for(int i = first; i <= last; i++){
int sum = 0;
int num = i; // use a separate variable to iterate through the digits of i
int* arr = new int[len(i)];
for(int j = 0; j < len(i); j++){
arr[j] = num % 10;
sum = sum + pow(arr[j], len(i));
num = num / 10;
}
if(sum == i){
cout << sum << " ";
count++;
}
delete[] arr; // free the memory allocated for the array
}
if (count == 0){
cout << "none" << endl;
}
return 0;
}