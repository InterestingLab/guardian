# encoding: utf-8

import logging

from alert.alert_factory import GuardianAlertFactory

from alert.alert_util import (UnsupportedAlertMethod, IncorrectConfig,
                              AlertException)


class GuardianAlert(object):

    def __init__(self, alert_config):
        self.alert_config = alert_config
        self.alerts = self.create_alert()
        self.check_config()

    def create_alert(self):
        alerts = []
        for method in self.alert_config:
            try:
                alerts.append(GuardianAlertFactory.render_alert(
                    method,
                    self.alert_config))
            except Exception as e:
                logging.error(e)
                raise UnsupportedAlertMethod(e)

        return alerts

    def send_alert(self, level, subject, objects, content):
        for alert in self.alerts:
            try:
                alert.send_alert(level, subject, objects, content)
            except AlertException as e:
                logging.error(
                    'failed to send alert, caught exception: ' + repr(e))

    def check_config(self):
        for alert_impl in self.alerts:
            if not alert_impl.check_config():
                raise IncorrectConfig("Incorrect Config: " + alert_impl.name)
