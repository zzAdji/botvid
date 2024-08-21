import random
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, ChatWriteForbiddenError, ChatAdminRequiredError

api_id = 22675377
api_hash = 'dbbb2bd930849d92c5e44bec71cc5cc0'
phone_number = '+237674644148'

client = TelegramClient('session_name', api_id, api_hash)

async def send_messages_to_groups():
    await client.start(phone_number)

    if not await client.is_user_authorized():
        try:
            await client.sign_in(phone_number)
        except SessionPasswordNeededError:
            pw = input('Veuillez entrer votre mot de passe : ')
            await client.sign_in(password=pw)

    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            group = dialog.id
            message = "E-Carte cadeau Carrefour dispo à -50% lien dans la bio"

            try:
                await client.send_message(group, message)
                print(f"Message envoyé au groupe: {dialog.name}")

            except (ChatWriteForbiddenError, ChatAdminRequiredError) as e:
                print(f"Impossible d'envoyer un message dans le groupe {dialog.name}: {str(e)}")

            await asyncio.sleep(random.randint(60, 120))

async def main():
    while True:
        await send_messages_to_groups()

        next_run_in = random.randint(3600, 7200)  # Secondes (1h à 2h)
        print(f"Prochain envoi dans {next_run_in / 3600:.2f} heures")
        await asyncio.sleep(next_run_in)

with client:
    client.loop.run_until_complete(main())
