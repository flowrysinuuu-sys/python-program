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
    long long p, q, n, phi, e, d, m, c;

    printf("Enter prime p: ");
    scanf("%lld", &p);

    printf("Enter prime q: ");
    scanf("%lld", &q);

    n = p * q;
    phi = (p - 1) * (q - 1);

    printf("Enter e: ");
    scanf("%lld", &e);

    /* Find d such that (e*d) mod phi = 1 */
    d = 1;
    while ((e * d) % phi != 1)
    {
        d++;
    }

    printf("\nPublic Key  = (%lld, %lld)", e, n);
    printf("\nPrivate Key = (%lld, %lld)", d, n);

    printf("\n\nEnter message as a number: ");
    scanf("%lld", &m);

    /* Encryption */
    c = power(m, e, n);
    printf("Encrypted message = %lld", c);

    /* Decryption */
    m = power(c, d, n);
    printf("\nDecrypted message = %lld\n", m);

    return 0;
}