import time
from itertools import cycle


class TrafficLight:
    __color = 'red'

    def running(self):
        cycler = cycle(['green', 'red'])
        while True:
            if self._TrafficLight__color != 'yellow':
                print(self._TrafficLight__color)
                time.sleep(5)
                self._TrafficLight__color = 'yellow'
            else:
                print(self._TrafficLight__color)
                time.sleep(2)
                self._TrafficLight__color = next(cycler)


a = TrafficLight()
a.running()
