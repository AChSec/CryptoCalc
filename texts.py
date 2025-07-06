### Home ###

introduction =       "Ziel kryptographischer Verfahren in der IT- Sicherheit ist die Gewährleistung von Vertraulichkeit, Authentizität und Integrität digitaler Nachrichten (\u25B6Sicherheitsdienste)." \
"\n\nDiese Ziele werden durch Verschlüsselung, digitale Signaturen und Authentifizierung erreicht (\u25B6Sicherheitsmechanismen)." \
"\n\nDie Grundlage bilden symmetrische und asymmetrische Verfahren, deren Einsatz in Regelwerken beschrieben ist (\u25B6Sicherheitsprotokolle)." \
"\n\nSymmetrische Verfahren verwenden denselben Schlüssel für die Ver- und Entschlüsselung. Beispiele sind Substitutions- (\u25B6Caesar) und Transpositionsverfahren (\u25B6Spalten), Blockchiffren wie DES und AES und Stromchiffren wie RC4 und A5." \
"\n\nDas Diffie-Hellman Verfahren (\u25B6DH) ermöglicht den sicheren Austausch eines gemeinsamen Schlüssels." \
"\n\nAsymmetrische Verfahren wie (\u25B6RSA) und (\u25B6ElGamal) verwenden Paare aus öffentlichen und privaten Schlüsseln und ermöglichen neben der Verschlüsselung auch digitale Signaturen (\u25B6Signatur)." \
"\n\nMultiplikativ inverse Elemente (\u25B6a\u207B\u00B9 mod n) und elliptische Kurven (\u25B6ECC) im endlichen Zahlenkörper dienen als Basis vieler moderner Verfahren und werden mit mathematisch schwierigen Problemen wie dem Diskreten Logarithmus Problem kombiniert." \
"\n\nIn der Kryptoanalyse werden Ansätze wie die Faktorisierungsmethode nach (\u25B6Fermat) oder Shanks' Baby-step Giant-step Algorithmus (\u25B6BSGS) zur Schwachstellensuche verwendet." \
"\n\nZero Knowledge Proof (\u25B6ZKP) und Hash- Funktionen (\u25B6Hash) sichern Authentizität und Integrität zusätzlich ab."

### Columnar Transposition ###

transposition =     "Klassische Transpositionschiffre aus der Antike (Skytale), bei der Zeichen des Klartexts nicht verändert, sondern lediglich ihre Positionen vertauscht werden (Permutation). In modernen kryptographischen Verfahren wird Transposition oft mit Substitution kombiniert, beispielsweise in Blockchiffren wie dem Advanced Encryption Standard (AES), wo sogenannte S-Boxen (Substitution) mit Permutationen zur erhöhten Diffusion beitragen." \
"\n\nEin weiteres Einsatzgebiet ist die formatbewahrende Verschlüsselung (Format-Preserving Encryption, FPE), bei der Transpositionskomponenten eingesetzt werden, um z.B. Zahlen oder Zeichenketten in einer festgelegten Struktur zu verschlüsseln (z.B. Kreditkartennummern)"

### Caesar ###

caesar_info =           "Die Caesar- Verschlüsselung ist ein Beispiel für eine monoalphabetische Substitutions-Chiffre, bei dem jedes Zeichen eindeutig auf ein anderes Zeichen desselben Zeichensatzes abgebildet wird." \
"\n\nDas Verfahren kann durch eine Häufigkeitsanalyse kompromittiert werden, indem die relativen Häufigkeiten der Zeichen (oder Bigramme) im Chiffretext mit den bekannten Häufigkeiten in einem Klartext verglichen werden. Dadurch wird es möglich, den verwendeten Schlüssel zu ermitteln." \
"\n\nHier dargestellt ist die additive Chiffre. Die multiplikative Chiffre (y = x * K mod n) ist nur möglich, wenn K teilerfremd zu n ist, was den Schlüsselraum stark einschränkt. Anderenfalls wäre die Eineindeutigkeit verletzt (Umkehrung nicht möglich)" \
"\n\n⚠️ Historisches Verfahren - heute nur noch zu didaktischen Zwecken eingesetzt ⚠️"
caesar_output_info =    "Hinweis: Es werden nur Buchstaben ersetzt."

### Multiplicate Inverse ###

