#include <stdio.h>
int main()
{
  int month;
  do {
    printf( "Please enter the month of your birth > " );
    scanf( "%d", &month );
  } while ( month < 1 || month > 12 );return 0;
}
