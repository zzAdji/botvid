from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Configuration des variables
api_id = 27252909
api_hash = '6f91353b47b4fac1ebbfcee74486d119'
phone_number = '+237656496419'

# Connexion au client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone_number)

    if not await client.is_user_authorized():
        try:
            await client.sign_in(phone_number)
        except SessionPasswordNeededError:
            pw = input('Veuillez entrer votre mot de passe : ')
            await client.sign_in(password=pw)

    group = 'universegroupe'

    message = "bonjour"

    # Envoi du message dans le groupe
    await client.send_message(group, message)

with client:
    client.loop.run_until_complete(main())
