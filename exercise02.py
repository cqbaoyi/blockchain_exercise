# https://github.com/jamiels/cryptopythonsnippets
from blockchain import exchangerates as er

def main():
    currency_symbols = er.get_ticker()

    for c in currency_symbols:
        print(c)

    for c in currency_symbols:
        print(c, ":", currency_symbols[c].p15min)

    for c in currency_symbols:
        print("1 BTC:", 1 / currency_symbols[c].p15min)

    cad_base_btc = er.to_btc("CAD", 5000)
    print("5000 CAD costs", cad_base_btc, "BTCs")

def satoshi_to_btc(satoshi):
    return satoshi / 100000000


if __name__ == "__main__":
    main()
