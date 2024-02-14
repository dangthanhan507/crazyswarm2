"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from crazyflie_py import Crazyswarm
import numpy as np

TAKEOFF_DURATION = 5.0
HOVER_DURATION = 10.0
import numpy as np

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    print(swarm.allcfs.crazyflies)
    cf = swarm.allcfs.crazyflies[0]
    # cf1 = swarm.allcfs.crazyflies[1]

    cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    # cf1.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    
    # timeHelper.sleep(TAKEOFF_DURATION+5.0)
    # pos = np.array(cf.initialPosition) + np.array([0.5, 0.0, 1.0])
    # cf.goTo(pos, 0, 3.0)
    # timeHelper.sleep(10.0)
    
    # pos = np.array(cf.initialPosition) + np.array([-0.5, 0.0, 1.0])
    # cf.goTo(pos, 0, 3.0)
    # timeHelper.sleep(10.0)
    
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    cf.land(targetHeight=0.04, duration=5)
    # cf1.land(targetHeight=0.04, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)


if __name__ == '__main__':
    main()
