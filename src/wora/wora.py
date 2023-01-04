from datetime import datetime

def timestamp(fmt: str) -> str:
    ''' Format timestamps for the current datetime '''
    return datetime.now().strftime(fmt)
