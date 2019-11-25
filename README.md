<img align="left" width="150" height="150" src="logo/logo.png">

# SharkFin
<p align="left">
    <a href="LICENSE" alt="License">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" /></a>
    <a href="http://hits.dwyl.io/digantamisra98/SharkFin" alt="HitCount">
        <img src="http://hits.dwyl.io/digantamisra98/SharkFin.svg" /></a>
</p>
<br>
<br>
<br>

SharkFin is a modified version of ReLU which has the following formula: 
<br>
**f(x) = Tanh(e<sup>x</sup>).ReLU(-1,x) = Tanh(e<sup>x</sup>).max(-1,x)**
<br>
Derivative: 
<div style="text-align:center"><img src ="assets/derivative.png"  width="500"/></div><br>
<div style="text-align:center"><img src ="assets/All.png"  width="1000"/></div>


## CIFAR-10:

- Network - ResNet v1-20
- Epoch - 20
- Optimizer - Adam
- Number of Runs - 3

|Activation Function|Test Accuracy|Test Loss|σ accuracy|σ loss|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin|82.6067%|7.8006%|0.6249444|0.292334031|
|Mish|81.85%|7.5327%|3.064647|1.1073503|
