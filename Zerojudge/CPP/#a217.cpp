#include<bits/stdc++.h>
#define N 1000
using namespace std;

int main(){
    int i, j ,k;
    char a[N];

    while(fgets(a, N, stdin)){
        k = strlen(a);
        if(a[k-1]==10 || a[k-1]==13) a[k-1]=0;

        bool first=true;
        for(i=0; a[i]; i++){
            if(islower(a[i]) && first) a[i]=toupper(a[i]), first=false;
            if(a[i]=='i' && !isalpha(a[i]) && !isalpha(a[i+1])) a[i]=toupper(a[i]);
            else if(a[i]=='.' || a[i]=='?' || a[i]=='!') first=true;
        }
        printf("%s\n", a);
    }

    return 0;
}
