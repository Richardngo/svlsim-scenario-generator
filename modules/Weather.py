import random
import lgsvl


class Weather:

    properties = {
        "rain": 0,
        "fog": 0,
        "wetness": 0,
        "cloudiness": 0,
        "damage": 0
    }
    
    def generate(self, sim):

        # randomly select how many properties to set
        num_properties = random.randint(0, len(self.properties.keys()))
        properties_to_set = random.sample(self.properties.keys(), num_properties)

        # set each weather property between 0 and 1
        config = self.properties.copy()
        for k in properties_to_set:
            config[k] = random.uniform(0, 1) 

        # set time of day (hour) randomly between 0 and 24
        config["time_of_day"] = random.randint(0, 24)

        w = lgsvl.simulator.WeatherState(
            config["rain"],
            config["fog"],
            config["wetness"],
            config["cloudiness"],
            config["damage"]
        )

        sim.weather=w

        sim.set_time_of_day(config["time_of_day"])
