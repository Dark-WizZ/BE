#include <stdio.h>
#include<stdlib.h>
#include<math.h>
int D;
int a,b,c;
int testcase=1;
void nature_of_roots(int a, int b, int c)
{
  if (a == 0) {
    printf("Not a Quadratic Equation\n");
    return;
  }
  D = b * b - 4 * a * c;
  if (D > 0) {
    printf("Real Roots\n");
  }
  else if (D == 0) {
    printf("Equal Roots\n");
  }
  else {
    printf("Imaginary Roots\n");
  }
}
// Function to check for all testcases
void checkForAllTestCase()
{
  printf("Testcase\ta\tb\tc\tActual Output\n");
  while (testcase <= 13) {
    if (testcase == 1) {
      a = 0;
      b = 50;
      c = 50;
    }
    else if (testcase == 2) {
      a = 1;
      b = 50;
      c = 50;
    }
    else if (testcase == 3) {
      a = 50;
      b = 50;
      c = 50;
    }
    else if (testcase == 4) {
      a = 99;
      b = 50;
      c = 50;
    }
    else if (testcase == 5) {
      a = 100;
      b = 50;
      c = 50;
    }
    else if (testcase == 6) {
      a = 50;
      b = 0;
      c = 50;
    }
    else if (testcase == 7) {
      a = 50;
      b = 1;
      c = 50;
    }
    else if (testcase == 8) {
      a = 50;
      b = 99;
      c = 50;
    }
    else if (testcase == 9) {
      a = 50;
      b = 100;
      c = 50;
    }
    else if (testcase == 10) {
      a = 50;
      b = 50;
      c = 0;
    }
    else if (testcase == 11) {
      a = 50;
      b = 50;
      c = 1;
    }
    else if (testcase == 12) {
      a = 50;
      b = 50;
      c = 99;
    }
    else if (testcase == 13) {
      a = 50;
      b = 50;
      c = 100;
    }
    printf("%d\t\t%d\t%d\t%d\t", testcase,a,b,c);
    nature_of_roots(a, b, c);
    testcase++;
  }
}
int main()
{
  checkForAllTestCase();
  return 0;
}
