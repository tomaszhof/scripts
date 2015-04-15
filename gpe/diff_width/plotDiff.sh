#!/bin/sh

python3 pyPlotWidthDiff.py example04_pint_x15.csv example04_dint_x15.csv ex04_diff.eps 0.0 1.5e-13
python3 pyPlotWidthDiff.py example03_pint_x15.csv example03_dint_x15.csv diffPlot.eps 0.0 1.5e-14
python3 pyPlotWidthDiff.py example08_pint_x15.csv example08_dint_x15.csv diffPlot.eps 0.0 1.0e-15
