"""A dummy plugin for bigacme"""
import time
import logging
from bigacme.plugin import InvalidConfigError

class Authenticator(object):
    """Dummy DNS Authenticator for bigacme"""

    def __init__(self, config):
        for element in config:
            setattr(self, element[0], element[1])

        if not hasattr(self, 'sleeptime'):
            raise InvalidConfigError("Missing 'sleeptime' parameter")

    def perform(self, domain, validation_name, validation):
        print('Add the following record: {} with content: {} for domain: {}'
             .format(validation_name, validation, domain))
        time.sleep(float(self.sleeptime))

    def cleanup(self, domain, validation_name, validation):
        print('Delete the following record: {} with content: {} for domain: {}'
             .format(validation_name, validation, domain))
