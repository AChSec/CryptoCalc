### Home ###

introduction =       "The goal of cryptographic methods in IT security is to ensure confidentiality, authenticity, and integrity of digital messages (\u25B6Security Services)." \
"\n\nThese goals are achieved through encryption, digital signatures, and authentication. (\u25B6Security Mechanisms)." \
"\n\nThe foundation is formed by symmetric and asymmetric methods, whose use is defined in standards (\u25B6Security Protocols)." \
"\n\nSymmetric methods use the same key for both encryption and decryption. Examples include substitution (\u25B6Caesar) and transposition methods (\u25B6Columns), block ciphers such as DES and AES, and stream ciphers such as RC4 and A5." \
"\n\nThe Diffie-Hellman method (\u25B6DH) enables the secure exchange of a shared key." \
"\n\nAsymmetric methods such as (\u25B6RSA) and (\u25B6ElGamal) use public–private key pairs and enable both encryption and digital signatures (\u25B6Signatures)." \
"\n\nMultiplicative inverses (\u25B6a\u207B\u00B9 mod n) and elliptic curves (\u25B6ECC) over finite fields underpin many modern cryptographic methods and are combined with hard mathematical problems such as the discrete logarithm problem." \
"\n\nIn cryptanalysis, methods such as Fermat's factorization method (\u25B6Fermat) and the Baby-step Giant-step algorithm (\u25B6BSGS) are used to identify vulnerabilities." \
"\n\nZero Knowledge proofs (\u25B6ZKP) and hash functions (\u25B6Hash) provide additional assurance of authenticity and integrity."

### Columnar Transposition ###

transposition =     "A classical transposition cipher from antiquity (scytale), where the characters of the plaintext are not changed but only rearranged (permutation). In modern cryptographic methods, transposition is often combined with substitution—for example in block ciphers such as the Advanced Encryption Standard (AES), where S-boxes (substitution) and permutations work together to increase diffusion." \
"\n\nAnother application is format-preserving encryption (FPE), where transposition components are used to encrypt numbers or strings while maintaining a predefined format (e.g., credit card numbers)."

### Caesar ###

caesar_info =           "The Caesar cipher is an example of a monoalphabetic substitution cipher in which each character is uniquely mapped to another character within the same alphabet." \
"\n\nThe method can be broken using frequency analysis by comparing the relative frequencies of characters (or bigrams) in the ciphertext with known frequencies in plaintext, making it possible to recover the key." \
"\n\nShown here is the additive cipher. The multiplicative cipher (y = x * K mod n) is only possible if K is coprime to n, which significantly restricts the key space. Otherwise, bijectivity would be violated (no unique inverse exists)." \
"\n\n⚠️ Historical method – today used only for educational purposes ⚠️"
caesar_output_info =    "(Note: Only letters are replaced.)"

### Multiplicate Inverse ###

m_inverse_info =         "The multiplicative inverse is used in a finite field to represent division. It is the factor that yields the identity element of the multiplicative group (= 1). This requires that the greatest common divisor (gcd) of n and a is 1. The diagram demonstrates this using a linear representation and the extended Euclidean algorithm, with gcd(26, 21) as an example." \
"\n\nFor prime numbers, this condition is always satisfied, and Euler’s theorem can be used to determine the multiplicative inverse. In this case, a is raised to the power φ(n) = n − 1, which yields 1 modulo n." \
"\n\nThe multiplicative inverse is a fundamental building block of most cryptographic methods."

### Diffie- Hellman ###

diffie_hellman_info =    "The Diffie-Hellman key agreement is a protocol for secure key exchange. The shared key remains secret even though the parameters p (a prime number, e.g., 1024 bits) and g, as well as the computed values α and β, are publicly known. The security of the protocol is based on the discrete logarithm problem." \
"\n\n⚠️ There is no authentication of the parties ⚠️"

### RSA Algorithm ###

rsa_info =          "The RSA algorithm typically uses key lengths of 1024 to 2048 bits and requires significant computational effort (around 1000× slower than symmetric methods). It can be broken if the modulus is successfully factorized (e.g., using Fermat’s method (\u25B6Fermat) or Pollard’s Rho)." \
"\n\nRSA encryption is deterministic, meaning identical plaintexts result in identical ciphertexts.\n\n"
rsa_application =   "Secure transmission of a symmetric session key\nDigital signature of the hash value of a message"

rsa_key_info =      "1. Choose two distinct prime numbers p and q\n2. Compute Euler’s totient function φ(n) and the modulus n\n3. Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1\n4. Destroy p and q after key generation" \
"\n\nThe factors p and q are typically generated using a pseudo-random number generator. The modulus n usually has a size of 512 to 4096 bits. The public exponent e is commonly set to 65537 to reduce computational effort during encryption."

