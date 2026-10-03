#include <stdio.h>

int main()
{
    int a, b, gcd;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }

    gcd = a;

    printf("GCD = %d\n", gcd);

    return 0;
}

Example Output:

Enter two numbers: 24 36
GCD = 12

Logic:
"GCD(a, b) = GCD(b, a % b)" — remainder "0" ಆದಾಗ ಸಿಗುವ numberನೇ GCD.