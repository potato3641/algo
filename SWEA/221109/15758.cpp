#include <stdio.h>
#include <string.h>
#include <malloc.h>
int main(void)
{
	setbuf(stdout, NULL);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
        char lineLeft[50];
        scanf(" %s", &lineLeft);
        char lineRight[50];
        scanf(" %s", &lineRight);
        char lenLeft = strlen(lineLeft);
        char lenRight = strlen(lineRight);
        char *leftRpt = malloc(lenLeft*lenRight);
        strcpy(leftRpt, lineLeft);
        int cnt = lenRight;
        while (--cnt>0)
            strcat(leftRpt, lineLeft);
        char *rightRpt = malloc(lenLeft*lenRight);
        strcpy(rightRpt, lineRight);
        cnt = lenLeft;
        while (--cnt>0)
            strcat(rightRpt, lineRight);
        if (strncmp(leftRpt, rightRpt, lenRight*lenLeft)==0) {
            printf("#%d yes\n", tc);
            continue;
        }
        printf("#%d no\n", tc);
	}
    return 0;
}
