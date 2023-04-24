#include <stdio.h>
#include <stdlib.h>
int input;
int max;
char output[30];
void recursive(int, int, int);
int main(){
    while(scanf("%d",&input)!=EOF){
            max=input*2; recursive(0, 0, 0);
        } return 0;
    }
void recursive(int left, int right, int num){
if(left > input || right > left)
        return;
    if(num == max){
            output[num] = '\0'; printf("%s\n", output); return;
    }
    output[num] = '(', recursive(left + 1, right, num + 1); output[num] = ')', recursive(left, right + 1, num + 1);
    }


