import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as cl
import matplotlib.pyplot as plt

luong_gao = int(input('Nhập lượng gạo: '))
thoi_gian = int(input('Nhập thời gian nấu: '))


rice = cl.Antecedent(np.arange(100, 1100, 100), 'rice')
time = cl.Antecedent(np.arange(10, 130, 10), 'time')
power = cl.Consequent(np.arange(0, 110, 10), 'power')

rice['Rất ít'] = fuzz.trimf(rice.universe, [100, 100, 200])
rice['Ít'] = fuzz.trimf(rice.universe, [100, 200, 400])
rice['Trung bình'] = fuzz.trimf(rice.universe, [200, 500, 800])
rice['Nhiều'] = fuzz.trimf(rice.universe, [600, 800, 1000])
rice['Rất nhiều'] = fuzz.trimf(rice.universe, [800, 1000, 1000])

time['Ít'] = fuzz.trimf(time.universe, [10, 10, 20])
time['Rất ít'] = fuzz.trimf(time.universe, [10, 20, 30])
time['Trung bình'] = fuzz.trimf(time.universe, [20, 60, 100])
time['Nhiều'] = fuzz.trimf(time.universe, [80, 100, 120])
time['Rất nhiều'] = fuzz.trimf(time.universe, [100, 120, 120])

power['Rất ít'] = fuzz.trimf(power.universe, [0, 0, 20])
power['Ít'] = fuzz.trimf(power.universe, [0, 20, 40])
power['Trung bình'] = fuzz.trimf(power.universe, [40, 60, 80])
power['Nhiều '] = fuzz.trimf(power.universe, [80, 90, 100])
power['Rất nhiều'] = fuzz.trimf(power.universe, [90, 100, 100])

names_rice = ['Rất ít', 'Ít', 'Trung bình', 'Nhiều', 'Rất nhiều']
names_time = ['Rất ít', 'Ít', 'Trung bình', 'Nhiều', 'Rất nhiều']
names_heating = ['Rất ít', 'Ít', 'Trung bình', 'Nhiều', 'Rất nhiều']

rice.automf(names=names_rice)
time.automf(names=names_time)
power.automf(names=names_heating)

rule1 = cl.Rule(rice['Rất ít'] & time['Rất ít'], power['Nhiều'])
rule2 = cl.Rule(rice['Rất ít'] & time['Ít'], power['Nhiều'])
rule3 = cl.Rule(rice['Rất ít'] & time['Trung bình'], power['Trung bình'])
rule4 = cl.Rule(rice['Rất ít'] & time['Nhiều'], power['Ít'])
rule5 = cl.Rule(rice['Rất ít'] & time['Rất nhiều'], power['Rất ít'])

rule6 = cl.Rule(rice['Ít'] & time['Rất ít'], power['Nhiều'])
rule7 = cl.Rule(rice['Ít'] & time['Ít'], power['Nhiều'])
rule8 = cl.Rule(rice['Ít'] & time['Trung bình'], power['Trung bình'])
rule9 = cl.Rule(rice['Ít'] & time['Nhiều'], power['Ít'])
rule10 = cl.Rule(rice['Ít'] & time['Rất nhiều'], power['Rất ít'])

rule11 = cl.Rule(rice['Trung bình'] & time['Rất ít'], power['Rất nhiều'])
rule12 = cl.Rule(rice['Trung bình'] & time['Ít'], power['Nhiều'])
rule13 = cl.Rule(rice['Trung bình'] & time['Trung bình'], power['Trung bình'])
rule14 = cl.Rule(rice['Trung bình'] & time['Nhiều'], power['Ít'])
rule15 = cl.Rule(rice['Trung bình'] & time['Rất nhiều'], power['Rất ít'])

rule16 = cl.Rule(rice['Nhiều'] & time['Rất ít'], power['Rất nhiều'])
rule17 = cl.Rule(rice['Nhiều'] & time['Ít'], power['Rất nhiều'])
rule18 = cl.Rule(rice['Nhiều'] & time['Trung bình'], power['Trung bình'])
rule19 = cl.Rule(rice['Nhiều'] & time['Nhiều'], power['Ít'])
rule20 = cl.Rule(rice['Nhiều'] & time['Rất nhiều'], power['Rất ít'])

rule21 = cl.Rule(rice['Rất nhiều'] & time['Rất ít'], power['Rất nhiều'])
rule22 = cl.Rule(rice['Rất nhiều'] & time['Ít'], power['Rất nhiều'])
rule23 = cl.Rule(rice['Rất nhiều'] & time['Trung bình'], power['Nhiều'])
rule24 = cl.Rule(rice['Rất nhiều'] & time['Nhiều'], power['Trung bình'])
rule25 = cl.Rule(rice['Rất nhiều'] & time['Rất nhiều'], power['Ít'])

system_cl = cl.ControlSystem(rules=[rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11,
                             rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25])
system = cl.ControlSystemSimulation(system_cl)
system.input['rice'] = luong_gao
system.input['time'] = thoi_gian
system.compute()
print("{:.2f}".format(system.output['power'])+'w')
power.view(sim=system)

power.view()
