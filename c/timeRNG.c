#include <stdio.h>
#include <stdlib.h>
#include<time.h>
int main(int argc, char **argv){

    int score = 0;
    srand(time(0));
    int RNG = rand()%1000;
    fflush(stdout);
    srand(RNG);
    while(1){
        for(int i = 0; i<5; i++){
            printf("%d ", rand());
            fflush(stdout);
        }  
        printf("\nWhat next? :");
        fflush(stdout);
        int num;
        char sbuffer[50] = "";
        fflush(stdin);
        scanf("%d",sbuffer);
        num = atoi(sbuffer);
        if(num == rand()){
            score++;
            printf("correct!! (%d/5)\n",score);
            fflush(stdout);
        }else{
            score = 0;
            printf("wrong!! (%d/5)\n",score);
            fflush(stdout);
        }
        if(score>=5)break;
    }
    printf("DeniceCTF_2020{don't_let_anyone_guess_your_seed_ez_SMCHRD}");
    fflush(stdout);
    return 0;
}

