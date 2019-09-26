from phue import Bridge

from gardnr import drivers, logger


class Hue(drivers.Power):

    def setup(self):
        self.bridge = Bridge(self.bridge_address)
        self.bridge.connect()

    def on(self):
        logger.info('turning on light {}'.format(self.light_number))
        self.bridge.set_light(int(self.light_number), 'on', True)

    def off(self):
        logger.info('turning off light {}'.format(self.light_number))
        self.bridge.set_light(int(self.light_number), 'on', False)
