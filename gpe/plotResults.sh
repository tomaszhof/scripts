#!/bin/sh

mkdir figures

#example01
python3 gpeResultsVisualizer.py example03_pint.csv x figures/fig01_x15_pint.eps
python3 gpeResultsVisualizer.py example03_dint.csv x figures/fig01_x15_dint.eps
python3 gpeResultsVisualizer.py example03_pint.csv y figures/fig01_y15_pint.eps
python3 gpeResultsVisualizer.py example03_dint.csv y figures/fig01_y15_dint.eps
python3 pyPlotSolution.py 1 2 1 2 example03/res_fp.csv figures/fig01.eps


#example02
python3 gpeResultsVisualizer.py example04_pint.csv x figures/fig02_x15_pint.eps
python3 gpeResultsVisualizer.py example04_dint.csv x figures/fig02_x15_dint.eps
python3 gpeResultsVisualizer.py example04_pint.csv y figures/fig02_y15_pint.eps
python3 gpeResultsVisualizer.py example04_dint.csv y figures/fig02_y15_dint.eps
python3 pyPlotSolution.py 1 2 1 2 example04/res_fp.csv figures/fig02.eps

#example03
python3 gpeResultsVisualizer.py example08_pint.csv x figures/fig03_x15_pint.eps
python3 gpeResultsVisualizer.py example08_dint.csv x figures/fig03_x15_dint.eps
python3 gpeResultsVisualizer.py example08_pint.csv y figures/fig03_y15_pint.eps
python3 gpeResultsVisualizer.py example08_dint.csv y figures/fig03_y15_dint.eps
python3 pyPlotSolution.py 1 2 1 2 example08/res_fp.csv figures/fig03.eps
