import datetime


def factor_seconds(seconds):
    """
    Converts given number of seconds to tuple (hours, minutes, seconds)
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def convert_seconds_to_iso(seconds):
    """
    Converts given number of seconds to Excel/CSV/ISO time format
    """
    return datetime.time(*factor_seconds(seconds)).isoformat()


def convert_seconds_to_human(seconds):
    """
    Converts seconds to human readable string.
    """
    hours, minutes, _ = factor_seconds(seconds)
    return ("{}h ".format(hours) if hours else "") + "{}m".format(minutes)
