# https://github.com/jamiels/cryptopythonsnippets
# https://github.com/vbuterin/pybitcointools
# multi-sig wallet (constructed from multiple public keys each of which is constructed from multiple private keys)
from bitcoin import *

def main():
    private_key1 = random_key()
    public_key1 = privtopub(private_key1)

    private_key2 = random_key()
    public_key2 = privtopub(private_key2)

    private_key3 = random_key()
    public_key3 = privtopub(private_key3)

    private_key4 = random_key()
    public_key4 = privtopub(private_key4)

    multisig = mk_multisig_script(public_key1, public_key2, public_key3, public_key4, 4)
    print(multisig)

    bitcoin_address = scriptaddr(multisig)
    print("Bitcoin address:", bitcoin_address)

def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
