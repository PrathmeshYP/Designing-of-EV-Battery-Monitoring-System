
# State of Health (SoH) Module


def estimate_soh(voltage, temperature, current, soc):
    """
    Estimate State of Health (SoH) using voltage, temperature,
    current, and SoC.
    Returns SoH in percentage (0–100).
    """

    # ---- Coefficients (tune as required) ----
    a0 = 68.0
    a1 = 4.2     # voltage factor
    a2 = -0.8    # temperature factor
    a3 = 0.5     # current factor
    a4 = 0.1     # SoC factor

    soh = a0 + (a1 * voltage) + (a2 * temperature) + (a3 * current) + (a4 * soc)
    return max(0, min(100, soh))

