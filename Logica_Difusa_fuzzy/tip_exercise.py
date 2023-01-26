import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')

# print(quality.universe)

tip = ctrl.Consequent(np.arange(0, 21, 1), 'tip')

quality.automf(number=3, names=['bad', 'good', 'tasty'])
service.automf(number=3, names=['bad', 'ok', 'good'])

tip['low'] = fuzz.sigmf(tip.universe, 5, -1)
tip['medium'] = fuzz.gaussmf(tip.universe, 10, 3)
tip['high'] = fuzz.pimf(tip.universe, 10, 20, 20, 21)

rule1= ctrl.Rule(quality['bad'] | service['bad'], tip['low'])
rule2= ctrl.Rule(service['ok'], tip['medium'])
rule3= ctrl.Rule(service['good'] | quality['tasty'], tip['high'])

controlSystem = ctrl.ControlSystem([rule1, rule2, rule3])

system = ctrl.ControlSystemSimulation(controlSystem)

system.input['quality'] = 10
system.input['service'] = 10
system.compute()

print(system.output['tip'])
tip.view(sim = system)