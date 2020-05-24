
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
int target(){
 printf("DeniceCTF_2020{bof_004_call_function_we_want_HDXNOW}");
}

int hackable()
{
  volatile int (*fp)();
  char buffer[256];
  fp = 0;
  printf("%x",target);
  gets(buffer);
  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
  return 0;
}

int main(int argc, char **argv){
  return hackable();
}
