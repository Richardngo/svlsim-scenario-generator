from environs import Env
import lgsvl

print("Python API Quickstart #4: Ego vehicle driving straight")
env = Env()

sim = lgsvl.Simulator(env.str("LGSVL__SIMULATOR_HOST", lgsvl.wise.SimulatorSettings.simulator_host), env.int("LGSVL__SIMULATOR_PORT", lgsvl.wise.SimulatorSettings.simulator_port))
if sim.current_scene == lgsvl.wise.DefaultAssets.map_borregasave:
    sim.reset()
else:
    sim.load(lgsvl.wise.DefaultAssets.map_borregasave)


spawns = sim.get_spawn()

state = lgsvl.AgentState()
state.transform = spawns[0]


npc = sim.add_agent("Bob", lgsvl.AgentType.PEDESTRIAN)
waypoints = [
    lgsvl.WalkWaypoint(lgsvl.Vector(1,0,3), 5, 0),
    lgsvl.WalkWaypoint(lgsvl.Vector(5,0,3), 10, 0),
    lgsvl.WalkWaypoint(lgsvl.Vector(1,0,5), 5, 0),
]
npc.follow(waypoints, loop=False)

# Agents can be spawned with a velocity. Default is to spawn with 0 velocity
ego = sim.add_agent(env.str("LGSVL__VEHICLE_0", lgsvl.wise.DefaultAssets.ego_lincoln2017mkz_apollo5), lgsvl.AgentType.EGO, state)

# The bounding box of an agent are 2 points (min and max) such that the box formed from those 2 points completely encases the agent
print("Vehicle bounding box =", ego.bounding_box)

print("Current time = ", sim.current_time)
print("Current frame = ", sim.current_frame)

input("Press Enter to drive forward for 2 seconds")

# The simulator can be run for a set amount of time. time_limit is optional and if omitted or set to 0, then the simulator will run indefinitely
sim.run(time_limit=2.0)

print("Current time = ", sim.current_time)
print("Current frame = ", sim.current_frame)

input("Press Enter to continue driving for 2 seconds")
