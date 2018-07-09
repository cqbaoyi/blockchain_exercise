# https://github.com/jamiels/cryptopythonsnippets
from blockchain import statistics as stats

def main():
    s = stats.get()
    print("Total blocks", s.total_blocks)
    print("# of Tx in last 24 hours", s.number_of_transactions)
    print("Total BTC sent last 24 hours", "{:,.2f}".format(satoshi_to_btc(s.total_btc_sent)))
    print("Miners revenue USD last 24 hours", "{:,.2f}".format(s.miners_revenue_usd))

    print("Hash rate", s.hash_rate)
    print("Difficulty", s.difficulty)

    # http://bitcoin.sipa.be

def satoshi_to_btc(satoshi):
    return satoshi / 100000000.0


if __name__ == "__main__":
    main()
