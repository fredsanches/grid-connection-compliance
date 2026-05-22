# Regulatory Compliance Framework

All analyses and automated validations are designed to strictly comply with the requirements defined by ANEEL (Agência Nacional de Energia Elétrica).

## PRODIST Módulo 8

Our compliance engine checks steady-state voltage deviation limits as defined by **PRODIST Módulo 8 (Quality of Electric Energy)**.

### Voltage Deviation Limits
Steady-state voltage at the Point of Common Coupling (PCC) must be maintained within the following range:

$$0.95 \le V_{pu} \le 1.05$$

Where:
- $V_{pu}$ is the per-unit voltage calculated relative to the nominal voltage of the grid segment.

### Grid Integration Impact Study
When simulating a Distributed Generation (DG) power plant:
1. **Base Case:** Evaluate the feeder's voltage profile under standard loading conditions without generation.
2. **Generation Case:** Inject the DG power plant's peak capacity at the PCC.
3. **Assessment:** Verify if the voltage profile remains within the PRODIST limits ($0.95 \le V_{pu} \le 1.05$) and verify conductor thermal limits (ampacity).
4. **Contestation Strategy:** If the utility claims upgrade requirements are needed, we use the simulation results to check if the utility's expansion plans are truly necessary or if they can be avoided by optimizing control settings (e.g., active/reactive power control curves on the generator inverters).
