import constants as c

class WORLD:
    def __init__(self):
        self.planeId = c.p.loadURDF("plane.urdf")
        self.worldId = c.p.loadSDF("world.sdf")