m_inverse_info =         "Das multiplikativ inverse Element wird im endlichen Zahlenkörper benötigt, um eine Division abzubilden. Es entspricht dem Faktor, der auf das Identitätselement der multiplikativen Gruppe (= 1) führt. Voraussetzung ist, dass der größte gemeinsame Teiler (ggT) von n und a ebenfalls 1 ist. Die Abbildung demonstriert dies anhand der Lineardarstellung und mithilfe des erweiterten Euklidischen Algorithmus am Beispiel ggT(26, 21)." \
"\n\nBei Primzahlen ist die Voraussetzung immer erfüllt und es kann alternativ der Satz von Euler zur Bestimmung des multiplikativ inversen Elements genutzt werden. Dabei wird a mit Φ(n) = n - 1 potenziert. Modulo n führt dies auf den Wert 1." \
"\n\nDas multiplikativ inverse Element ist elementarer Bestandteile der meisten kryptographischen Verfahren."

### Diffie- Hellman ###

diffie_hellman_info =    "Die Schlüsselvereinbarung nach Diffie- Hellman ist ein Protokoll zum sicheren Schlüsselaustausch. Der gemeinsame Schlüssel bleibt trotz Veröffentlichung der gemeinsamen Werte p (Primzahl, z.B. 1024 Bit Länge) und g sowie der berechneten Werte Alpha und Beta geheim. Die Sicherheit des Protokolls basiert auf dem Diskreten Logarithmus Problem." \
"\n\n⚠️ Es findet keine Authentifizierung der Parteien statt. ⚠️"

### RSA Algorithm ###

rsa_info =          "Der RSA- Algoithmus arbeitet mit Schlüssellängen von typischerweise 1024 - 2048 Bit und erfordert einen hohen Rechenaufwand (ca. 1000x langsamer als symmetrische Verfahren). Ein Angriff ist möglich, wenn es gelingt, das verwendete Modul zu faktorisieren (z.B. mit der Methode nach \u25B6Fermat oder Pollard's Rho)." \
"\n\nDie Verschlüsselung mit RSA ist deterministisch, d.h. gleiche Klartexte führen auf gleiche Geheimtexte.\n\n"
rsa_application =   "Übertragung eines symmetrischen Sitzungsschlüssels\nDigitale Signatur auf den Hash-Wert einer Nachricht"

rsa_key_info =      "1. Wähle zwei ungleiche Primfaktoren p und q\n2. Berechne die Eulersche Φ-Funktion und das Modul n\n3. Wähle e mit 1 < e < Φ(n) und ggT(e, Φ(n)) = 1\n4. Vernichte p und q nach der Schlüsselerzeugung" \
"\n\nDie Faktoren p und q werden üblicherweise mit einem Pseudo- Noise- Generator erstellt. Die Größe des Moduls n entspricht oft Zahlen mit 512 bis 4096 Binärstellen. Als öffentlicher Schlüssel e wird häufig der Dezimalwert 65537 gewählt (geringerer Rechenaufwand bei der Verschlüsselung)."

rsa_encrypt_info =  "Der Klartext x wird in Nachrichtenblöcke m\u2081-m\u1D62 (m < n) aufgeteilt, die als natürliche Zahlen interpretiert werden. In dieser Version ist eine automatische Blockbildung nicht verfügbar. Sollte der ASCII- Wert des Klartextes größer / gleich dem gewählten Modul n sein, verschlüssele bitte schrittweise z.B. 3er oder 6er Blöcke als x." \
"\n\n⚠️ Chosen Plaintext Angriffe möglich. ⚠️"

rsa_decrypt_info =  "Die Entschlüsselung (und Signatur) kann mit dem Chinesischen Restsatz um den Faktor 4 beschleunigt werden. Das Grundprinzip beruht darauf, bei der Rechnung die kleineren Faktoren p und q anstelle des großen Moduls n zu verwenden. Dank dem dadurch eingesparten Rechenaufwand können Entschlüsselung (und RSA Signaturen) auch auf Chipkarten durchgeführt werden. Der Chinesische Restsatz wird praktisch in allen Implementierungen von RSA verwendet. "

### ElGamal ###

elgamal_info =          "Das Verfahren nach Taher ElGamal ist ein probabilistisches Verschlüsselsverfahren: In die Berechnung gehen Zufallszahlen ein, sodass gleiche Klartexte auf unterschiedliche Geheimtexte abgebildet werden. Aufgrund der komplexeren Berechnungen ist das Verfahren aufwendiger als der RSA- Algorithmus." \
"\n\nNeben Ver- und Entschlüsselung ermöglicht das Verfahren auch einen sicheren Schlüsselaustausch und das Erzeugen digitaler \u25B6Signaturen.\n\n"
elgamal_application =   "Übertragung eines symmetrischen Sitzungsschlüssels\nErzeugung und Verifikation digitaler Signaturen mit Hashwert- Anhang"

