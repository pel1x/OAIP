def future(VIN, *masses, **const,):
    
    critical_mass = sum(const.values()) + VIN
    
    total_mass = sum(masses)

    if total_mass < critical_mass:
        return "ACCELERATION"
    elif total_mass > critical_mass:
        return "DECELERATION"
    else:
        return "UNCHANGED"
