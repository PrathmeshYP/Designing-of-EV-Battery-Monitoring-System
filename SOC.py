# soc.py
# ===============================
# State of Charge (SoC) Module
# ===============================

# Battery voltage limits
MAX_V = 8.4     # Fully charged voltage
MIN_V = 6.0     # Fully discharged voltage

def compute_soc(voltage):
    """
    Calculate State of Charge (SoC) based on battery voltage.
    Returns SoC in percentage (0–100).
    """
    soc = (voltage - MIN_V) / (MAX_V - MIN_V) * 100
    return max(0, min(100, soc))
