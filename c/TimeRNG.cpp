#include <stdio.h>
#include <stdlib.h>
#include<time.h>
int main(void)
{
    int score = 0;
    srand(time(0));
    int RNG = rand()%1000;
    printf("%d\n",RNG);
    srand(RNG);
    while(1){
        for(int i = 0; i<5; i++)
            printf("%d ", rand());
        printf("\nWhat next? :");
        int num;
        scanf("%d",&num);
        if(num == rand()){
            score++;
            printf("correct!! (%d/5)\n",score);
        }else{
            score = 0;
            printf("wrong!! (%d/5)\n",score);
        }
        if(score>=5)break;
    }
    printf("DeniceCTF_2020{don't_let_anyone_guess_your_seed_ez_SMCHRD}");
    return 0;
}
