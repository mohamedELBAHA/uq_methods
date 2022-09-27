<h2 align='center'> Snapshot Ensemble </h2>



## Introduction
Snapshot Ensemble method is a nice way to counter the big limitation of ensemble methods which is training each model apart which can become rapidly computationaly expensive. This method focuses on controlling the learning rate by defining a schceduler.
The advantages of this techniques is to recover multiple models while training . 

This is achieved by letting a single neural network converge into several local minima along its optimization path and save the model parameters at certain epochs, therefore the weights being saved "snapshots" of the model (picture below)


<div align='center'>
   <img src="pictures/locaux.PNG" width="850"/> 
</div>

The learning rate scheduler presented in *Huang et al (2017)* is called the **Cosine Annealing** 

<div align='center'>
   <img src="pictures/cosine.JPG" width="450"/> 
</div>

- <img src="https://latex.codecogs.com/svg.image?\alpha(t)"/> represents the learning rate at epoch <img src="https://latex.codecogs.com/svg.image?t"/>.
- <img src="https://latex.codecogs.com/svg.image?T"/> is the total number of epochs.
- <img src="https://latex.codecogs.com/svg.image?M"/> represents the number of cycles (periods).

Since the function is periodicaly decreasing (périodique, décroissante par période) the first value <img src="https://latex.codecogs.com/svg.image?\alpha(t=0)"/> is equal the maximum learning rate.

To understand how this function works, we plot the cosine Annealing rate scheduler  

<div align='center'>
   <img src="pictures/cosineline.PNG" width="450"/> 
</div>

We notice that the function starts with a maximum lr of 0.01 at the beginning of the cycle and ends the cycle ( 50 epochs ) with a lr close to zero.   

## Implementation
The impletentation relies on **Callbacks** from keras, the callback class allow us to define operations while training, like stop the training when reaching a certain score, save the models when reaching a local minima ... etc. 
```python
from keras.callbacks import Callback
#instanciate the callback
mycallback = Callback()
#add your callback in the model.fit method
model.fit(X_train, y_train,
          validation_data=(X_test, y_test),
          epochs=n_epochs,
          verbose=1, 
          callbacks=[mycallbacks])

```


## Results 

Fllowing the same setup above, where we used a Sequential Neural Network (100,100,100,10,1) and total number of epochs **T=500** divided into 10 cycles **M = 10**.
the variability of predictions with this method is not very disperse as shown in the picture below. 



<div align='center'>
   <img src="pictures/variability.jpg" width="550"/> 
</div>

In term of the evalutation of the prediction, we got an `RMSE` and `MAE` not too bad compared to other methods.

<div align='center'>
   <img src="pictures/marrmse.PNG" width="550"/> 
</div>

for the correlation between the residuals and uncertainty :


<div align='center'>
   <img src="pictures/correlat.PNG" width="550"/> 
</div>




## Comments

We presented in this method an alternative the big limitation of Ensemble methods where training multiple models is is not preferred due to the computational cost of training each single model.





### References
Huang, Gao, et al. "Snapshot ensembles: Train 1, get m for free." arXiv preprint arXiv:1704.00109 (2017).