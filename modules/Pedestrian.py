import random
import lgsvl


class Pedestrian:

    paths = [
        [
            lgsvl.Vector(-30.1, -1.8, -22.5),
            lgsvl.Vector(-9.3, -1.9, -27.9),
            lgsvl.Vector(12.0, -2.4, -35.1)
        ],
        [
            lgsvl.Vector(-30.1, -1.8, -22.5),
            lgsvl.Vector(-26.3, -1.7, -11.9),
            lgsvl.Vector(-22.5, -1.7, -0.6)
        ],
        [
            lgsvl.Vector(-22.5, -1.7, -0.6),
            lgsvl.Vector(1.4, -2.0, -8.2),
            lgsvl.Vector(19.2, -2.4, -10.1)
        ],
        [
            lgsvl.Vector(19.2, -2.4, -10.1),
            lgsvl.Vector(12.0, -2.4, -35.1)
        ]
    ]

    # "EntrepreneurFemale", "Howard", "Johny", "Pamela", "Presley", "Red", "Robin", "Stephen", "Zoe", 
    pedestrian_types = ["Bob", "SegwayKickScooterMaxG30LP", "Deer", "Turkey"]
    
    def generate(self, sim):
        pedState = lgsvl.AgentState()
        pedState.transform.position = self.paths[0][0]

        npc = sim.add_agent(random.sample(self.pedestrian_types, 1)[0], lgsvl.AgentType.PEDESTRIAN, pedState)
        waypoints = list(map(lambda x: lgsvl.WalkWaypoint(x, idle=1), random.sample(self.paths, 1)[0]))
        npc.follow(waypoints, loop=False)
