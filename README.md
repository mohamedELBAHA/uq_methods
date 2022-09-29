
<div align="center">
  <h2> Uncertainty Quantification For Model Validation</h2>
  <a href=""><img src="https://readme-typing-svg.herokuapp.com?color=195671&lines=Uncertainty+Quantification+;Model+Validation"></a>
</div>

Uncertainty quantification (UQ) plays a vital role in the decision-making process. Bayesian approximation and Ensemble learning techniques are two of the most widely-used UQ methods in the literature.
This project aims to explore several UQ methods and compare their performances on different Datasets to validate the predicitive Machine Learning models.

In this respository you will find : 
1. [Here](UQ Methods/), Uncertainty Quantification methods applied on two types of data. 
2. [Here](Validation metrics/), We present several metrics to evaluate the estimation of uncertainties of each method.
3. [Here](Analysis/), We analyze and comment the results.

To have a large view betweeen the performance of the methods using two types of data, we displayed the figures and tables for the sake of comparaison ===> [here](https://sim-ssd.si-pages.michelin.com/uncertainty-quantification)

<div align="center">
  <a href="UQ Methods/"><img src="pictures/ICONS.PNG"></a>
</div>

<br> </br> 

### Project Structure

Uncertainty-quantification
```
 └── Analysis/ 
     └── utils.py
 └── pictures/
 └── UQ methods/
     └── Bayesian Neural Networks
     │     ├── BNN_dense.ipynb
     │     └── BNN_sparse.ipynb
     └── Bagging
     │     ├── Bagging_dense.ipynb
     │     └── Bagging_sparse.ipynb
     └── Conformalized Quantile
     │     ├── CQR_dense.ipynb
     │     └── CQR_sparse.ipynb
     └── Deep Evidential Regression
     │     ├── DER_dense.ipynb
     │     └── DER_sparse.ipynb 
     └── Gaussian Processes
     │     ├── GP_dense.ipynb
     │     └── GP_sparse.ipynb
     └── Monte Carlo Dropout
     │     ├── MCD_dense.ipynb 
     │     └── MCD_sparse.ipynb
     └── Random Forest
     │     ├── RF_dense.ipynb
     │     └── RF_sparse.ipynb
     └── Snapshot Ensemble
           ├── Models/
           └── SnapEns_dense.ipynb
 └── Validation-Metrics/
     └── metrics.py
```
### Tools 

Here a non-exhaustive list of tools and APIs ready-to-use for Uncertainty Quantification in Machine Learning :

|  Name|  Description| Licence |
| ------ | ------ | ------ |
|<a href='https://uq360.mybluemix.net/'> IBM UQ360 </a>|Extensible open-source toolkit that can help you estimate, communicate and use uncertainty in machine learning model predictions|MIT|
|  <a href='https://uncertainty-toolbox.github.io/'>Uncertainty Toolbox</a>  |  A python toolbox for predictive uncertainty quantification, calibration, metrics, and visualizations. |  MIT |
| <a href='https://mapie.readthedocs.io/en/latest/index.html'>MAPPIE</a> | A scikit-learn-compatible module for estimating prediction intervals.| DD |




<details><summary> <h3> References à resources </h3> </summary>

    
I- **Uncertainty**

1. Hüllermeier, Eyke, and Willem Waegeman. "Aleatoric and epistemic uncertainty in machine learning: An introduction to concepts and methods." Machine Learning 110.3 (2021): 457-506.
<br> 

II- **UQ Methods**


1. Yarin Gal and Zoubin Ghahramani. *Dropout as a bayesian approximation : Representing model uncertainty in deep learning.* In international conference on machine learning, pages 1050–1059. PMLR, 2016

2. Huang, Gao, et al. "*Snapshot ensembles: Train 1, get m for free.*" arXiv preprint arXiv:1704.00109 (2017).
    
3. Amini, Alexander, et al. "*Deep evidential regression.*" Advances in Neural Information Processing Systems 33 (2020): 14927-14937.
 
4. C. Blundell, J. Cornebise, K. Kavukcuoglu, and D. Wierstra, *“Weight uncertainty in neural networks,”* 
arXiv:1505.05424, 2015
    
5. Rasmussen, C. E., Williams, C. K. I., *Gaussian processes for machine learning (2016)*, The MIT Press

6. Breiman, Leo. *"Bagging predictors."* Machine learning 24.2 (1996): 123-140.

7. Romano, Yaniv, Evan Patterson, and Emmanuel Candes. *"Conformalized quantile regression."* Advances in neural information processing systems 32 (2019).

<br>
   
III- **Validation metrics**  
 
 
1. Tran, Kevin, et al. *"Methods for comparing uncertainty quantifications for material property predictions."* Machine Learning: Science and Technology 1.2 (2020): 025006. 

2. Sluijterman, L., Cator, E., Heskes, T. (2021). *How to Evaluate Uncertainty Estimates in Machine Learning for Regression.* arXiv preprint arXiv:2106.03395.
    
3. Levi D, Gispan L, Giladi N and Fetaya E 2020 Evaluating and Calibrating Uncertainty Prediction in Regression Tasks
</details>


*@author : Mohamed El Baha*  
