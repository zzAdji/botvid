import random
import asyncio
from telethon import TelegramClient
from telethon.errors import (
    SessionPasswordNeededError, 
    ChatWriteForbiddenError, 
    ChatAdminRequiredError,
    SlowModeWaitError,
    ChannelPrivateError
)

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
            message = "Je leak les cc sniff ce soir à 20h 🕗 dans mon canal ne manqué pas !! \nLien du canal en bio"

            try:
                await client.send_message(group, message)
                print(f"Message envoyé au groupe: {dialog.name}")

            except SlowModeWaitError as e:
                print(f"Le groupe {dialog.name} est en mode lent : {str(e)}")
                await asyncio.sleep(e.seconds)

            except ChatWriteForbiddenError as e:
                print(f"Impossible d'envoyer un message dans le groupe {dialog.name}: {str(e)}")
                continue  # Skip this group and move to the next

            except ChatAdminRequiredError as e:
                print(f"Droits d'administration requis pour envoyer un message dans le groupe {dialog.name}: {str(e)}")
                continue  # Skip this group and move to the next

            except ChannelPrivateError as e:
                print(f"Le groupe {dialog.name} est privé ou vous n'avez pas accès : {str(e)}")
                continue  # Skip this group and move to the next

            await asyncio.sleep(random.randint(0, 8))

async def main():
    await send_messages_to_groups()

with client:
    client.loop.run_until_complete(main())
