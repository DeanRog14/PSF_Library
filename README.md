# Texas PSF Library

The goal behind this library is to have  shortcuts for commonly used functions or actions within finance. To help reduce time spent on building, improve accuracy on calculations, and ensure consistent results. The library is split up into 4 major groups cleaning, calculations, plotting, and building. Each work together to help improve workflows, by cleaning the data so it works properly for different calculations and graphs. 

Different Packages:
1. Cleaning - getting basic info about data and cleaning any data
2. Calculations - ensuring accuracy and speeding up the time it takes to do calculations
3. Plotting - enables customizable graphs, with colors, axes modifications, and labeling different areas on the graphs
4. Building - allows for transforming some graphs to work in pdf format

## Installation

To install:

`pip install psf_library`

**psf_library** should be the location of where you have the library located in your computer. 

## How To Use
Loading the library in properly:

``` 
import psf_library as psf
import psf_library.plotting as psf_plot
import psf_library.calcs as psf_calc
import psf_library.cleaning as psf_clean
import psf_library.building as psf_build
```
This is how all the different parts of the library can be loaded in and used within your code. The part after the **as** can be changed to whatever you want the name to be, but these are the names that I recommend. 
