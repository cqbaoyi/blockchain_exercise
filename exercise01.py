# https://github.com/jamiels/cryptopythonsnippets
from blockchain import blockexplorer as be

def main():
    latest_block = be.get_latest_block()
    print("latest block:", latest_block.height)
    print("latest block hash", latest_block.hash)
    
    pizza_tx_hash = "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
    pizza_block_hash = "00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8"
    laszlo_addr = "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"

    pizza_block = be.get_block(pizza_block_hash)
    print("The block height for the Laszlo tx is ", pizza_block.height)

    pizza_tx = be.get_tx(pizza_tx_hash)

    print(pizza_tx)

    for o in pizza_tx.outputs:
        print(satoshi_to_btc(o.value))
    
    s = 0
    for o in pizza_tx.inputs:
        s += satoshi_to_btc(o.value)
        print(satoshi_to_btc(o.value))

    pizza_cost = format(satoshi_to_btc(pizza_tx.outputs.pop().value), ",f")
    print("The cost of the pizza was", pizza_cost)

    #laszlo_tx = be.get_address(laszlo_addr).transactions
    #for t in laszlo_tx:
    #    for o in t.outputs:
    #        print(satoshi_to_btc(o.value))

def satoshi_to_btc(satoshi):
    return satoshi / 100000000


if __name__ == "__main__":
    main()
