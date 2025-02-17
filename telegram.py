def init(api_id, api_hash):
    import asyncio
    from telethon import TelegramClient, events

    from emotions import Analyzer

    asyncio.set_event_loop(asyncio.new_event_loop())

    analyzer = Analyzer()
    client = TelegramClient('./data/telegram', api_id, api_hash, system_version='4.16.30-vxCUSTOM')
    client.start()

    @client.on(events.NewMessage(from_users=['@fanikalin']))
    async def NewMessage_handler(event: events.NewMessage.Event):
        text = event.message.message
        
        analyzer.push(text)
        
    client.run_until_disconnected()