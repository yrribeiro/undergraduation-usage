#include<stdio.h>
#include<string.h>

int main(){
    char input[10];

    printf("> Type the sequence of parenthesis:\n");
    scanf("%s", input);
    char currInput;
    int count=0, i=0, len=strlen(input);

    for(i=0; i<len; i++){
        currInput = input[i];
        if (currInput != '(' && currInput != ')'){
            printf("{!} Only parenthesis allowed.\n");
            count = -1;
            break;
        }

        if (currInput != '('){
            count++;
        }else{
            count--;
        }
    }
    if (count != 0){
        printf("\n{!} Not a valid input.\n");
    }else{
        printf("\n** Valid input. **\n");
    }

    return 0;
}
