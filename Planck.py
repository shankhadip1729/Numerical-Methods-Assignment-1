import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

# Constants
T_cmb = 2.725  # Temperature of the cosmic microwave background (CMB) in Kelvin

# Planck's law for black body radiation
def black_body_spectrum(frequency, temperature):
    exponent = h * frequency / (k * temperature)
    intensity = ((2 * h * frequency ** 3 / (c ** 2)) / (np.exp(exponent) - 1))*(10**20)
    return intensity

# Load data from COBE FIRAS
data = np.loadtxt("CMB data.txt")

# Extract frequency and CMB flux
frequency = data[:, 0]*100*c
cmb_flux = data[:, 1]

# Plotting
plt.figure(figsize=(10, 6))

# Plot black body spectrum
plt.plot(frequency, black_body_spectrum(frequency, T_cmb), label='Black Body Spectrum (CMB)')

# Plot CMB flux
plt.plot(frequency, cmb_flux, label='COBE/FIRAS CMB Flux', linestyle='--')

# Find wavelength at which the black body spectrum peaks
wavelength_peak = h * c / (k * T_cmb)
print(f"The wavelength at which the black body spectrum peaks is approximately {wavelength_peak:.2e} meters.")

# Set labels and legend
plt.xlabel('Frequency (Hz)')
plt.ylabel('Intensity')
plt.legend()

# Save the plot to a PDF file
plt.savefig('black_body_spectrum_and_cmb_flux.pdf')

# Show the plot
plt.show()
