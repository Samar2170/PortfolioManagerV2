import jwt
from django.conf import settings
from datetime import datetime, timedelta,date


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=15)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def generate_refresh_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=15)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')


formatts = ['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%y', '%d-%b-%Y', '%d-%B-%Y',
            '%d-%b-%Y %H:%M:%S', '%d-%B-%Y %H:%M:%S']

def parse_datetime(arg):
    for fmt in formatts:
        try:
            return datetime.strptime(arg, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')

def parse_datetime_series(arg):
    if isinstance(arg, list):
        return [parse_datetime(x) for x in arg]
    else:
        return [parse_datetime(arg)]
