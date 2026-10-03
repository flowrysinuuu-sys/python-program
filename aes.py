#include <stdio.h>
#include <string.h>
#include <openssl/aes.h>

int main()
{
    unsigned char key[16] = "1234567890123456";
    unsigned char text[16] = "Hello AES";

    unsigned char encrypted[16];
    unsigned char decrypted[16];

    AES_KEY enc_key, dec_key;

    /* Encryption */
    AES_set_encrypt_key(key, 128, &enc_key);
    AES_encrypt(text, encrypted, &enc_key);

    printf("Encrypted data: ");
    for (int i = 0; i < 16; i++)
        printf("%02x", encrypted[i]);

    /* Decryption */
    AES_set_decrypt_key(key, 128, &dec_key);
    AES_decrypt(encrypted, decrypted, &dec_key);

    decrypted[15] = '\0';

    printf("\nDecrypted data: %s\n", decrypted);

    return 0;
}

Output

Encrypted data: 7f8a...
Decrypted data: Hello AES

ಮುಖ್ಯ points

- AES = Advanced Encryption Standard
- ಇದು symmetric-key encryption.
- Encryption ಮತ್ತು decryption ಎರಡಕ್ಕೂ same key ಬಳಸಲಾಗುತ್ತದೆ.
- AES key sizes: 128, 192, 256 bits.
- "AES_encrypt()" → Encryption
- "AES_decrypt()" → Decryption

Note: "openssl/aes.h" ಬಳಸಿರುವುದರಿಂದ systemನಲ್ಲಿ OpenSSL library ಇರಬೇಕು.