<div align = 'center'>
    <h2> Deep Evidential Regression </h2>
</div>

## Introduction
Unlike looking to sample from different models, The Evidential approach focuses on getting the high order distribution. 

<div align='center'>
     
<img src="https://latex.codecogs.com/svg.image?y_1,&space;y_2,&space;\dots,&space;y_n&space;\sim&space;\mathcal{N}(\mu,&space;\sigma^2)"/>

</div>


and since we don't know the parameters of this gaussian distribution, we will be estimating it by putting priors on each one them ( the mean and the variance). 

<div align='center'>
<img src="https://latex.codecogs.com/svg.image?\mu&space;\sim&space;\mathcal{N}(\gamma,&space;\sigma^2\nu^{-1})&space;\quad&space;and&space;\quad&space;\sigma^2&space;\sim&space;\Gamma^{-1}(\alpha,&space;\beta)&space;"/>
</div>

Our model now will learn this new set of parameters <img src='https://latex.codecogs.com/svg.image?m&space;=&space;(\alpha,&space;\beta,&space;\gamma,&space;\nu&space;)'/>.

By learning these parameters we can get the desired estimations by computing the quantities below : 
<div align='center' >
<img src='https://latex.codecogs.com/svg.image?&space;\mathbb{E}(\mu)&space;=&space;\gamma&space;\qquad&space;\text{The&space;prediction.}&space;&space;'>
<br> 
<img src='https://latex.codecogs.com/svg.image?\mathbb{E}(\sigma^2)&space;=&space;\frac{\beta}{\alpha-1}&space;\qquad&space;\text{The&space;aleatoric&space;uncertainty}&space;'>
<br>
<img src='https://latex.codecogs.com/svg.image?&space;Var(\mu)&space;=&space;\frac{\beta}{\nu(\alpha-1)}&space;\qquad&space;\text{The&space;Epistemic&space;uncertainty}'>
</div>


## Implementation
One of the advantages of this method is the simplicity to implement it. Firstly, the last output layer should be Evidential, that means the activation function should be conjugate prior which is a Normal Inverse Gamma. Secondly, The loss should be the adopted loss above.

<div align ='center'>
    <img src="pictures/archi.PNG" width="600"/>    
</div>

## Results

|  |  |
| ------ | ------: |
| Mean Absolute Error (MAE) |**0.122** |
| Root Mean Squarred Error RMSE| **0.162** |
|Calibration Error |  **0.008** |
| Sharpness | **0.151**|
|Negative-Log-Likelihood | **-0.395**|

As mentionned, this method allow us to distinguish between the two uncertainties (aleatoric and epistemic), and here how it looks like if we plot the respective variances.

As we can see, the aleatoric uncertainty is bigger than the epistemic uncertainty, nevethless, both of the estimations are sharp.  

<div align ='center'>
    <img src="pictures/distinct.PNG" width="450"/>    
</div>

Here is the coverage plot and the calibration curve, its done after calibration.

<div align ='center'>
    <img src="pictures/covcalib.PNG" width="750"/>    
</div>



---


## References 
[1] Amini, Alexander, et al. "Deep evidential regression." Advances in Neural Information Processing Systems 33 (2020): 14927-14937.

