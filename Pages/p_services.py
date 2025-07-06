import customtkinter as ctk
from texts import confidentiality, authenticity, integrity, non_repudiation, encryption, signatures, auxiliaries, tls, ipsec, pgp, ssh, smime, kerberos
from utils import insert_info


def services(ctx): 						# info page regarding security services
	image = ctx.images.get("services")
	if image:
		ctk.CTkLabel(ctx.content, image=image, text="", 
			   width=200).pack(padx=3, pady=(10,5), expand=True, fill="both")
	
	insert_info(ctx.info_box, "Vertraulichkeit", confidentiality)
	insert_info(ctx.info_box, "Authentizität", authenticity)
	insert_info(ctx.info_box, "Integrität", integrity)
	insert_info(ctx.info_box, "Verbindlichkeit", non_repudiation)



def mechanisms(ctx): 						# info page regarding security mechanisms
	image = ctx.images.get("mechanisms")
	if image:
		ctk.CTkLabel(ctx.content, image=image, text="", 
			   width=200).pack(padx=3, pady=(10,5), expand=True, fill="both")
	
	insert_info(ctx.info_box, "Verschlüsselung", encryption)
	insert_info(ctx.info_box, "Digitale Signaturen", signatures)
	insert_info(ctx.info_box, "Hilfsfunktionen", auxiliaries)



def protocols(ctx): 						# info page regarding security protocols
	image = ctx.images.get("protocols")
	if image:
		ctk.CTkLabel(ctx.content, image=image, text="", 
			   width=200).pack(padx=3, pady=(10,5), expand=True, fill="both")
	
	insert_info(ctx.info_box, "TLS / SSL (Transport Layer Security / Secure Sockets Layer)", tls)
	insert_info(ctx.info_box, "IPsec (Internet Protocol Security)", ipsec)
	insert_info(ctx.info_box, "PGP /GPG (Pretty Good Privacy / GNU Privacy Guard)", pgp)
	insert_info(ctx.info_box, "SSH (Secure Shell)", ssh)
	insert_info(ctx.info_box, "S/MIME (Secure/Multipurpose Internet Mail Extensions)", smime)
	insert_info(ctx.info_box, "Kerberos", kerberos)

