<h2 align = 'center'> Bayes By Backprop </h2>

### Introduction
Bayesian Neural Networks are the most used method to quantify uncertainty, unlike the classical setup where we want the model to learn the parameters and expecting a scalare values, in the Bayesian setup we put distributions over the parameters and learn the paramaters of that distribution. using the Bayes rule hense the name Bayesian. 

<div align ='center'>
    <img src="pictures/BNN.png" width="500"/>    
</div>

The quantity that we want is the posterior, and try to learn this probibility distribution using Bayes rule using a prior and and a Likelihood. 

<div align='center'>
   <img src="https://latex.codecogs.com/svg.image?\text{posterior}=&space;\frac{\text{Likelihood&space;x&space;Prior}}{\text{Marginal&space;Likelihood}}&space;" title="\text{posterior}= \frac{\text{Likelihood x Prior}}{\text{Marginal Likelihood}} " />
</div>
<br/>


Considering the following notations, where <img src="https://latex.codecogs.com/svg.image?\mathcal{D}"/> is the training data, and <img src="https://latex.codecogs.com/svg.image?\theta"/> are the model parameters, we have the Bayes formula : 

<div align='center'>
<img src="https://latex.codecogs.com/svg.image?&space;p(\theta|\mathcal{D})&space;=\frac{p(\mathcal{D}|\theta)p(\theta)}{p(\mathcal{D})}&space;=\frac{p(\mathcal{D}|\theta)p(\theta)}{\int&space;p(\mathcal{D}|\theta')p(\theta')d\theta'}&space;" />
</div>
<br/>


Since the marginal likelihood ( the evidence) is untractable, the posterior cannot be analyticaly computed and hence the trick of approximating the posterior : this is what we call **Variational Inference** where we choose a variational posterior <img src="https://latex.codecogs.com/svg.image?q_\omega(\theta)"/>, and try to get close as possible to the true posterior <img src="https://latex.codecogs.com/svg.image?p(\theta|\mathcal{D})"/> by minimizing the Kullback-Leibler Difference defined as :
<div align='center'>
<img src="https://latex.codecogs.com/svg.image?\textsc{KL}\Big{(}q_{\omega}(\theta)~||~p(\theta|\mathcal{D})\Big{)}&space;=&space;\int&space;q_{\omega}(\theta)\text{log}\frac{q_{\omega}(\theta)}{p(\theta|\mathcal{D})}\text{d}\theta" />
</div>
<br />


The KL-Divergnece compute the similarity between two distributions 




### Results







### Comments




---
### References
[1] C. Blundell, J. Cornebise, K. Kavukcuoglu, and D. Wierstra, “Weight uncertainty in neural networks,” arXiv preprint
arXiv:1505.05424, 2015