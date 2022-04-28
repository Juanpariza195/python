from operator import ne


def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if(efficiency >= 80):
        return 'green'
    if(efficiency < 80 and efficiency >= 60):
        return 'orange'
    if(efficiency < 60 and efficiency >= 30):
        return 'red'
    if(efficiency < 30):
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    TporN = temperature * neutrons_produced_per_second
    thresholdMax = threshold + (threshold * 0.10)
    thresholdMin = threshold - (threshold * 0.10)

    if(TporN < threshold * 0.90):
        return 'LOW'
    elif(TporN <= thresholdMax and TporN >= thresholdMin):
        return 'NORMAL'
    else:
        return 'DANGER'



print(fail_safe(10, 1099, 10000))