rsa_encrypt_info =  "The plaintext x is divided into message blocks m\u2081-m\u1D62 (m < n), which are interpreted as natural numbers. Automatic block formation is not available in this version. If the ASCII value of the plaintext is greater than or equal to the selected modulus n, please encrypt it step by step using, for example, 3- or 6-digit blocks as x." \
"\n\n⚠️ Chosen-plaintext attacks are possible ⚠️"

rsa_decrypt_info =  "Decryption (and signing) can be sped up by a factor of 4 using the Chinese Remainder Theorem. The basic idea is to perform computations using the smaller factors p and q instead of the large modulus n. This reduction in computational effort enables decryption (and RSA signatures) even on smart cards. The Chinese Remainder Theorem is used in almost all RSA implementations. "

### ElGamal ###

elgamal_info =          "The ElGamal scheme is a probabilistic encryption method: it incorporates random values into the computation, so that identical plaintexts result in different ciphertexts. Due to its more complex computations, it is more computationally intensive than the RSA algorithm." \
"\n\nIn addition to encryption and decryption, the scheme also supports secure key exchange and the generation of digital signatures \u25B6Signatures.\n\n"
elgamal_application =   "Secure transmission of a symmetric session key\nGeneration and verification of digital signatures with an appended hash value"

elgamal_key_info =      "1. Choose a prime number p and a base g from the Galois field GF(p)\n2. Choose a private key d\n3. Compute e and publish (p, g, e) as the public key\n4. Keep d secret\n\nFor the modulus p, sizes similar to RSA are recommended (1024, 2048, or 4096 bits). In practice, g is chosen as a generator in GF(p). A generator has the property that every element in [1, p−1] can be expressed as a power of g modulo p. The private key d can be chosen freely but must be unpredictable."

elgamal_encrypt_info =  "Due to the transmission of two ciphertexts, the storage overhead is twice as high as RSA for comparable security."

elgamal_exchange_info = "Combines key exchange with asymmetric encryption. The key value a can be transmitted alongside the symmetrically encrypted message (hybrid cryptography)."

### Elliptic Curve Cryptography ###

ecc_info =  "Elliptic Curve Diffie-Hellman\nElliptic Curve Digital Signature Algorithm"

### Digital Signatures ###

digital_signature1 = "The message itself is incorporated into the signature and reconstructed during verification. The scheme only supports short messages whose length is less than the key length (e.g., 1024 bits).\n\n"
digital_signature2 = "A hash of the message (e.g., using SHA-256) is signed, while the message and signature are transmitted separately. Due to its efficiency, this approach is widely used in practice. The diagram illustrates the underlying principle.\nA forgery is possible if an attacker can find a different message with the same hash value and substitute it during transmission."

### Fermat ###

fermat_info =       "This approach exploits weaknesses in schemes whose security relies on the factorization of large numbers (e.g., \u25B6RSA). The goal is to determine the factors p and q in order to compute φ(n) = (p−1)(q−1), thereby working in the modulus where e (public key) has a multiplicative inverse d (private key). The mathematical foundation is based on the third binomial formula."

### Shanks' Babystep- Giantstep

bsgs_info =         "Shanks’ Baby-step Giant-step algorithm is a method for solving the discrete logarithm problem. The goal is to find a value r such that e * g\u207B\u02B3 mod p equals 1 (implying d = r mod p). This is achieved by expressing the exponent as d = m * q + r mod (p − 1). In principle, this allows cryptographic attacks on schemes such as the Diffie-Hellman key exchange (DH) or the ElGamal scheme." \
"\nIn an attack on Diffie-Hellman, e corresponds to the intercepted value \u03B1. Using d, the attacker recovers the random value a. The shared key K can then be computed as \u03B2\u1D43." \
"\n\n⚠️ This function cannot be used to attack real-world cryptographic systems. In this implementation, the maximum modulus size is limited to 10**6 to prevent excessive memory usage. ⚠️"

### Zero Knowledge Proof ###

zkp_info =          "Zero-knowledge proofs (ZKP) are cryptographic methods that allow one party to prove to another that it possesses specific knowledge (a secret) without revealing the secret itself. They are commonly used for anonymous authentication." \
"\nZKP protocols such as Fiat-Shamir authentication are based on challenge–response mechanisms. The verifier sends a challenge, and the prover responds. Only a correct response constitutes a successful round." \
"\nThe concept can be illustrated using the ‘magic door’ example by Jean-Jacques Quisquater (see diagram). Only if Bob knows the secret (i.e., possesses the key) will he appear on the side randomly requested by Alice in each round. He thus proves possession of the key without Alice learning anything about the key itself."

