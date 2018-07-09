import asyncio, websockets, json

def main():
    asyncio.get_event_loop().run_until_complete(start_gdax_websocket())

async def start_gdax_websocket():
    async with websockets.connect("wss://ws-feed.gdax.com") as websocket:
        await websocket.send(build_request())
        async for m in websocket:
            print(m)


def build_request():
    #return "{ \"type\": \"subscribe\",    \"channels\": [{ \"name\": \"heartbeat\", \"product_ids\": [\"ETH-USD\"] }]}"
    return "{ \"type\": \"subscribe\",    \"channels\": [{ \"name\": \"ticker\", \"product_ids\": [\"ETH-USD\"] }]}"



if __name__ == "__main__":
    main()
