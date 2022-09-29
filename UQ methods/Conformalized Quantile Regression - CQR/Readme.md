<h2 align='center'> Conformalized Quantile Regression </h2>

## Introduction
CQR is a technique for constructing prediction intervals (PI= that attain valid coverage in finite samples, without making distributional assumptions. It combines the statistical efficiency of **quantile regression** with the distribution-free coverage guarantee of **conformal prediction**.

The advantages of CQR are :

 1. It can wrap around **any algorithm** for quantile regression, including random forests and deep neural networks.
 2. Its rigorous control of the miscoverage rate, **independent** of the underlying regression algorithm.
 3. CQR is a procedure that inherits the advantages of **conformal prediction** and **quantile regression**. 

In CQR method, we use Quantile Regression to estimate the true conditional quantile, and then apply conformal steps on a calibration set to ensure marginal coverage. 
The overall steps are : 
 1. Split the training data into two substets ( proper train & Calibration).
<div align='center'>
<img src="https://latex.codecogs.com/svg.image?\{X_i,Y_i\}_{i=1}^n&space;=&space;\{\left&space;(&space;X_i,Y_i&space;\right&space;),&space;i\in\mathcal{I}_1\}\bigoplus&space;\{\left&space;(&space;X_i,Y_i&space;\right&space;),&space;i\in\mathcal{I}_2\}"/>
</div>
</br>


 2. Choose any Quantile Regression Model, and fit 2 conditional quantile functions. 
</br>

<div align='center'>
 <img src="https://latex.codecogs.com/svg.image?\{\hat{q}_{\alpha_{lower}},\hat{q}_{\alpha_{upper}}\}\leftarrow&space;\mathcal{F}(\{(X_i,Y_i):&space;i\in\mathcal{I}_1\})"/>
</div>
</br>


 3. Compute the conformity score.
</br>
<div align='center'>
<img src="https://latex.codecogs.com/svg.image?E_i:=&space;\text{max}\{\hat{q}_{\alpha_{lower}}(X_i)-Y_i,Y_i-\hat{q}_{\alpha_{upper}}(X_i)\}&space;\quad\text{for&space;each}\;&space;i\in\mathcal{I}_2&space;" title="E_i:= \text{max}\{\hat{q}_{\alpha_{lower}}(X_i)-Y_i,Y_i-\hat{q}_{\alpha_{upper}}(X_i)\} \quad\text{for each}\; i\in\mathcal{I}_2 " />
</div>
</br>
 4. Make the prediction for a new test point.
 
<div align='center'>
 <img src="https://latex.codecogs.com/svg.image?Y_{n+1}\leftarrow&space;\mathcal{C}(X_{n+1})=\Big{[}\hat{q}_{\alpha_{lower}}(X_{n+1} - Q_{1-\alpha}(E, \mathcal{I}_2))\;,\;\hat{q}_{\alpha_{upper}}(X_{n+1} + Q_{1-\alpha}(E, \mathcal{I}_2)) \Big{]}"/>
</div>
 

## Results

Let's first look at the prediction performance, and that by looking at the MAE and RMSE while training and testing. 

<div align='center'>
 <img src="pictures/cqrmae.PNG"/>
</div>
 
In terms of coverage and uncertainty/error correlation we can refer to this graphs, while the first one is in the training data and the second one in the test test. recall that the test set size is 10% of the data thats why we see a small number of points.

<div align='center'>
 <img src="pictures/covtrain.PNG"/>
</div>

The interessting phenomenon that we are witnessing here is that there is some points that are aligned with upper and lower bounds, and the dispersion of points are perfectly distributed between the two ligns.

<div align='center'>
 <img src="pictures/covtest.PNG"/>
</div>

## Appendix 

Since this method doesn't not get us the variance, which we need to compute the adopted metrics as the neglog and sharpness. 
To get this values we used the *Extended Pearson-Tukey method* [2]

<div align='center'>
 <img src="pictures/pearson.PNG"/>
</div>

## References 
[1] Romano, Yaniv, Evan Patterson, and Emmanuel Candes. "Conformalized quantile regression." Advances in neural information processing systems 32 (2019).

[2]  By J.J.A. Moors, L.W.G. Strijbosch, W.J.H. van Groenendaal, Estimating mean and variance through quantiles: : an experimental comparison of different methods, July 2002
