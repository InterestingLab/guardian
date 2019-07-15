# encoding: utf-8

from alert.emails import Emails
from alert.webhook import Webhook
from alert.alert_util import UnsupportedAlertMethod


class GuardianAlertFactory:
    def __init__(self):
        pass

    @staticmethod
    def render_alert(name, config):
        if name == "emails":
            return Emails(name, config)
        elif name == "webhook":
            return Webhook(name, config)
        else:
            raise UnsupportedAlertMethod(
                "Unsupported alert method: {}".format(name))
