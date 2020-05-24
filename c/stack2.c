#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char detectbof[2];
  char buffer[256];
  detectbof[0] = 'N';
  modified = 0;
  gets(buffer);
  if(detectbof[0] != 'N'){
      printf("bof detected\n");
      printf("detectbof %x modified %d",detectbof[0],modified);
      exit(1);
  }
  if(modified == 69) {
      printf("detectbof %x modified %d\n",detectbof[0],modified);
      printf("you have changed the 'modified' variable flag is DeniceCTF_2020{bof_003_set_value_with_bufferOverflow_MEXKUV}\n");
  } else {
      printf("detectbof %x modified %d\n",detectbof[0],modified);
      printf("Try again?\n");
  }
}
