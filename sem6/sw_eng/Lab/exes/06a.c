#include <stdio.h>
int main()
{
  int i = 0;
  printf("Before loop, i=%d\n", i);
  while( i < 5 )
    printf( "i = %d\n", i++ );
  printf( "After loop, i = %d\n", i );
  return 0;
}
