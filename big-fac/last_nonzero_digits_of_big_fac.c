// not solved for n_max >= 100000000 ...
#include <stdio.h>
#include <time.h>

int main() {
  time_t rawtime;
  struct tm * timeinfo;

  time ( &rawtime );
  timeinfo = localtime ( &rawtime );
  printf( "Current local time and date: %s", asctime (timeinfo) );

  unsigned long long res = 1;
  unsigned long long start = 1;
  // unsigned long long n_max = 1000000000000;
  unsigned long long n_max = 100000000;
  unsigned long long dr = 1000000; // for large n_max, dr = 10^6 and dr = 10^7 would cause different result..., need to fix
  printf("The target factorial is %llu \n", n_max);
  for (unsigned long long i = start; i <= n_max; i++) {
    res *= i;
    while (res % 10 == 0) {
      res /= 10;
    }
    res %= dr;
  }
  printf("The last 6 digits is %llu \n", res);

  time ( &rawtime );
  timeinfo = localtime ( &rawtime );
  printf( "Current local time and date: %s", asctime (timeinfo) );
  return 0;
}
