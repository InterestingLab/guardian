# encoding: utf-8

import abc


class GuardianAlertBase:
    def __init__(self, name, config):
        self.name = name
        self.config = config

    @abc.abstractmethod
    def send_alert(self, level, subject, objects, content):
        pass

    @abc.abstractmethod
    def check_config(self):
        pass
