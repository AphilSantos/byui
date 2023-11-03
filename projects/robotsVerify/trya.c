#include <stdio.h>

int main() {

    char* name = "Name:";

    printf("%s\n", name);
    printf("School:\n");
    printf("Address:\n");
    printf("Age:\n");

    printf("\n");

    printf("a. %d\n", 127);
    printf("b. %10f\n", 3.1415926535);
    printf("c. %d\n", 122013);
    printf("d. %.5f\n", 0.00008);
    printf("e. %d\n", 2506);

    printf("\n");

    printf("a. %.2f\n", 19.20);
    printf("b. %.1f\n", 200.0);
    printf("c. %.2f\n", 56.1300);
    printf("d. %.2f\n", 8.602);
    printf("e. %.3f\n", 1.01100);
    return 0;
}