import hashlib
from ecdsa import SigningKey, SECP256k1
import bech32

def hash160(data: bytes) -> bytes:
    sha = hashlib.sha256(data).digest()
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha)
    return ripemd.digest()

def d_to_pubkey_and_bc1(d_hex: str):
    d_int = int(d_hex, 16)
    sk = SigningKey.from_secret_exponent(d_int, curve=SECP256k1)
    vk = sk.verifying_key
    x = vk.pubkey.point.x()
    y = vk.pubkey.point.y()
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    compressed_pubkey = prefix + x.to_bytes(32, 'big')
    h160 = hash160(compressed_pubkey)
    bc1 = bech32.encode("bc", 0, h160)
    return compressed_pubkey.hex(), bc1

if __name__ == "__main__":
    d_hex = "0xa1c0e721c19b3593928086c91f88452ce9cd3c8cdc4d84b28e7beed85cf6ff7a"
    pubkey, bc1_address = d_to_pubkey_and_bc1(d_hex)
    print("🔑 Public key:", pubkey)
    print("🏠 Bech32 address:", bc1_address)
