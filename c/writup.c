#include <stdio.h>
#include <stdlib.h>
#include<time.h>
int main(void)
{
    int n1,n2,n3,n4,n5;
    scanf("%d %d %d %d %d",&n1,&n2,&n3,&n4,&n5);
    int seed = 0;
    while(1){
        srand(seed);
        if(rand() == n1){
            if(rand() == n2){
                if(rand() == n3){
                    if(rand() == n4){
                        if(rand() == n5){
                            printf("Found %d",seed);
                            break;
                        }
                    }
                }
            }
        }
        seed++;
    }
    printf("%d %d %d %d %d ANS: %d\n",n1,n2,n3,n4,n5,rand());
    while(1){
        for(int i = 0; i<5; i++)
            printf("%d ", rand());
        printf(" ANS: %d\n",rand());
        getchar();
    }
    return 0;
}
