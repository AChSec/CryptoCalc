import math
import numpy as np
import hashlib
import hmac 

                            ### Primality test ###

def is_prime(n):                                # is used in functions rsa_key, elgamal_key, col_trans, dh_exchange
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True                                 # returns True if n is prime


                            ### Convert ASCII ###

def text_to_ascii(text):                        # each character represented by 3 digits
     return ''.join(str(ord(char)).zfill(3) for char in text)


def ascii_to_text(ascii_string):                # converts ASCII string back to normal text
     try:  
          s = str(ascii_string)
          if len(s) % 3 != 0:                   # pad with leading zeros if length is not a multiple of 3
               s = s.zfill(((len(s)+2)//3)*3)
          chars = [chr(int(s[i:i+3])) for i in range(0, len(s), 3)]
          return ''.join(chars)
     except ValueError:
          return "Ungültige Eingabe"
     

                            ### Multiplicative Inverse ###

def m_inverse(a, n):                            # is used in functions rsa_key, elgamal_sign fiat_shamir, fiat_shamir_verification, point_addition
    t, new_t = 0, 1                             # looking for t * a = 1 mod n
    r, new_r = n, a                             # r remainder
    
    while new_r != 0:                           # if new_r == 0 : gcd == r 
         quotient = r // new_r                  # extended Euclidian algorithm
         t, new_t = new_t, t - quotient * new_t
         r, new_r = new_r, r - quotient * new_r
         
    if r > 1:                                   # no multiplicative inverse if a and n not mutually prime
         b = 0                                  # error message is implemented in file: p_minv
    else: 
         b = t if t >= 0 else t + n             # b = multiplicative inverse                   
    return (n, a, b)


                            ### Caesar Substitution ###

def caesar_substitution(text, key):             # applies a Caesar cipher substitution to the input text
    text = text.upper()
    key = int(key) % 26                         # Latin alphabet: mod 26
    s = ""
    for char in text:
        if 'A' <= char <= 'Z':
            pos = ord(char) - ord('A')          # calculate position in alphabet (0 for A, 1 for B, ...)
            shifted = (pos + key) % 26
            new = chr(shifted + ord('A'))       # convert back to ASCII character
            s += new
        else:
            s += char                           # keeps non-alphabet characters unchanged
    return s


                            ### Columnar Transposition ###

def columnar_transposition(text):               # performs columnar transposition visualization on the input text

    if is_prime(len(text)):                     # error message if text length is prime
        return f"Die Zeichenlänge {len(text)} ist eine Primzahl - keine Spaltentransformation möglich"
    else:
        t = []*len(text)                        # converts entry text into list of characters
        for i in text:   
            t.append(i)

        def get_factors(x):                     # finds integer factors for text length
            f = []                              
            for i in range(1, x + 1):
                if x % i == 0:
                    f.append(i)                 # returns a list of factors
            return f

        def create_matrix(t, f):
            matrix = f"Textlänge: {len(t)} Zeichen\n"
            f = f[1:]                           # remove 1 and len(text) from factor list
            f = f[:-1]                          # (both are not relevant for columnar transposition)
           
            for col in f:       
                s = ""                          # create empty string for each factor (displayed at the end)
                col = int(col)
                row = int(len(t) / col)
                matrix += f"\nSpalten: {col}, Zeilen: {row}\n"
                matrix_array = np.asarray(t).reshape(col, row).T     # using numpy to reshape the text into the grid
                matrix += "Matrix:\n"
                for r in matrix_array:
                    for char in r:
                        s += str(char)
                        matrix += str(char) + " "
                    matrix += "\n"
                matrix += f"\nString: \n{s}\n"
                matrix += "_" * 23 + "\n"
            return matrix

    output = create_matrix(t, get_factors(len(text)))
    return output


                            ### Diffie-Hellman Key Exchange ###

def dh_exchange(p, g, a, b):
    if not is_prime(p):                         # checks prerequisites (p = prime)
        raise ValueError("\np muss eine Primzahlen sein")
    if not (1 < a <= p - 2 and 1 < b <= p - 2):
         raise ValueError(f"\nZufallszahlen müssen zwischen 1 und {p-2} liegen")
    if not (2 < g <= p - 2):
         raise ValueError(f"\ng muss zwischen 2 und {p-2} liegen")
    alpha, beta = pow(g, a, p), pow(g, b, p)    # discrete exponentiation, returns alpha and beta
    key = pow(alpha, b, p)
    return alpha, beta, key               


                            ### RSA- Algorithm ###

def rsa_key(p, q, e):
    if not is_prime(p) or not is_prime(q):
         raise ValueError("\np und q müssen Primzahlen sein")
    n = p * q
    phi_n = (p - 1) * (q - 1)
    while math.gcd(e, phi_n) > 1:               # ensure e is coprime to phi_n
         e = e + 1        
    if e >= phi_n:
         raise ValueError("\ne größer/gleich phi_n")
    _, _, d = m_inverse(e, phi_n)               # compute multiplicative inverse of e mod phi_n (i.e. private key d)
    return (n, e, d, phi_n) 


def rsa_encrypt(n, e, x):                       # encrypts message x using RSA public key (n, e)
    y = pow(x, e, n)
    return y                                    # returns encrypted ciphertext y = x^e mod n


def rsa_decrypt(n, d, y):                       # decrypts ciphertext y using RSA private key (n, d)
    x = pow(y, d, n)
    return x                                    # returns decrypted plaintext x = y^d mod n


                            ### ElGamal ###

def elgamal_key(p, g, d):                       # generates ElGamal public key
    if not is_prime(p):
         raise ValueError("\np muss eine Primzahl sein")
    e = g ** d % p
    return e                                    # returns public key component e = g^d mod p


def elgamal_encrypt(x, p, g, e, k):             # encrypts plaintext x using ElGamal encryption
    while math.gcd(k, (p-1))>1:
         raise ValueError("\nk muss teilerfremd zu p-1 sein")
    a = pow(g, k, p)
    b = (pow(e, k, p) * x) % p
    return (a, b)                               # returns ciphertext tuple


def elgamal_exchange_A(p, g, e, k):             # simulates ElGamal key exchange from party A
    while math.gcd(k, (p-1))>1:
         raise ValueError("\nk muss teilerfremd zu p-1 sein")
    key = e ** k % p
    a = g ** k % p
    return (a, key)                             # returns a (public value to send), key (shared secred component)


def elgamal_exchange_B(a, d, p):                # computes the shared secret on party B's side
    key = pow(a, d, p)
    return (key)                    


                            ### Elliptic Curve Cryptography (Point Addition) ###

def point_addition(xp, yp, xq, yq, n):          # performs elliptic curve point addition over modulo n
    temp1 = (yp - yq) % n                       # calculates the slope m
    temp2 = (xp - xq) % n
    _, _, temp3 = m_inverse(temp2, n)
    m = (temp1 * temp3) % n
    xr = (m ** 2 - xp - xq) % n                 # computes the resulting point coordinates
    yri = yp - m * (xp - xr) % n
    yr = (-yri) % n                             # inverts y-coordinate for elliptic curve equation
    return xr, yr


                            ### Digital Signatures ###

def rsa_sign(x, d, n):                          # generates RSA signature for message x
     s = pow(x, d, n)
     return s                                   # returns signature s = x^d mod n


def elgamal_sign(p, g, d, r, m):                # generates ElGamal signature for message m
     while math.gcd(r, (p-1))>1:                # ensure r is coprime to p-1
         raise ValueError("\nr muss teilerfremd zu p-1 sein")
     _, _, ri = m_inverse(r, (p-1))             # compute multiplicative inverse of r mod (p-1)
     rho = pow(g, r, p)
     h = int(hashlib.sha256(str(m).encode()).hexdigest(), 16)
     s = (h - (d * rho)) * ri % (p - 1)
     return h, m, s, rho                        # returns hashed message value, original message, and signature components


def rsa_check(e, n, s, x):                      # verifies RSA signature
     temp = pow(s, e, n)
     if temp == x:                              # x : original message
          return "\u2705 Die Signatur ist gültig!"
     else: 
          return "\U0001F6AB Die Signatur ist ungültig!"


def elgamal_check(p, g, e, rho, s, m):          # verifies ElGamal signature
     temp1 = pow(g, m, p)                       # m : original message
     temp2 = (e ** rho) * (rho ** s) % p
     if temp1 == temp2:
        return "\u2705 Die Signatur ist gültig!"
     else: 
          return "\U0001F6AB Die Signatur ist ungültig!"


                              ### Fermat's Factorization Method ###

def factorise(n):                               # n = a² - b² = (a + b) * (a - b) (3rd binomial formula)
    if n % 2 == 0:                              # trivial factorization: increased performance for large even numbers
         return n // 2, 2
    x = math.ceil(math.sqrt(n))                 # starts with the ceiling of sqrt(n)
    y = x ** 2 - n
    MAX_ITER = 10 ** 6                          # avoids endless loops
    i = 0
    while not math.sqrt(y).is_integer() and i < MAX_ITER:
        x += 1
        y = x ** 2 - n                          # loop within range until y becomes a perfect square
        i += 1
    if i >= MAX_ITER:                           # shows error message
         raise ValueError(f"\nFaktorisierung nicht gefunden. Suche bricht nach {MAX_ITER} Durchläufen ab")
    s = int(math.sqrt(y))                       # converts sqrt(y) into integers (performance optimization)
    return x + s, x - s                         # returns two factors p and q


                              ### Shanks' Babystep-Giantstep- Algorithm ###

def babystep_giantstep(p, g, e, max_size=10**6):
    m = math.ceil(math.sqrt(p - 1))             # phi(p) is p-1 if p is prime
    if m > max_size:                            # restricts large inputs to prevent excessive memory usage
         raise ValueError(f"Eingabe zu groß")
    baby_steps = {pow(g, r, p): r for r in range(m)}    # g^r mod p for r = 0..m-1

    y = pow(g, m * (p - 2), p)                  # Fermat's little theorem
    current = e                                 # giant steps: e * y^q mod p for q = 0..m-1
    for q in range(m):
        if current in baby_steps:
             return q * m + baby_steps[current] # returns solution                  
        current = (current * y) % p             # prepare next giant step
    return "Keine Lösung gefunden"


                              ### Fiat-Shamir Authentification ###

def fiat_shamir(n, s, k, bit):                  # prover's step in the Fiat-Shamir identification scheme
     _, _, v = m_inverse((s**2), n)
     x = k ** 2 % n
     y = 0
     if bit == 0:                               # bit = challenge bit sent by verifier
        y = k % n
        return v, x, y
     elif bit == 1:
        y = k * s % n
        return v, x, y                          # x = commitment, y = response to challenge


def fiat_shamir_verification(n, v, x, y, bit):  # verifier's step in the Fiat-Shamir identification scheme
    if v == 0:
         raise ValueError("\nv darf nicht 0 sein")
    _, _, v_inv = m_inverse(v, n)
    if bit == 1:                                # check if challenge was 1
        temp = x * v_inv % n
        if temp == pow(y, 2, n):
            return "Bestanden!\nx * v\u207B\u00B9 = y² mod n"
    elif bit == 0:                              # check if challenge was 0
        if pow(y, 2, n) == x % n:
            return "Bestanden!\nx = y² mod n"
    return "Ungültig"


                              ### Auxiliaries ###

def create_hash(text, algo):                    # creates hash of the given text using the specified algorithm
    output = ""
    hash_value = hashlib.new(algo)
    hash_value.update(text.encode())
    output += f"Hashwert ({algo}) : \n\n{hash_value.hexdigest()}\n\n"
    hash_info = f"{hash_value.digest_size * 8} Bit Länge \n\n"
    return output, hash_info                    # returns hash value and digest size in bits


def pw_hash(username, password):                # authenticates a user by verifying the password
     users_db = {                               # simulated user database with salted password hashes
          "Alice":  {"password_hash": "76089d360efcd261d4b366c2c90029ccf7ce2de7", "salt": "abc123xyz"},
          "Bob":    {"password_hash": "b3158545d498b9e9dd99c1157a2f3b5465d0617b", "salt": "def456uvw"}
     }
     def hash_password(password, salt):         # creates a SHA-1 hash of password concatenated with salt
          combined = password + salt
          return hashlib.sha1(combined.encode()).hexdigest()
     
     user_record = users_db.get(username)       # retrieves user record from database
     if not user_record: 
          return False
     salt = user_record["salt"]                 # extract stored salt and password hash
     stored_hash = user_record["password_hash"]
     input_hash = hash_password(password, salt) # computes hash of provided password
     return input_hash == stored_hash           # returns True or False after comparison


def calc_hmac(key_raw: str, message_raw: str, hashfunc=hashlib.sha256):
     key = key_raw.encode("utf-8")
     message = message_raw.encode("utf8")
     mac = hmac.new(key, message, hashfunc)
     return mac.hexdigest()                     # returns hexadecimal string of HMAC
