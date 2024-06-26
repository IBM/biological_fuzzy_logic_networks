# Loops

This folder contain the necessary data for generating the results presented in the *BioFuzzNets can handle and fit loops* part of the report.

    - Test_loops.ipynb: contains toy code for fiddling with loops and finding parameters generating different behaviors. Also contains a part checking whether loop behavior is very sensitive to parameter change. Not used in the report.
    - Loops_CV.ipynb: Used to generate the RMSE plots in the report (Figure 11). Analyses data generated by the other python scripts in this folder.
    
    - CV_neg_100: results obtained after 50 replicates of simulating and fitting a randomly initialised negative loop.
    - CV_pos_100: results obtained after 50 replicates of simulating and fitting a randomly initialised positive loop.
    - CV_neg_oscill_100: results obtained after 50 replicates of simulating and fitting a negative oscillatory loop with parameters oscillatory_params_big_loop.p.
    - CV_pos_bistabl_100: results obtained after 50 replicates of simulating and fitting a positive bistable loop with parameters bistabillity_params_big_loop.p.
    **CAREFUL: I think I made a mistake:though the folders are called XX_100, I think I only have 50 simulations in each case**
     - bistability_params_big_loop.p: params used to generate an oscillatory behavior on a positive feedback loop with the topology shown Figure 10.a of the report
     - oscillatory_params_big_loop.p: params used to generate an oscillatory behavior on a positive feedback loop with the topology shown Figure 10.b of the report
     
     - CV_pos_bistabl.py: script to simulate and fit a positive bistable loop multiple times
     - CV_neg_oscill.py: script to simulate and fit a negative oscillatory loop multiple times
     - loop_optim_pos.py: script to simulate and fit a randomly initialised positive loop multiple times
     - loop_optim_neg.py: script to simulate and fit a randomly initialised negative loop multiple times