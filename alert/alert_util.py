# encoding: utf-8


def match_alert(routes, level):
    if level in routes['match']['level']:
        return True
    else:
        return False


class AlertException(Exception):
    pass


class UnsupportedAlertMethod(AlertException):
    pass


class IncorrectConfig(AlertException):
    pass
