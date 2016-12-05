# COLLABORATIVE DEEP LEARNING
Novel approach combining Deep Learning with Collaborative Filtering for Recommender Systems

#Usage Notes 
First run cdl.py. In this code relu activation has been used instead of sigmoid and the code does not use pretraining
# Evaluate
To evaluate run evaluate_CDL.py. The code calculates recall@M for M from M_low to M_high. Keep the value of variable "p" same as in cdl.py. This "p" is used for the directory path for model files generated, not to be conufsed with "P" used to denote the sparse (P=1) and dense(P=10) settings.

