#& "C:\Program Files\Python312\python.exe" -m pip install networkx
#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx



import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'Temperature')
humid = ctrl.Antecedent(np.arange(0, 101, 1), 'Humidity')
fan = ctrl.Consequent(np.arange(0, 101, 1), 'FanSpeed')

# Membership functions
temp['low'] = fuzz.trimf(temp.universe, [0, 0, 20])
temp['medium'] = fuzz.trimf(temp.universe, [10, 20, 30])
temp['high'] = fuzz.trimf(temp.universe, [20, 40, 40])

humid['low'] = fuzz.trimf(humid.universe, [0, 0, 50])
humid['high'] = fuzz.trimf(humid.universe, [50, 100, 100])

fan['slow'] = fuzz.trimf(fan.universe, [0, 0, 50])
fan['medium'] = fuzz.trimf(fan.universe, [25, 50, 75])
fan['fast'] = fuzz.trimf(fan.universe, [50, 100, 100])

# Rules
rule1 = ctrl.Rule(temp['high'] | humid['high'], fan['fast'])
rule2 = ctrl.Rule(temp['medium'], fan['medium'])
rule3 = ctrl.Rule(temp['low'] & humid['low'], fan['slow'])

# Control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# ---- User Input ----
t = float(input("Enter Temperature (0-40): "))
h = float(input("Enter Humidity (0-100): "))
fan_sim.input['Temperature'] = t
fan_sim.input['Humidity'] = h
fan_sim.compute()

print(f"Recommended Fan Speed: {fan_sim.output['FanSpeed']:.2f}")

'''
Fuzzy logic is a way for computers to make smart decisions like humans —
it doesn’t say only YES or NO, but also things like MAYBE, A LITTLE, or MOSTLY.
Humans don’t suddenly say “HOT” or “COLD” — we say “a little hot” or “somewhat cool.”
Fuzzy logic helps machines think the same way.
Fuzzy Logic (Smart computer):
If temperature is a little hot → fan speed = 40%
If medium hot → fan speed = 70%
If very hot → fan speed = 100%
(Gradual changes ✅ — more natural)
'''