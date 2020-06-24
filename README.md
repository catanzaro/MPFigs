# Code for multiparameter persistence figures

A repository for creating plotly figures for understanding
multiparameter persistent homology. 

## Motivation

The idea behind multiparameter persistence is to study how shapes or datasets (or whatever you'd like to study) change as multiple parameters vary. Traditionally, ordinary persistence focus on sub-level thresholding, meaning taking various truncations of an object, and seeing what properties change or persistence as a function of the truncation parameter. 
In multiparameter persistence, the idea is the same, but now we look at multiple ways of truncating a shape simultaneously. 

What we focus on here is truncating objects which have been deformed. One example is the wrinkled cylinder introduced below. One way to think about the wrinkled cylinder is to take an ordinary cylinder and push in on the side of it. A more theoretical perspective is to view it as a one-parameter family of deformations of an ordinary circle: at either end of the wrinkled cylinder, the slices (or level-sets) are still circles, but in the middle you see the slices acquires an additional maximum and minimum. Thresholding this object gives a simple yet still visualizable example of the types of objects we're interested in studying.

## Contents 
* The `Wrinkled_cylinder` directory contains:
  - the main code, `wrinkled_cylinder.py` for making plotly figures of the wrinkled cylinder;
  - a modified version, 'wrinkled_cylinder_with_thresh.py' for making thresholded or sliced versions of the wrinkled cylinder to better understand its persistence. For example, by just change the z-range to [-2,-0.5], one can easily see the hole in the surface, generating a first homology class (see the figure below);
  - a modified version, 'wrinkled_cylinder_slices.py' for just drawing the traces of the deformation; and
  - the 'Output_html_files' directory, containing a bunch of samples of thresholding.


* `Slider_tests` contains (deprecated) code for creating interactive versions of thresholding using native plotly and making a dash app.

* `old_tests` contains misc. old code

### Examples

The wrinkled cylinder

![The wrinkled cylinder](./figs/Wrinkled_cylinder.png)

A thresholded version of the wrinkled cylinder.
 
![A thresholded wrinkled cylinder](./figs/thresh.png)

### Interactive versions

I think the best intuition is obtained by messing with these in real time. Here are interactive versions of the above two static pictures. You can also find them in the above directory.

 * [Wrinkled_cylinder/Wrinkled_cylinder.html](https://rawcdn.githack.com/catanzaromj/MPFigs/293e30202cfbd950163c9af91008de8e970b6bd4/Wrinkled_cylinder/Wrinkled_cylinder.html)
 * [Wrinkled_cylinder/Wrinkled_cylinder_thresh.html](https://rawcdn.githack.com/catanzaromj/MPFigs/293e30202cfbd950163c9af91008de8e970b6bd4/Wrinkled_cylinder/Wrinkled_cylinder_thresh.html).

