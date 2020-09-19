import json

from api import User
from crypto import decrypt


def get_receiver(uid):
    if not uid:
        return None

    return User.query.filter_by(id=uid).first()


def decrypt_message(message):
    message_enc = json.loads(message.contents)
    pwd = str(message.from_user.tpass) + str(message.to_user.tpass)

    return decrypt(message_enc, pwd)
