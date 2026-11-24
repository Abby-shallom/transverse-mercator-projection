# Transverse Mercator Projection Using Python

## 1. Project Overview

This project demonstrates the implementation of the Transverse Mercator projection using Python. It involves applying mathematical equations to transform geographic coordinates (latitude and longitude) into projected coordinates (Easting and Northing), and calculating the scale factor at a given point.

The computation uses the Clarke 1880 reference ellipsoid.

## 2. Objectives

The main objectives of this project are:

- To understand the mathematical principles of the Transverse Mercator projection.
- To implement the Transverse Mercator projection equations using Python.
- To calculate the Easting and Northing coordinates of a given point.
- To determine the scale factor at the point of interest.
- To develop practical programming skills in geodetic computations.

## 3. Input Parameters

The following parameters were used in the computation:

### Reference Ellipsoid: Clarke 1880

| Parameter | Value |
|---|---:|
| Semi-major axis (a) | 6,378,249.145 m |
| Inverse flattening (1/f) | 293.465 |

### Geographic Coordinates

| Parameter | Value |
|---|---:|
| Latitude (φ) | 1.091520° S |
| Longitude (λ) | 37.014007° E |
| Azimuth (Az) | 20° |

### Projection Parameters

| Parameter | Value |
|---|---:|
| UTM Zone | 37S |
| Central Meridian | 39° E |
| Latitude of Origin | 0° |

## 4. Methodology

The computation was carried out through the following steps:

1. Defined the Clarke 1880 ellipsoid parameters.
2. Calculated the flattening and first eccentricity squared.
3. Defined the geographic coordinates of the point of interest.
4. Determined the UTM zone and central meridian.
5. Converted angular measurements from degrees to radians.
6. Calculated the required projection parameters: N, T, A and C.
7. Calculated the meridional arc (M) and meridional arc at the origin (M₀).
8. Computed the Easting (x) and Northing (y).
9. Calculated the scale factor (s).
10. Displayed the final results.

## 5. Mathematical Formulas

The implementation follows the Transverse Mercator projection equations, including:

- Easting (x)
- Northing (y)
- Scale Factor (s)
- Radius of curvature in the prime vertical (N)
- Meridional arc (M)

The equations are implemented using Python's mathematical functions.

## 6. Tools and Technologies

- **Python:** Used to implement the projection equations and perform calculations.
- **Jupyter Notebook:** Used for step-by-step development and testing.
- **Visual Studio Code:** Used to execute and verify the Python script.
- **Math Library:** Used for trigonometric functions, square roots and angle conversions.
- **GitHub:** Used to store and manage the project files.

## 7. Repository Contents

This repository contains:

- `transverse_mercator_jkuat.ipynb` – Jupyter Notebook containing the step-by-step implementation.
- `transverse_mercator_jkuat.py` – Python script containing the projection calculations.
- `README.md` – Project documentation.

## 8. Output

The program displays the following results:

- **Easting (x):** Projected Easting coordinate in metres.
- **Northing (y):** Projected Northing coordinate in metres.
- **Scale Factor (s):** Scale factor at the point of interest.

## 9. Conclusion

This project demonstrates how Python can be applied in geodetic computations to implement the Transverse Mercator projection. It provides practical experience in translating mathematical equations into computer code and applying them to coordinate projection problems.
