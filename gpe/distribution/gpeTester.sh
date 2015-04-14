#!/bin/sh

mkdir fp_res

#example01
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='fp_res/ex01_m_20_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='fp_res/ex01_m_30_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=40 --out_file='fp_res/ex01_m_40_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'

#example02
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='fp_res/ex02_m_20_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='fp_res/ex02_m_30_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='fp_res/ex02_m_40_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'

#example03
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='fp_res/ex03_m_20_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='fp_res/ex03_m_30_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=40 --out_file='fp_res/ex03_m_40_fp.txt' --arth_mode=pint --exp_mode='classical_exp' --print_csv='true'


mkdir pint_res

#example01
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='pint_res/ex01_m_20_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='pint_res/ex01_m_30_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'
#./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=40 --out_file='pint_res/ex01_m_40_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'

#example02
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='pint_res/ex02_m_20_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='pint_res/ex02_m_30_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'
#./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='pint_res/ex02_m_40_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'

#example03
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='pint_res/ex03_m_20_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='pint_res/ex03_m_30_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'
#./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=40 --out_file='pint_res/ex03_m_40_pint.txt' --arth_mode=pint --exp_mode='interval_exp' --print_csv='true'

mkdir dint_res

#example01
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='dint_res/ex01_m_20_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='dint_res/ex01_m_30_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
#./gpe_tester --e=3 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=40 --out_file='dint_res/ex01_m_40_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'

#example02
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='dint_res/ex02_m_20_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='dint_res/ex02_m_30_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
#./gpe_tester --e=4 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=30 --out_file='dint_res/ex02_m_40_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'

#example03
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='dint_res/ex03_m_20_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=20 --out_file='dint_res/ex03_m_30_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
#./gpe_tester --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 --m=40 --out_file='dint_res/ex03_m_40_dint.txt' --arth_mode=dint --exp_mode='interval_exp' --print_csv='true'
