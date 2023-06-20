from datetime import datetime


def get_rounded_iso_timestamp() -> str:
    """
    Returns a string representing the current time rounded to the nearest 10 seconds.
    :return: str
    """
    now = datetime.utcnow()
    rounded_seconds = (now.second // 10) * 10
    rounded_time = now.replace(second=rounded_seconds, microsecond=0)
    iso_timestamp = rounded_time.isoformat() + "Z"
    return iso_timestamp


def string_to_date(date: str) -> datetime:
    """
    Converts a string to a datetime object.
    :param date: str
    :return: datetime
    """
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
