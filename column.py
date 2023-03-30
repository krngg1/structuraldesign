import math

# Input data
b = float(input("Enter the width of the column (mm): "))
h = float(input("Enter the height of the column (mm): "))
L = float(input("Enter the height of the building (m): "))
fck = float(input("Enter the grade of concrete (MPa): "))
fy = float(input("Enter the grade of steel (MPa): "))
P = float(input("Enter the axial load on the column (kN): "))
Zone_Factor = int(input("Enter the zone factor (1-5): "))

# Calculate design parameters
Ac = b * h
As = math.pi * (12**2) / 4
Lb = min(b, h)
Le = 2.5 * Lb
lambda_ = Le / math.sqrt(Ac)
gamma_M = 1.5
gamma_C = 1.5
phi = 0.8
K = 1

# Calculate earthquake loads
Ag = b * h
Z = 0.16 + (0.035 * Zone_Factor)
Ie = 1.0
A_h = Ag * Z * Ie
S_DS = float(input("Enter the design spectral acceleration value (m/s^2): "))
S_D1 = 0.8 * S_DS
S_M = 1.5 * S_D1
R = float(input("Enter the response reduction factor (1.0-8.0): "))
V = R * S_M * A_h / 1000.0

# Determine critical buckling load
Es = fy / 1.15
sigma_c = 0.67 * fck / 1.5
Ncr = (math.pi ** 2) * Es * Ac / (Le ** 2)

# Calculate design compressive strength
alpha = 0.8
fcd = alpha * sigma_c
Acf = 0.85 * (1 - (fcd / (phi * fck)))
N = Acf * phi * fck * Ac + phi * As * fy

# Verify code compliance
if N >= P * gamma_M:
    print("The column is safe under axial load.")
else:
    print("The column is not safe under axial load.")
    
if N >= V * gamma_C:
    print("The column is safe under earthquake load.")
else:
    print("The column is not safe under earthquake load.")
    
if lambda_ <= 32:
    print("The slenderness ratio is within permissible limits.")
else:
    print("The slenderness ratio is not within permissible limits.")