elgamal_key_info =      "1. Wähle Primzahl p und Basis g aus dem Galois-Körper(p)\n2. Wähle privaten Schlüssel d\n3. Berechne e und veröffentliche (p, g, e) als öffentlichen Schlüssel\n4. Halte d geheim\n\nFür das Modul p werden ähnliche Größen wie bei RSA empfohlen (1024, 2048 oder 4096 Bit). Für die Basis g wird in praxi ein Generator- Element in GF(p) gewählt. Ein Generator- Element hat die Eigenschaft, dass jedes Element aus [1, p-1] als Potenz von g mod p darstellbar ist. Der private Schlüssel d ist frei wählbar, sollte jedoch nicht zu erraten sein."

elgamal_encrypt_info =  "Aufgrund der Übermittlung zweier Geheimtexte ergibt sich ein doppelter Speicheraufwand als RSA bei vergleichbarer Sicherheit."

elgamal_exchange_info = "Verbindet Schlüsselaustausch mit asymmetrischer Verschlüsselung. Der Schlüsselwert a kann gemeinsam mit der symmetrisch verschlüsselten Nachricht übertragen werden (hybride Kryptographie)"

### Elliptic Curve Cryptography ###

ecc_info =  "Elliptic Curve Diffie-Hellman\nElliptic Curve Digital Signature Algorithm"

### Digital Signatures ###

digital_signature1 = "Die Nachricht selbst wird bei der Signatur mitverarbeitet und bei der Verifizierung wiederhergestellt. Das Verfahren unterstützt nur kurze Nachrichten, deren Länge kleiner als die Schlüssellänge ist (z.B. 1024 Bit).\n\n"
digital_signature2 = "Signiert wird ein Hashwert der Nachricht (z.B. mit SHA-256). Signatur und Nachricht werden separat übermittelt. Das Vorgehen ist aufgrund seiner Effizienz gängig in der Praxis. Die Abbildung zeigt das prinzipielle Verfahren.\nEine Fälschung ist möglich, wenn es dem Angreifer gelingt, eine ihm günstige Nachricht mit demselben Hashwert zu finden und bei der Übertragung zu ersetzen."

### Fermat ###

fermat_info =       "Ausnutzung von Schwachstellen in Verfahren, deren Sicherheit auf der Faktorisierung großer Zahlen beruht (z.B. \u25B6RSA). Ziel ist es, die Faktoren p und q zu ermitteln, um durch den Satz von EULER Φ(n) = (p-1) * (q-1) das Modul zu erhalten, in dem e (öffentlicher Schlüssel) multiplikativ invers zu d (privater Schlüssel) ist. Mathematische Grundlage ist die Ausnutzung der 3. Binomischen Formel."

### Shanks' Babystep- Giantstep

bsgs_info =         "Shanks‘ Baby-step Giant-step Algorithmus ist ein Verfahren zur Lösung des Diskreten Logarithmus Problems. Gesucht wird ein Wert r, der in der Gleichung e * g\u207B\u02B3 mod p den Wert 1 liefert (weil dann gilt: d = r mod p). Realisiert wird dies, indem auf dem Exponenten d = m * q + r mod (p – 1) gerechnet wird. Damit können prinzipiell kryptographische Angriffe z.B. auf den Diffie-Hellman Schlüsselaustausch (DH) oder das ElGamal- Verfahren umgesetzt werden." \
"\nBei einem Angriff auf DH entspricht e dem abgefangenen \u03B1. Mit d erhält der Angreifer die Zufallszahl a. Der gemeinsame Schlüssel K kann anschließend durch \u03B2\u1D43 ermittelt werden." \
"\n\n⚠️ Ein Angriff auf reale kryptographische Systeme ist mit dieser Funktion nicht möglich. In der vorliegenden Implementation ist die maximale Modulgröße auf 10**6 begrenzt, um eine zu hohe Speichernutzung zu verhindern. ⚠️"

### Zero Knowledge Proof ###

zkp_info =          "Zero-Knowledge Proofs (ZKP) sind kryptographische Verfahren, mit denen eine Partei einer anderen Partei beweisen kann, dass sie über ein bestimmtes Wissen (Geheimnis) verfügt, ohne dabei das Geheimnis selbst preiszugeben. Zero-Knowledge Proofs werden für die anonyme Authentifizierung eingesetzt." \
"\nZKP- Protokolle wie die Fiat-Shamir Authentifizierung bauen auf Challenge-Response Verfahren auf. Dabei sendet die verifizierende Partei eine Anforderung (Challenge), auf die die beweisende Partei antwortet (Response). Nur bei korrekter Response gilt die Runde als bestanden." \
"\nDie Funktionsweise kann am Beispiel der Magischen Tür nach Jean-Jacques Quisquater illustriert werden (siehe Abbildung). Nur bei Kenntnis des Geheimnisses (Besitz des Schlüssels) kommt Bob in jeder Runde an der von Alice per Zufall geforderten Seite heraus. Er hat damit bewiesen, den Schlüssel zu besitzen, ohne dass Alice Kenntnis vom Schlüssel erlangt."

fiat_shamir_info =  "Das Fiat-Shamir Protokoll kommt mit einem geringen Rechenaufwand aus, was den Einsatz z.B. in Chipkarten ermöglicht.\nÜblicherweise werden 20-30 Runden als ausreichend erachtet."

### Auxiliaries ###

hash_functions_info = "Durch eine Hashfunktion H(x) wird eine Nachricht beliebiger Länge auf einen Hashwert oder Message Digest fester Länge (z. B. 160 Bit) abgebildet. Hashfunktionen sind deterministisch, d.h. die gleiche Eingabe liefert immer denselben Hashwert. Sie werden daher im Sinne eines Fingerabdrucks genutzt, um die Integrität von Dateien bei der Speicherung oder Übertragung nachträglich feststellen zu können. Insbesondere kommen Hashwerte zum Einsatz, wenn es um die Speicherung von Passwörtern in Datenbanken oder die Übertragung der Passwort-Eingabe geht. Um Wörterbuchangriffe zu erschweren (Abgleich mit Hashwerten von automatisch generierten Passwort-Listen), kann dem Passwort vor dem Hashen ein Salt (zufällige Zeichenfolge) hinzugefügt werden. " \
"\nDie Rekonstruktion einer Nachricht aus dem Hashwert ist bei modernen Hashfunktionen praktisch nicht möglich. Dennoch sind Kollisionen grundsätzlich ein Sicherheitsrisiko, insbesondere wenn zwei unterschiedliche Nachrichten auf denselben Hashwert abgebildet werden.\n\n"  

pw_hash_info =      "Verwende für Alice mySecret und für Bob admin01 als Klartext- Passwörter. Die Abbildung zeigt die intern genutzte Datenbank (fiktiv)." \
"\n\nHier wurde zu Demonstrationszwecken SHA1 für die Hashwerte verwendet. Moderne Systeme nutzen spezielle Hashing- Verfahren wie bcrypt, scrypt oder Argon2 sowie Iterationen. Der Salt wird zufällig generiert und pro Benutzer gespeichert."

mac_info =          "Der MAC ist eine kryptographische Prüfsumme, in die die Nachricht m und ein Schlüssel k einfließen. Ein MAC gewährleistet Authentizität und Integrität einer Nachricht, kann gegenüber Dritten allerdings nicht ihre Herkunft beweisen, da zwei Parteien im Besitz des symmetrischen Schlüssels sind. Zudem ist das Verfahren dadurch angreifbar, dass die ursprüngliche Nachricht auch ohne Kenntnis des Schlüssels durch einen Angreifer solange verändert werden kann, bis ein identischer MAC entsteht.\n\n"
hmac_info =         "Der HMAC (keyed-Hash Message Authentication Code) ist immun gegen solche Längenangriffe. Es kann eine beliebige Hashfunktion verwendet werden (z.B. HMAC-SHA256). Es handelt sich um ein zweistufiges Verfahren. Hier wurde die in Python vorhandene Funktion zur Berechnung des HMAC verwendet."

### Security Services ###

