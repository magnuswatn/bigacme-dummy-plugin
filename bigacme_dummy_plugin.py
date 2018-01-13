"""A dummy plugin for bigacme"""
import time
import logging
from bigacme.plugin import InvalidConfigError, BigacmePlugin

logger = logging.getLogger(__name__)

class DummyPlugin(BigacmePlugin):
    """Dummy DNS Authenticator for bigacme"""

    name = 'bigacme dummy plugin'

    def __init__(self, **kwargs):
        try:
            sleeptime = kwargs.pop('sleeptime')
        except KeyError as error:
            raise InvalidConfigError('Missing config parameter {}'.format(error.args[0]))

        if kwargs:
            raise InvalidConfigError('Unexpected config parameter(s): {}'
                                     .format(', '.join([x for x in kwargs])))

        try:
            self.sleeptime = float(sleeptime)
        except ValueError:
            raise InvalidConfigError('Invalid value for sleeptime')

    def perform(self, domain, validation_name, validation):
        logger.debug('Performing...')
        print('Add the following record: {} with content: {} for domain: {}'
              .format(validation_name, validation, domain))

    def finish_perform(self):
        print('Remeber to publish that zone! I\'ll wait while you do that.')
        time.sleep(self.sleeptime)

    def cleanup(self, domain, validation_name, validation):
        logger.debug('Cleaning up...')
        print('Delete the following record: {} with content: {} for domain: {}'
              .format(validation_name, validation, domain))

    def finish_cleanup(self):
        print('Remeber to publish that zone again.')
