# encoding: utf-8

import json
import httplib
from alert.alert_base import GuardianAlertBase
from urlparse import urlparse

from alert_util import match_alert, AlertException


class Webhook(GuardianAlertBase):

    def send_alert(self, level, subject, objects, content):

        alert_config = self.config['webhook']
        url = alert_config['url']
        params = {
            'subject': subject,
            'objects': objects,
            'content': content
        }

        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'Accept': 'text/plain'
        }

        if match_alert(alert_config['routes'], level):
            url_info = urlparse(url)
            port = 80 if url_info.port is None else url_info.port
            try:
                http_client = httplib.HTTPConnection(url_info.hostname,
                                                     port, timeout=5)
                http_client.request("POST", url_info.path,
                                    json.dumps(params), headers)
            except Exception as e:
                raise AlertException(e)

    def check_config(self):
        alert_config = self.config['webhook']
        if 'url' not in alert_config or 'routes' not in alert_config:
            return False
        else:
            return True
