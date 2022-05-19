from datetime import datetime

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