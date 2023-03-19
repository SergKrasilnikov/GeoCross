## GeoCross - Drawing of the Geological Cross-Section of the Ejecta Materials on the Moon
Planetary Remote Sensing Laboratory / Department of Land Surveying & Geo-Informatics / 
The Hong Kong Polytechnic University

in cooperation with 

Laboratory of Comparative Planetology / Vernadsky Institute of Geochemistry and Analytical 
Chemistry RAS

---

### Overview
This program builds geological cross-sections of the ejecta deposits on the Moon based on the models: Sharpton (2014), 
Housen et al., (1983) and  Fassett et al., (2011).

```
Sharpton, (2014) - for craters < 45 km
T = 0.033*R*(r/R)^-3

Housen et al., (1983)
T = 0.0078*R*(r/R)^-2.61 - for craters in a diameter range from 45 to 300 km

Fassett et al., (2011) - for impact basins > 300 km
T = 2900(±300)*(r/R)^(- 2.8(±0.5))

In all formulae, r is the distance to the point of interest, R is crater radius; both are in meters.
```
This program allow to draw the fellow geological cross-sections in automatical regime:
![cross-section throw the 9th landing site of the Artemis mission](./data/output/9.jpg)

After correction of the cross-section we have the fellow result:
![cross-section throw the 9th landing site of the Artemis mission](./data/output/final_example.jpg)

---

### Running
Locate 'profile.dbf' with elevation profile in the folder (...\data\elevation\)

Locate layers .dbf files in the folder (...\data\layers\'NUMBER OF LAYER') - starts from the lower layer/layers at the 
zero folder until upper layer at the latest number.

To run this code type in the terminal in the folder with run.py file (...\src\):
```
python run.py \'ABSOLUTE LOCATION OF THE \'data\' DIRECTORY\'
```
Results will be stored in the folder (...\data\output\) in the .jpg and .svg formats.

---

### Author
- Sergey Krasilnikov
### Contributors
- Anastasiia Radaeva
- Azat Almukhametov

---


### How to cite:
The theoretical explanation and application of the program in the envestigation of the 
geological structure of the Artemis landing sites will be published in Krasilnikov et al., (2023).
Some results already used in:
>Krasilnikov, S.S., Ivanov, M.A., Head, J.W., Krasilnikov, A.S., 2023. Geologic history of the south circumpolar
> region (SCR) of the moon. Icarus, 115422.
> 
> Krasilnikov, S.S., Krasilnikov, A.S., Ivanov, M.A., 2022. Geological Details of the Main Landing Ellipses of
> Luna-25. Solar System Research, 56(3), 135-144.