confidentiality =   "Die Eigenschaft einer Information, nur autorisierten Instanzen (Befugten) verfügbar zu sein. Dies kann erreicht werden, indem die Existenz der Information verborgen wird (Steganographie), die Informationen bzw. Daten verschlüsselt werden (Kryptographie) oder organisatorische Maßnahmen zur Zugangs- oder Zugriffskontrolle implementiert werden.\n\n"
authenticity =      "Die Echtheit von befugten Instanzen, die mittels Authentifizierung geprüft wird. Dabei beweist die Instanz ihre Identität oder ihre Kenntnis eines Geheimnisses (Partner- Authentizität). Vorausgesetzt, die Nachricht bleibt unverändert, erlangt der Empfänger dadurch Sicherheit, von wem die Nachricht stammt.\n\n"
integrity =         "Die Eigenschaft einer Information, nur in zulässiger und beabsichtigter Weise durch Befugte geändert worden zu sein (Nachrichten- Authentizität). Dies muss durch Prüfsummen, Hashwerte oder weitere Methoden nachvollziehbar sein.\n\n"
non_repudiation =   "Die Möglichkeit, die Herkunft einer Nachricht gegenüber Dritten eindeutig nachweisen zu können (Nicht- Abstreitbarkeit).\n\n"

### Security Mechanisms ###

encryption =        "Schützt in erster Linie die Vertraulichkeit von Informationen. Klartext wird dabei eineindeutig (bijektiv) auf Geheimtext abgebildet, d.h. die Umkehrung (Entschlüsselung) führt wieder auf den Klartext. Symmetrische Verfahren nutzen denselben Schlüssel für Sender und Empfänger, z.B. bei Block- oder Stromchiffren. Asymmetrische Verfahren basieren auf einem Schlüsselpaar (öffentlich/privat) und ermöglichen sichere Kommunikation ohne vorherigen Schlüsselaustausch.\n\n"
signatures =        "Sichern Authentizität und Integrität. Als persönliches Merkmal wird häufig der private Schlüssel für die Authentifizierung genutzt. Die verbindliche Zuordnung eines Schlüsselpaares zu einer Instanz kann durch Zertifikate bestätigt werden.\n\n"
auxiliaries =       "Unterstützen die grundlegenden Sicherheitsdienste. Hashfunktionen erzeugen aus beliebigen Daten einen Hashwert mit fester Länge. Message Authentification Codes verwenden zusätzlich den symmetrischen Schlüssel, um Integrität und Authentizität einer Nachricht zu sichern (allerdings ohne Nichtabstreitbarkeit). Die mathematische Basis vieler Verfahren bilden sogenannte Trapdoor- Einwegfunktionen, deren Umkehr einen unverhältnismäßigen Ressourceneinsatz erfordert (Rechenleistung, Speicheraufwand). Beispiele sind das Faktorisierungsproblem großer Primzahlen oder das diskrete Logarithmusproblem."

### Security Protocols ###

tls =       "Sorgt für die sichere Datenübertragung im Internet (z. B. HTTPS). Bietet Authentifizierung durch Zertifikate, Verschlüsselung (z. B. AES) sowie Integritäts- und Authentizitätsprüfungen durch MACs (z. B. HMAC).\n\n"
ipsec =     "Schützt IP-Datenverkehr (z.B. in VPNs). Verschlüsselt IP-Pakete (Encapsulating Security Payload) und stellt Authentizität und Integrität durch AH (Authentication Header) sicher. Der Schlüsselaustausch erfolgt meist über IKE (Internet Key Exchange).\n\n"
pgp =       "Dient der E-Mail-Verschlüsselung und Dateisicherung. Verwendet asymmetrische Verfahren (z. B. RSA) zum sicheren Austausch von Schlüsseln, symmetrische Algorithmen (z. B. AES) für die Nachricht selbst sowie digitale Signaturen zur Authentifizierung und Integritätsprüfung.\n\n"
ssh =       "Ermöglicht sicheren Fernzugriff auf Systeme über unsichere Netzwerke. Nutzt asymmetrische Schlüsselpaare zur Authentifizierung und symmetrische Verschlüsselung für die Datenübertragung.\n\n"
smime =     "Standard für die Verschlüsselung und Signatur von E-Mails. Setzt auf digitale Zertifikate (X.509) für Authentifizierung und asymmetrische Schlüssel, kombiniert mit symmetrischer Verschlüsselung der eigentlichen Nachricht.\n\n"
kerberos =  "Ein Netzwerk- Authentifizierungsprotokoll, das auf Tickets und einem zentralen Schlüsselverteilungsdienst basiert. Ermöglicht eine sichere Authentifizierung und Sitzungsverschlüsselung in großen Netzwerken (ausschließlich symmetrische Krpytographie)."
