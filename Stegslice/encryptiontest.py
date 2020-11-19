try:
    import base64
    from cryptography.hazmat.primitives import hashes
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.backends import default_backend
except:
    print('[-] Please install modules !')

flag = input("Flag :")
print('\n')
password = flag.encode()
salt = b'salt_'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))


encrypted_password = b"gAAAAABfsUj99kH73wJUDgWK24g-R26aFiEYuu0PxpsM7jt0X1O1FK2vLL49G3IkVMaYvxFYunsldBtZJUYg_EU6iAPXCTZ3Bg=="

f = Fernet(key)
try:
    decrypted_pass = f.decrypt(encrypted_password)
    print("[*] Correct Flag, Decrypting ...\n")
    print(f'[+] SSH creds : stegslice:{decrypted_pass.decode()}')
except:
    print('[-] Wrong flag Try Again :)')