fiat_shamir_info =  "The Fiat-Shamir protocol requires only low computational effort, making it suitable for use in smart cards. Typically, 20–30 rounds are considered sufficient."

### Auxiliaries ###

hash_functions_info = "A hash function H(x) maps a message of arbitrary length to a fixed-length hash value (message digest), e.g., 160 bits. Hash functions are deterministic, meaning the same input always produces the same hash. They are therefore used as a fingerprint to verify the integrity of data after storage or transmission. Hashes are commonly used for storing passwords in databases and for handling password input during transmission. To mitigate dictionary attacks (matching against precomputed password hashes), a salt (a random string) can be added before hashing. " \
"\nReconstructing a message from its hash is practically infeasible with modern hash functions. However, collisions remain a fundamental security risk, especially when two different messages produce the same hash value.\n\n"  

pw_hash_info =      "Use mySecret for Alice and admin01 for Bob as plaintext passwords. The diagram shows the internally used database (fictitious)." \
"\n\nFor demonstration purposes, SHA-1 is used here. Modern systems rely on dedicated password hashing schemes such as bcrypt, scrypt, or Argon2, combined with multiple iterations. The salt is randomly generated and stored per user."

mac_info =          "A MAC is a cryptographic checksum derived from both the message m and a key k. It ensures message authenticity and integrity but cannot provide non-repudiation, as both parties share the same symmetric key. Moreover, the scheme can be vulnerable if an attacker modifies the message without knowing the key until a matching MAC is obtained.\n\n"
hmac_info =         "HMAC (keyed-hash message authentication code) is resistant to such length-extension attacks and can be used with any hash function (e.g., HMAC-SHA256). It is a two-step construction. In this implementation, Python’s built-in function was used to compute the HMAC."

### Security Services ###

confidentiality =   "The property of information being accessible only to authorized entities. This can be achieved by concealing the existence of the information (steganography), encrypting data (cryptography), or implementing organizational access control measures.\n\n"
authenticity =      "The authenticity of authorized entities, verified through authentication. In this process, an entity proves its identity or knowledge of a secret (entity authenticity). If the message remains unchanged, the recipient can be assured of its origin.\n\n"
integrity =         "The property of information being modified only in an authorized and intended manner by authorized entities (message authenticity). This must be verifiable through checksums, hashes, or other methods.\n\n"
non_repudiation =   "The ability to prove the origin of a message to third parties (non-repudiation).\n\n"

### Security Mechanisms ###

encryption =        "Primarily protects the confidentiality of information. Plaintext is mapped bijectively to ciphertext, meaning that decryption restores the original plaintext. Symmetric methods use the same key for both sender and receiver, for example in block or stream ciphers. Asymmetric methods rely on a public–private key pair and enable secure communication without prior key exchange.\n\n"
signatures =        "Ensure authenticity and integrity. The private key is often used as a personal credential for authentication. The association of a key pair with an entity can be verified through certificates.\n\n"
auxiliaries =       "Support the fundamental security services. Hash functions generate a fixed-length hash from arbitrary data. Message authentication codes additionally use a symmetric key to ensure message integrity and authenticity (but not non-repudiation). Many cryptographic schemes are based on so-called trapdoor one-way functions, whose inversion requires disproportionate computational resources (processing power and memory). Examples include integer factorization and the discrete logarithm problem."

### Security Protocols ###

tls =       "Ensures secure data transmission over the Internet (e.g., HTTPS). It provides authentication via certificates, encryption (e.g., AES), and integrity and authenticity checks using MACs (e.g., HMAC).\n\n"
ipsec =     "Protects IP traffic (e.g., in VPNs). It encrypts IP packets using Encapsulating Security Payload (ESP) and ensures authenticity and integrity through the Authentication Header (AH). Key exchange is typically handled by IKE (Internet Key Exchange).\n\n"
pgp =       "Used for email encryption and file security. It employs asymmetric methods (e.g., RSA) for secure key exchange, symmetric algorithms (e.g., AES) for the message itself, and digital signatures for authentication and integrity verification.\n\n"
ssh =       "Enables secure remote access to systems over insecure networks. It uses asymmetric key pairs for authentication and symmetric encryption for data transmission.\n\n"
smime =     "A standard for email encryption and signing. It relies on digital certificates (X.509) for authentication and asymmetric keys, combined with symmetric encryption of the message itself.\n\n"
kerberos =  "A network authentication protocol based on tickets and a central key distribution service, enabling secure authentication and session encryption in large networks (using exclusively symmetric cryptography)."
