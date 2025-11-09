Public Key & Bech32 Address Generator from Private Key (Python)

This small script converts an ECDSA private key (hex) into a compressed public key and a native Bech32 (bc1…) SegWit address.
It uses ecdsa (secp256k1) to derive the public key, performs HASH160 (SHA256 then RIPEMD-160), and encodes the result with bech32.

What it does

Accepts a private key in hex string format (optionally prefixed with 0x).

Converts the private key into a secp256k1 public point.

Produces the compressed public key (33 bytes; prefix 02 or 03 depending on y parity).

Computes HASH160(pubkey) = RIPEMD160(SHA256(pubkey)).

Encodes HASH160 into a native SegWit (bech32) address using witness version 0 and HRP "bc" (Bitcoin mainnet).

Key functions

hash160(data: bytes) -> bytes
Computes RIPEMD-160(SHA-256(data)) and returns 20 bytes.

d_to_pubkey_and_bc1(d_hex: str) -> (str, str)
Converts a hex private key d_hex into:

compressed public key hex string (33 bytes),

bech32 bc1... address string.

Example usage
python3 script.py


Example code snippet (inside if __name__ == "__main__":):

d_hex = "0xa1c0e721c19b3593928086c91f88452ce9cd3c8cdc4d84b28e7beed85cf6ff7a"
pubkey, bc1_address = d_to_pubkey_and_bc1(d_hex)
print("🔑 Public key:", pubkey)
print("🏠 Bech32 address:", bc1_address)


Example output:

🔑 Public key: 02a1b2c3... (33-byte hex)
🏠 Bech32 address: bc1qxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Dependencies

Python 3.7+

ecdsa (for secp256k1 key operations)

bech32 (BIP-0173 encoding; common bech32 library)

Standard library: hashlib

Install dependencies:

pip install ecdsa bech32

Notes & caveats

The script assumes the private key is valid for secp256k1 and provided as hex. If the input is malformed or out of range, ecdsa will raise an error.

The produced Bech32 address uses HRP "bc" (Bitcoin mainnet). For testnet use "tb".

Compressed public key format used: prefix 0x02 if y is even, 0x03 if odd (standard compressed format).

This script does not perform any wallet management (no key storage, no signing, no broadcasting). It only performs deterministic derivation.

Ethical & security reminder

Do not paste or use real, sensitive private keys on machines you do not fully control. Any exposed private key grants full access to associated funds.

This tool is intended for educational, testing, and development purposes only (address derivation validation, offline testing, learning how keys map to addresses). Use responsibly.

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
