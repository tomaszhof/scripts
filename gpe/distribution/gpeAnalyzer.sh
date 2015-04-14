#!/bin/sh

mkdir res

./IntervalAnalyzer pint_res/ex01_m_20_pint_l.csv pint_res/ex01_m_20_pint_r.csv fp_res/ex01_m_20_fp_e.csv  fp_res/ex01_m_20_fp_f.csv res/ex01_m_20_pint_e_distr.csv res/ex01_m_20_pint_f_distr.csv

./IntervalAnalyzer pint_res/ex01_m_30_pint_l.csv pint_res/ex01_m_30_pint_r.csv fp_res/ex01_m_30_fp_e.csv fp_res/ex01_m_30_fp_f.csv res/ex01_m_30_pint_e_distr.csv res/ex01_m_30_pint_f_distr.csv

#./IntervalAnalyzer pint_res/ex01_m_40_pint_l.csv pint_res/ex01_m_40_pint_r.csv fp_res/ex01_m_40_fp_e.csv fp_res/ex01_m_40_fp_f.csv res/ex01_m_40_pint_e_distr.csv res/ex01_m_40_pint_f_distr.csv

./IntervalAnalyzer dint_res/ex01_m_20_dint_l.csv dint_res/ex01_m_20_dint_r.csv fp_res/ex01_m_20_fp_e.csv fp_res/ex01_m_20_fp_f.csv res/ex01_m_20_dint_e_distr.csv res/ex01_m_20_dint_f_distr.csv

./IntervalAnalyzer dint_res/ex01_m_30_dint_l.csv dint_res/ex01_m_30_dint_r.csv fp_res/ex01_m_30_fp_e.csv fp_res/ex01_m_30_fp_f.csv res/ex01_m_30_dint_e_distr.csv res/ex01_m_30_dint_f_distr.csv


#./IntervalAnalyzer dint_res/ex01_m_40_dint_l.csv dint_res/ex01_m_40_dint_r.csv fp_res/ex01_m_40_fp_e.csv fp_res/ex01_m_40_fp_f.csv res/ex01_m_40_dint_e_distr.csv res/ex01_m_40_dint_f_distr.csv

