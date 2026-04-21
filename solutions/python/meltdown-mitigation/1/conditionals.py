def is_criticality_balanced(temperature, neutrons_emitted):
    # Διορθώθηκε το όνομα της μεταβλητής (neutrons αντί για neurons)
    # Μπορείς να επιστρέψεις το αποτέλεσμα της σύγκρισης απευθείας!
    return (temperature < 800 and 
            neutrons_emitted > 500 and 
            temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    
    if efficiency >= 80:
        return 'green'
    if efficiency >= 60: # Δεν χρειάζεται "and < 80", το πρώτο if το καλύπτει
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    val = temperature * neutrons_produced_per_second
    
    # 90% του threshold
    low_bound = 0.9 * threshold
    # 110% του threshold (για το +10%)
    high_bound = 1.1 * threshold
    
    if val < low_bound:
        return 'LOW'
    # Έλεγχος αν είναι εντός του +/- 10%
    if low_bound <= val <= high_bound:
        return 'NORMAL'
    return 'DANGER'