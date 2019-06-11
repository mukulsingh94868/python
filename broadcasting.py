# radio_listener.py
class WSClient():

    def __init__(self, url):
        self.url = url
        # constant values, but can be passed as params
        self.reply_timeout = 10
        self.ping_timeout = 5
        self.sleep_time = 5

    async def listen_forever(self):
        while True:
            logger.debug('Creating new connection...')
            try:
                async with websockets.connect(self.url) as ws:
                    while True:
                        try:
                            reply = await asyncio.wait_for(ws.recv(), timeout=self.reply_timeout)
                        except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed):
                            try:
                                pong = await ws.ping()
                                await asyncio.wait_for(pong, timeout=self.ping_timeout)
                                logger.debug('Ping OK, keeping connection alive...')
                                continue
                            except:
                                logger.debug('Ping error - retrying connection in {} sec (Ctrl-C to quit)'.format(self.sleep_time))
                                await asyncio.sleep(self.sleep_time)
                                break
                        # Here do something with the data
                        logger.debug(‘Got data > {}’.format(reply))
            except socket.gaierror:
                logger.debug('Socket error - retrying connection in {} sec (Ctrl-C to quit)'.format(self.sleep_time))
                await asyncio.sleep(self.sleep_time)
               	continue
            except ConnectionRefusedError:
                logger.debug('Nobody seems to listen to this URL')
                logger.debug('Exiting...')
                break
