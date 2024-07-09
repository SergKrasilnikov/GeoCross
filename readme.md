## GeoCross - Geological Cross-Section Mapping of the Ejecta Materials on the Moon

---
Planetary Remote Sensing Laboratory / The Hong Kong Polytechnic University & Laboratory of Comparative Planetology / 
Vernadsky Institute of Geochemistry and Analytical Chemistry RAS

### Author
- [Sergey Krasilnikov](https://github.com/SergKrasilnikov)
### Contributors
- [Anastasiia Radaeva](https://github.com/AnastasiiaRadaeva)
- [Azat Almukhametov](https://github.com/gigabotan)

---

### Overview
This program builds geological cross-sections of the ejecta deposits on the Moon based on the models: Sharpton (2014), 
Housen et al., (1983) and  Fassett et al., (2011).

Sharpton, (2014) - for craters < 45 km in diameter:

$$T = 0.033\*R*(r/R)^{-3}$$

Housen et al., (1983) - for craters in a diameter range from 45 to 300 km:

$$T = 0.0078\*R*(r/R)^{-2.61}$$

Fassett et al., (2011) - for impact basins > 300 km:

$$T = 2900(±300)*(r/R)^{(- 2.8(±0.5))}$$

In all formulae, r is the distance to the point of interest, and R is the crater radius (both are in meters).


This program allows drawing the geological cross-sections of ejecta materials in an automatical regime (Fig. 1.A).
After manually correcting the profile using the geologic map (Krasilnikov et al., 2023), the cross-section starts 
looking closer to the classical view (Fig. 1.B).

<image
    src="./data/readme_images/fig1.jpg"
    alt="Cross-section of the Artemis mission's landing site"
    title="Fig. 1. Cross-section throw the 1st and 2d landing sites of the Artemis mission."
    height="400"/>

Fig. 1. Cross-section throw the 1st and 2d landing sites of the Artemis mission.

---

### Pre-procassing stage
Preparation of data conducted in the GIS program (ArcGis - in my example).

(1) The profile on the surface.
Drawing a line on the surface. It will be a profile of the cross-section. Build points along the line with 100 m 
intervals ("Creating new points along a line"). Better to "Include End Points".

(2) Get X, Y, Z attributes.
"Add Field" "x" and "y" (Double type) in the attribute table in meters. Use "Extract Values to Points" to extract "z" 
values. Export the file as "profile.dbf" ("Export" in the attribute table).

<image
    src="./data/readme_images/fig2.jpg"
    alt="Measuring the distance between the crater centre and each profile point"
    title="Fig. 2. Measuring the distance between the crater centre and each profile point."
    height="400"/>

Fig. 2. Measuring the distance between the crater centre and each profile point.

(3) Calculate the distance from the crater to the points.
Using points in the centre of each crater from which you want to calculate ejecta thickness, calculate the distance 
between this point and the profiles' points (Point Distance) (Fig. 2). Add a column named "DIAM" with a diameter of 
the crater in km. Export this file as .dbf ("Export" in the attribute table). Open it and sort values "NEAR_FID" 
(could be done in LibreOffice). Make the same movements for all craters, which ejecta could be found in the area of 
your cross-section.

(4) Naming of .dbf files.
The .dbf file with the profile should be called "profile.dbf". The layers files with distances between craters and 
cross-section points should be called by numbers (like "0.dbf"). IF 0-IS LOWER LAYER AT THE CROSS-SECTION.

(5) Location of the files.
Add all files to the program folders.
Locate 'profile.dbf' with elevation profile in the folder `(...\data\elevation\)`

---

### Running
To run this code type in the terminal in the folder with `...\src\`:

`python run.py \'ABSOLUTE LOCATION OF THE \'data\' DIRECTORY\'`

Results will be stored in the folder `(...\data\output\)` in the .jpg and .svg formats.

You can correct plot settings if axes are wrong in the file `(...\src\geo_cross\functions\plotting\plot.py`.


---


### How to cite:
The theoretical explanation and application of the program in the investigating the 
geological structure of the Artemis landing sites was published in Krasilnikov et al., (2024).
Some results already used in Krasilnikov et al., (2022, 2023a, 2023b):

>Krasilnikov, A.S., Ivanov, M.A., Krasilnikov, S.S., Head, J.W., 2024. Stratigraphic cross-sections, geologic history, 
> and provenance of material at the candidate landing sites of the Artemis missions. Icarus, 420, 116190.

>Krasilnikov, S.S., Ivanov, M.A., Head, J.W., Krasilnikov, A.S., 2023a. Geologic history of the south circumpolar
> region (SCR) of the Moon. Icarus, 394, 115422.
> 
>Krasilnikov, A.S., Krasilnikov, S.S., Ivanov, M.A., Head, J.W., 2023b. Estimation of ejecta thickness from impact 
> craters in the South polar region of the Moon, Solar System Research, Vol. 57, No. 2, pp. 122–132.
> 
>Krasilnikov, S.S., Krasilnikov, A.S., Ivanov, M.A., 2022. Geological Details of the Main Landing Ellipses of
> Luna-25. Solar System Research, 56(3), 135-144.
