import customtkinter as ctk
from PIL import Image
from Pages.p_home		import home
from Pages.p_caesar		import caesar
from Pages.p_coltrans	import col_trans
from Pages.p_minv 		import m_inverse
from Pages.p_dh 		import diffie_hellman
from Pages.p_rsa 		import rsa_main, rsa_key, rsa_encrypt, rsa_decrypt
from Pages.p_elgamal 	import elgamal_main, elgamal_key, elgamal_encrypt, elgamal_exchange
from Pages.p_ecc		import point_addition
from Pages.p_signatures import signature_main, create_signature, verification
from Pages.p_fermat		import fermat
from Pages.p_bsgs 		import bsgs
from Pages.p_zkp 		import fiat_shamir, zero_knowledge_info
from Pages.p_hash		import hash_function, auxiliaries_main, pw_hashing
from Pages.p_mac 		import mac
from Pages.p_services 	import services, mechanisms, protocols


### Pages ###

pages = {
	"HOME":				home,
	"CAESAR":			caesar,
	"COL_TRANS":		col_trans,
	"M_INV":			m_inverse,
	"DH":				diffie_hellman,

	"RSA_INFO":			rsa_main,
	"RSA_KEY":			rsa_key,
	"RSA_ENCRYPT":		rsa_encrypt,
	"RSA_DECRYPT":		rsa_decrypt,

	"ELGAMAL_INFO":		elgamal_main,
	"ELGAMAL_KEY":		elgamal_key,
	"ELGAMAL_ENCRYPT": 	elgamal_encrypt,
	"ELGAMAL_EXCHANGE":	elgamal_exchange,

	"ECC":				point_addition,

	"SIGNATURES":		signature_main,
	"SIGN":				create_signature,
	"VERIFY":			verification,

	"FERMAT":			fermat,
	"BSGS":				bsgs,

	"ZKP_INFO":			zero_knowledge_info,
	"FIAT-SHAMIR":		fiat_shamir,

	"AUXILIARIES":		auxiliaries_main,
	"PW-HASHING":		pw_hashing,
	"HASH":				hash_function,
	"MAC":				mac,

	"SERVICES":			services,
	"MECHANISMS":		mechanisms,
	"PROTOCOLS":		protocols,
}


### Images ###

def load_image(path, size):
	return ctk.CTkImage(light_image=Image.open(path), size=size)

images = {
	"logo":				load_image("./Images/logo.png", (86, 70)),
	"caesar":			load_image("./Images/formula_caesar.jpg", (250, 50)),
	"scytale":			load_image("./Images/figure_scytale.png", (170, 150)),
	"gcd":				load_image("./Images/formula_euclidian.jpg", (200, 150)),
	"dh_exchange":		load_image("./Images/sketch_dh.png", (370, 200)),
	"rsa":				load_image("./Images/figure_rsa_keys.png", (250, 150)),
	"rsa_sec":			load_image("./Images/figure_rsa_security.png", (250, 70)),
	"key": 				load_image("./Images/figure_key.png", (90, 90)),
	"rsa_encr":			load_image("./Images/sketch_rsa_encrypt.png", (350, 200)),
	"rsa_decr":			load_image("./Images/sketch_rsa_decrypt.png", (300, 200)),
	"elgamal":			load_image("./Images/figure_elgamal_keys.png", (250, 150)),
	"elgamal_sec":		load_image("./Images/figure_elgamal_security.png", (250, 70)),
	"elgamal_encr":		load_image("./Images/sketch_elgamal_encrypt.png", (350, 200)),
	"elgamal_exch":		load_image("./Images/sketch_elgamal_exchange.png", (400, 200)),
	"ecc":				load_image("./Images/formula_point_addition.png", (400, 200)),
	"signature":		load_image("./Images/sketch_signature.png", (400, 200)),
	"rsa_sign":			load_image("./Images/formula_rsa_sig_create.jpg", (250, 50)),
	"elgamal_sign":		load_image("./Images/formula_elgamal_sign.jpg", (250, 50)),
	"rsa_verify":		load_image("./Images/formula_rsa_sig_verify.jpg", (250, 50)),
	"elgamal_verify":	load_image("./Images/formula_elgamal_verify.jpg", (250, 50)),
	"fermat":			load_image("./Images/sketch_fermat.png", (400, 200)),
	"bsgs":				load_image("./Images/sketch_bsgs.png", (400, 200)),
	"zkp":				load_image("./Images/sketch_fiat_shamir.png", (380, 200)),
	"zkp_info":			load_image("./Images/sketch_zkp.png", (250, 200)),
	"auxiliaries":		load_image("./Images/sketch_auxiliaries.png", (300, 200)),
	"user_database":	load_image("./Images/figure_pw_hashing.jpg", (400, 145)),
	"services":			load_image("./Images/figure_services.png", (350, 158)),
	"mechanisms":		load_image("./Images/figure_mechanisms.png", (350, 158)),
	"about":			load_image("./Images/logo2.jpg", (300, 300))
}