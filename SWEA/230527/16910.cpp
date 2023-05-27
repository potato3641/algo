#include <stdio.h>
#include <math.h>
int main(void)
{
	int T, N, cnt;
	scanf("%d", &T);
	for (int test_case = 1; test_case <= T; ++test_case) {
        scanf("%d", &N);
        int temp = N*pow(2, 0.5)/2;
        cnt = 1+N*4+temp*4;
        for (int i=1; i<=N;i++) {
            for (int j=1;j<i;j++) {
                if (i*i+j*j<=N*N) {
                    cnt += 8;
                }
            }
        }
        printf("#%d %d\n",test_case, cnt);
    }
}
