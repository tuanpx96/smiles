from datetime import timedelta

from app_smiles.app_smiles import settings


def get_expired_time(token):
    return token.created + timedelta(seconds=settings.EXPIRED_TOKEN_TIME)
