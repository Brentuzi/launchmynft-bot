import os
import json

import launchmy







def getConfig():
        configFile = open("config.json", 'r')
        return list(json.load(configFile).values())



config = getConfig()


isWindows = True if os.name == 'nt' else False


if "launchmynft.io" in config[0]:
    print("Found launchmynft.io link")
    launchmy.mint(config, isWindows)
else:
    print("Could not recognize link")

