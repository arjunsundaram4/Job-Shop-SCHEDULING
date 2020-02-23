# CIOL-scheduling
## Overview
In this repository, it is focused on extracting priority rules (PR) for dynamic multi-objective flexible job shop scheduling problems using gene expression programming (GEP). This repository also enables you to test your PR's. You can find the related paper from this [link](https://www.tandfonline.com/doi/abs/10.1080/00207543.2018.1543964).
## Citation
     @article{ozturk2019extracting,
     title={Extracting priority rules for dynamic multi-objective flexible job shop scheduling problems using gene expression programming},
     author={Ozturk, Gurkan and Bahadir, Ozan and Teymourifar, Aydin},
     journal={International Journal of Production Research},
     volume={57},
     number={10},
     pages={3121--3137},
     year={2019},
     publisher={Taylor \& Francis}},
     URL = { https://doi.org/10.1080/00207543.2018.1543964}}
    
    
    @article{teymourifar2018dynamic,
     title={Dynamic Priority Rule Selection for Solving Multi-objective Job Shop Scheduling Problems},
     author={Teymourifar, Aydin and Bahadir, Ozan and Ozturk, Gurkan},
     journal={Universal Journal of Industrial and Business Management},
     volume={6},
     number={1},
     pages={11--22},
     year={2018},
     publisher={Horizon Research Publishing}
     }
## Initial Setup
This project was developed using Python2.
I highly recommend using Anaconda for Python environment management. It will help you install Shapely, which I've had some problems installing with pip. You do not need extra libraries not contained by Anaconda. 
## Extracting new PR's using GEP
When you run the ```genetikAlgoritma.py``` new rules automatically are generated according to given parameters. This script calls the ```main.py``` containing both ```schedulingProblem.py``` generating the problem and ``` createSolution.py``` that is the simulation scripts. After have finished, the scripts ```sumofresult.txt``` file is created. This file contains all information about GEP steps and at the bottom of this file, you can find the extracted PR's. 
## Testing PR's
If you have your PR's you can test them by running ```dispatchingRules.py``` script. Before running this script you should add your rules on this file. You must select your variables created your rules in our GEP terminal sets (you can find it in the paper page 8).  
When you run the script, ```main.py``` is called same as Extracting new PR's using GEP. After finish the script ```result.txt```and  ```sumofresult.txt``` files are created. The first file records all result for all PR's for each subproblem while the second file gives brief information.
## Extracting dynamic rules 
If you want to extract dynamic rules, you must run the ```dynamicSelectionOfRules.py```. You can also access the related paper from this [link](http://www.hrpub.org/download/20180330/UJIBM2-11611325.pdf).
## Using existed data
This repository enables users not only generate data but also opening existed one. If you want to use existed dataset, you should make some modification the creating dataset on the ```__init__``` function under the ```schedulingProblem.py```. There are some prospect kinds of data options in lines between 32 and 35.  
# Job-Shop-SCHEDULING
