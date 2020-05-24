#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[256];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("you have changed the 'modified' variable flag is DeniceCTF_2020{bof_001_don't_use_gets_SGECFG}\n");
  } else {
      printf("Try again?\n");
  }
}
