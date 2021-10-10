from modules.Weather import Weather
import lgsvl

sim = lgsvl.Simulator("127.0.0.1", 8181)

weather_module = Weather()

for _ in range(10):
    if sim.current_scene == "BorregasAve":
        sim.reset()
    else:
        sim.load("BorregasAve")

    spawns = sim.get_spawn()

    state = lgsvl.AgentState()
    state.transform = spawns[0]

    ego = sim.add_agent("2e9095fa-c9b9-4f3f-8d7d-65fa2bb03921", lgsvl.AgentType.EGO, state)

    weather_config = weather_module.generate()

    # w = sim.weather
    w = lgsvl.simulator.WeatherState(
        weather_config["rain"],
        weather_config["fog"],
        weather_config["wetness"],
        weather_config["cloudiness"],
        weather_config["damage"]
    )

    sim.weather=w

    sim.set_time_of_day(weather_config["time_of_day"])

    sim.run(5)
