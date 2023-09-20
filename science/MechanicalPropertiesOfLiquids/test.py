# take random 10 samples from nlm.json and dump in new json file

import json
import random

with open('science/MechanicalPropertiesOfLiquids/mpl.json', 'r') as f:
    data = json.load(f)

random.shuffle(data)

with open('science/laws_of_motion/nlm_random.json','w') as f:
    json.dump(data[:10],f,indent=4)
    f.close()
