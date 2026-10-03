#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char password[100];
    int i, length;
    int upper = 0, lower = 0, digit = 0, special = 0;
    int score = 0;

    printf("Enter password: ");
    scanf("%99s", password);

    length = strlen(password);

    for (i = 0; i < length; i++)
    {
        if (isupper(password[i]))
            upper = 1;
        else if (islower(password[i]))
            lower = 1;
        else if (isdigit(password[i]))
            digit = 1;
        else
            special = 1;
    }

    if (length >= 8)
        score++;
    if (upper)
        score++;
    if (lower)
        score++;
    if (digit)
        score++;
    if (special)
        score++;

    printf("\nPassword Strength: ");

    if (score <= 2)
        printf("Weak\n");
    else if (score == 3 || score == 4)
        printf("Medium\n");
    else
        printf("Strong\n");

    return 0;
}

Example:

Enter password: Hello@123

Password Strength: Strong

Checks:

- Minimum 8 characters
- Uppercase letter
- Lowercase letter
- Number
- Special character