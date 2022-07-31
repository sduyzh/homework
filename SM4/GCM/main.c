#include "mbedtls/cipher.h"
#include "mbedtls/dhm.h"
#include "mbedtls/md.h"

int main()
{
    gcm_test(MBEDTLS_CIPHER_AES_128_GCM);
    return 1;
}

