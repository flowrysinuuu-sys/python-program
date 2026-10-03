#include <stdio.h>

long long power(long long base, long long exp, long long mod)
{
    long long result = 1;

    while (exp > 0)
    {
        result = (result * base) % mod;
        exp--;
    }

    return result;
}

int main()
{
    long long P, G;
    long long a, b;
    long long A, B;
    long long key1, key2;

    printf("Enter prime number P: ");
    scanf("%lld", &P);

    printf("Enter primitive root G: ");
    scanf("%lld", &G);

    printf("Enter private key of Alice: ");
    scanf("%lld", &a);

    printf("Enter private key of Bob: ");
    scanf("%lld", &b);

    /* Public keys */
    A = power(G, a, P);
    B = power(G, b, P);

    printf("\nAlice's Public Key = %lld", A);
    printf("\nBob's Public Key   = %lld", B);

    /* Shared secret key */
    key1 = power(B, a, P);
    key2 = power(A, b, P);

    printf("\n\nAlice's Shared Key = %lld", key1);
    printf("\nBob's Shared Key   = %lld\n", key2);

    if (key1 == key2)
        printf("\nKey Exchange Successful!\n");
    else
        printf("\nKey Exchange Failed!\n");

    return 0;
}

Example

Enter prime number P: 23
Enter primitive root G: 5
Enter private key of Alice: 6
Enter private key of Bob: 15

Alice's Public Key = 8
Bob's Public Key   = 19

Alice's Shared Key = 2
Bob's Shared Key   = 2

Key Exchange Successful!

Main formula

- Alice public key: A = Gᵃ mod P
- Bob public key: B = Gᵇ mod P
- Shared key: K = Bᵃ mod P = Aᵇ mod P

ಇದು learning/lab implementation; real applications use established cryptographic libraries and secure parameter choices.