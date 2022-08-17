#include<stdio.h>
#include<string.h>
#include <ctype.h>

int main(int argc, char *argv[]){
    char* input = argv[1];
    int state=0, i=0, len=strlen(input);

    if (input[len-1] != '1'){
        printf("\n{!} Not a valid input.\n");
    }else{
        char currInput;

        for(i=0; i<len; i++){
            currInput = input[i];
            if (isdigit(currInput) == '0'){
                printf("{!} Only numbers allowed.\n");
                break;
            }

            if (state == '0' && currInput == '1'){
                state = 1;
            }else if (state == '1' && currInput == '0'){
                state = 0;
            }
        }
        printf("\n** Valid input. **\n");
    }
    
    return 0;
}
