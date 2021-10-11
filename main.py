from modules.Weather import Weather
from modules.Pedestrian import Pedestrian
import lgsvl

sim = lgsvl.Simulator("127.0.0.1", 8181)

weather_module = Weather()
pedestrian_module = Pedestrian()

for _ in range(5):
    if sim.current_scene == "BorregasAve":
        sim.reset()
    else:
        sim.load("BorregasAve")

    spawns = sim.get_spawn()

    state = lgsvl.AgentState()
    state.transform = spawns[0]

    ego = sim.add_agent("2e9095fa-c9b9-4f3f-8d7d-65fa2bb03921", lgsvl.AgentType.EGO, state)

    weather_module.generate(sim)
    pedestrian_module.generate(sim)

    sim.run(10)
