# https://github.com/jamiels/cryptopythonsnippets
# bitcoin address
from bitcoin import *

def main():
    private_key = random_key()
    public_key = privtopub(private_key)
    bitcoin_address = pubtoaddr(public_key)    # SHA-256 hash twice
    print(private_key, public_key, bitcoin_address)

def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
