#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ellipsoid parameters (Clarke 1880)

a = 6378249.145
inverse_f = 293.465


# In[2]:


f=1/inverse_f
print("Flattening (f):",f)


# In[3]:


# Calculate first eccentricity squared

e2 = 2 * f - f**2

print("First eccentricity squared (e2):", e2)


# In[4]:


# Define geographical coordinates of JKUAT

phi_deg = -1.091520
lambda_deg = 37.014007
Az_deg = 20


# In[5]:


# Determine UTM zone and central meridian

zone = int((lambda_deg + 180) / 6) + 1

lambda0_deg = 6 * zone - 183

phi0_deg = 0

print("UTM Zone:", zone)
print("Central Meridian:", lambda0_deg)
print("Latitude of Origin:", phi0_deg)


# In[6]:


import math

# Convert degrees to radians

phi = math.radians(phi_deg)
lambda_rad = math.radians(lambda_deg)
lambda0 = math.radians(lambda0_deg)
phi0 = math.radians(phi0_deg)
Az = math.radians(Az_deg)

print("Latitude in radians:", phi)
print("Longitude in radians:", lambda_rad)
print("Central meridian in radians:", lambda0)
print("Latitude of origin in radians:", phi0)
print("Azimuth in radians:", Az)


# In[7]:


# Calculate radius of curvature in the prime vertical (N)

N = a / math.sqrt(1 - e2 * math.sin(phi)**2)

print("Radius of curvature (N):", N, "m")


# In[8]:


# Calculate T

T = math.tan(phi)**2

print("T:", T)


# In[9]:


# Calculate A

A = (lambda_rad - lambda0) * math.cos(phi)

print("A:", A)


# In[10]:


# Calculate C

C = (e2 * math.cos(phi)**2) / (1 - e2)

print("C:", C)


# In[11]:


# Calculate meridional arc (M)

M = a * (
    (1 - e2/4 - 3*e2**2/64 - 5*e2**3/256) * phi
    - (3*e2/8 + 3*e2**2/32 + 45*e2**3/1024) * math.sin(2*phi)
    + (15*e2**2/256 + 45*e2**3/1024) * math.sin(4*phi)
    - (35*e2**3/3072) * math.sin(6*phi)
)

print("Meridional arc (M):", M, "m")


# In[12]:


# Calculate meridional arc at the origin (M0)

M0 = a * (
    (1 - e2/4 - 3*e2**2/64 - 5*e2**3/256) * phi0
    - (3*e2/8 + 3*e2**2/32 + 45*e2**3/1024) * math.sin(2*phi0)
    + (15*e2**2/256 + 45*e2**3/1024) * math.sin(4*phi0)
    - (35*e2**3/3072) * math.sin(6*phi0)
)

print("Meridional arc at origin (M0):", M0, "m")


# In[13]:


# Calculate Easting (x)

x = N * (
    A
    - (T * A**3) / 6
    - ((8 - T + 8*C) * T * A**5) / 120
)

print("Easting (x):", x, "m")


# In[14]:


# Calculate Northing (y)

y = M - M0 + N * math.tan(phi) * (
    A**2 / 2
    + ((5 - T + 6*C) * A**4) / 24
)

print("Northing (y):", y, "m")


# In[17]:


# Calculate scale factor (s)

s = 1 + (
    x**2 * math.cos(Az)**2 * (1 - e2 * math.sin(phi)**2)**2
) / (2 * a**2 * (1 - e2))

print("Scale factor (s):", s)


# In[18]:


# Display final results

print("FINAL RESULTS FOR JKUAT")
print("-------------------------")
print("Easting (x):", x, "m")
print("Northing (y):", y, "m")
print("Scale factor (s):", s)


# In[ ]:




