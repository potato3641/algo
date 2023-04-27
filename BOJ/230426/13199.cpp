#include <stdio.h>
int main(void) {
    int T;
    scanf(" %d", &T);
    while (T--) {
        int P, M, F, C;
        scanf(" %d %d %d %d", &P, &M, &F, &C);
        int temp = (M/P)*C;
        int ccnt = temp%F + (temp/F)*C - F;
        printf("%d\n", ccnt?(ccnt>0?1+ccnt/(F-C):0):1);
    }
}
