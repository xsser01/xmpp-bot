import slixmpp
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

class XMPPBot(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()
        logging.info("Bot online")

    async def message(self, msg):
        if msg["type"] in ("chat", "normal"):
            sender = msg["from"].bare
            body = msg["body"]
            logging.info(f"Message from {sender}: {body}")
            # هنا تقدر تخزن الرسالة في ملف أو ترسلها لمكان ثاني

async def main():
    jid = "nevskynull@exploit.im"
    password = "PASSWORD_HERE"
    bot = XMPPBot(jid, password)
    await bot.connect()
    await bot.process(forever=True)

if __name__ == "__main__":
    asyncio.run(main())
