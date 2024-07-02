









# NOTE: -=-=-=- PROTOTYPE SLICER PIPELINE -=-=-=-
"""
Stage 1: Image/file handling
-   Reads in necessary cubes, etc. and pulls information from the header to create WCS objects, get pixel size/dimensions, beam shape, etc.

Stage 2: Line finding/assisted line finding
-   Enact any of the requested line finding routines (should be tracked in the output catalogue too)
-   Use external line-finder output (such as SoFiA-2 catalogues) as assisted search
-   Diagnostic plots
-   Reliability checkers
-   Save output found line catalogue + template for user to input known a-priori redshifts for any lines

Stage 3: Line extraction
-   Extract the data/stats needed to later characterise/identify the lines (masks, etc.)
-   While we are at it, if the user specified any a-prior redshifts, we can do a spiderweb-mask sub-division to look for any (low S/N)
    plausible lines from Splatalogue (mask divided into centre point-like mask, surrounded by pieces-of-pie masks)
-   Save finalised line catalogue data on locations, x/y/z extents, masks, associations to single sources, etc.

Stage 4: Line Characterisation
-   With all ID'd lines in hand, characterise them all with fitting routines (lmfit; choose components using AIC), get S/N, etc.
-   For associated lines to sources, optimise mask for summed S/N of all lines
-   Save line statistics to catalogue

Stage 5: Line Identification
-   For all lines/sources without redshift, attempt to identify using Splatalogue/spectral overlap with known redshift sources
    (this will mostly be a fruitless endeavour without additional spectral modelling)
    For identified lines, can extract additional derived properties/ratios/statistics with assumptions (user optionally set assumptions)

Stage 6: Final outputs/pretty plotting
-   Accumulated catalogue of data/stats on sources/lines, as well as many different plots for analysis.
"""