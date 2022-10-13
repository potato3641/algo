#include <stdio.h>
int main(void) {
	int T;
	setbuf(stdout, NULL);
	scanf(" %d", &T);
    int J = T;
	for (int tc = 1; tc <= J; tc++) {
        int checker = 1;
        int myvar = 255;
 		for (int i=0; i<8; i++) {
			char line[8];
        	scanf(" %s", &line);
            if (checker == 1) {
                int todo = 0;
                for (int j=0; j<=8; j++) {
                    if (line[j]=='O') {
                        if ((myvar&(1<<j))==(1<<j)) {
                            myvar -= (1<<j);
                            if (todo==1) {
                                checker = 0;
                                break;
                            }
                            todo = 1;
                        } else {
                            checker = 0;
                            break;
                        }
                    }
                }
            }
        }
        if (myvar != 0)
            checker = 0;
        if (checker==1)
        	printf("#%d yes\n", tc);
       	else
            printf("#%d no\n", tc);
	}
	return 0;
}
