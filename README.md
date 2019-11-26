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
<div style="text-align:center"><img src ="assets/All1.png"  width="1000"/></div>


## CIFAR-10:

### ResNet v1-20

- Epoch - 20
- Optimizer - Adam
- Number of Runs - 3

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin|**82.6067%**|7.8006%|0.6249444|0.292334031|
|Mish|81.85%|**7.5327%**|3.064647|1.1073503|
|Swish|80.64%|7.8447%|0.3747888|0.152951|
|ReLU|79.02%|8.5212%|2.048854|0.7663393|
|SELU|78.96%|8.0047%|2.156803|0.6439562|
|ELU|80.497%|7.7353%|0.527278|0.405108|
|TanH|66.643%|12.6799%|**0.3068478**|0.2829257|
|Sigmoid|24.44%|38.2795%|13.715487|11.328736|
|Linear|38.953%|17.892%|0.4028509|**0.04750964**|
|SoftPlus|74.57%|10.291%|1.1881919|0.7724417|
|Softsign|55.396%|18.0109%|8.7452285|3.7473952|
|Leaky ReLU|79.483%|8.0239%|2.1014492|0.6178107|

<div style="text-align:center"><img src ="assets/test_res20.png"  width="1000"/></div>

### ResNet v1-56

- Epoch - 20
- Optimizer - Adam
- Number of Runs - 3

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin|82.167%|8.9934%|0.984626|0.4272043|
