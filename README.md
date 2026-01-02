# 🔐 CryptoCalc

A modular Cryptography Calculator and graphical learning tool implemented in Python, designed to support the understanding of cryptographic algorithms, protocols, and security concepts through **interactive calculations, visualizations, and step-by-step explanations**.

The tool combines classical cryptography, modern public-key systems, cryptanalysis methods, and zero-knowledge protocols in a single, extensible GUI application.

---

## 📌 Project Motivation

This project was developed to deepen practical and conceptual understanding of cryptography beyond standard lecture material.

Inspired by academic cryptography courses, the tool:
- supports **learning and exam preparation**
- visualizes **elementary cryptographic steps**
- explains **security services, mechanisms, and protocols**
- allows experimentation with **large numerical parameters**

The graphical design intentionally resembles a traditional calculator – hence the name **Cryptography Calculator** – to emphasize structured, step-by-step computation rather than black-box execution.

---

## 🖥️ Application Type

- **GUI-based desktop application**
- Implemented in **Python (CustomTkinter)**
- Manual implementation of cryptographic logic
- Fully self-designed illustrations and explanatory graphics

---

## ✨ Key Features

- 🔢 Modular cryptographic calculations
- 🔑 Classical & modern public-key algorithms
- 📊 Informative diagrams and visual explanations for cryptographic computations
- 🧠 Integrated educational texts explaining security concepts and protocols
- 🧮 Robust handling of large integers
- 📂 Clean, extensible project structure
- 🖼️ All figures and graphics designed independently

---

## 🔐 Implemented Cryptographic Topics

### Classical Cryptography
- **Caesar Cipher**
- **Columnar Transposition Cipher**

---

### Mathematical Foundations
- Modular arithmetic
- Calculation of the **multiplicative inverse**
- Prime number handling
- Euler’s totient function

---

### Public-Key Cryptography
- **Diffie–Hellman key exchange (simulation)**
- **RSA**
  - Key generation
  - Encryption & decryption
  - Digital signatures
- **ElGamal**
  - Encryption
  - Key agreement
  - Digital signatures
- **Comparative analysis of RSA vs. ElGamal**

---

### Elliptic Curve Cryptography
- **Point addition on elliptic curves**
- Visualization of ECC group operations

---

### Cryptanalysis Methods
- **Fermat's factorization method**
- **Shanks’ Baby-Step Giant-Step (BSGS)** algorithm
- Discrete logarithm problem demonstrations

---

### Zero-Knowledge Proofs
- **Fiat–Shamir identification protocol**
- Step-by-step explanation of zero-knowledge properties

---

### Hashing & Authentication
- Cryptographic hash functions
- **MAC / HMAC**
- Password hashing concepts
- Explanation of integrity and authentication guarantees

---

## 🎓 Educational Focus

The tool is explicitly designed to help users:

- Understand **encryption, authentication, and integrity mechanisms**
- Trace **elementary algorithmic steps**
- Relate mathematical operations to security properties
- Build intuition for cryptographic protocols used in practice

It is particularly useful for:
- Cryptography courses and demonstrations in academic contexts
- Cybersecurity & IT-Forensics studies
- Cryptography learning & experimentation
- Exam and self-study preparation  

---

## 🖥️ Usage

Clone the repository

```bash
git clone https://github.com/AChSec/CryptoCalc

cd CryptoCalc
```
Create and activate a virtual environment (Windows):

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```
The graphical user interface will start automatically.

---

## ⚠️ Security Disclaimer

This application is **not intended for real-world cryptographic use**.

- ❌ No production hardening
- ❌ No side-channel protection
- ❌ No secure parameter validation for operational deployment

All implementations serve **educational and demonstrational purposes only**.

---

## 🧩 Extensibility

The project is designed to be easily extended, for example by adding:
- Additional cryptographic protocols
- More cryptanalysis techniques
- Further ECC operations
- Exportable calculation steps for reports or teaching material

---

## 👤 Author

Chris L.  
Cybersecurity & IT-Forensics | MSc Psychology  
GitHub: AChSec

---

## 📜 License

This project is provided for **educational and non-commercial use**.
