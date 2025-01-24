def circuit_resistance(*data, connection='serial', conductivity=False):
    if connection == 'serial':
        total_data = sum(data)
    elif connection == 'parallel':
        if any(r == 0 for r in data):
            return 0.0
        total_data = 1 / sum(1 / r for r in data)
    else:
        raise ValueError("Invalid connection type. Use 'serial' or 'parallel'.")

    if conductivity:
        total_data = 1 / total_data if total_data != 0 else float('inf')
    
    return round(total_data, 4)
