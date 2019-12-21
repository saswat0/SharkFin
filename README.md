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

SharkFin v1 is a modified version of ReLU which has the following formula: 
<br>
**f(x) = Tanh(e<sup>x</sup>).ReLU(-1,x) = Tanh(e<sup>x</sup>).max(-1,x)**
<br>

SharkFin v2 is a modified smoother version of SharkFin v1 which has the following formula: 
<br>
**f(x) = Tanh(e<sup>x</sup>).clamp(x, min_value = -1, max_value = None)**
<br>

Zoomed in positive and negative domains of SharkFins:

<p float="left">
  <img src="assets/negative1.png"  width="420"/>
  <img src="assets/positive1.png"  width="420"/>
</p>

Derivative of SharkFin v1: 
<div style="text-align:center"><img src ="assets/derivative.png"  width="500"/></div><br>
<div style="text-align:center"><img src ="assets/All11.png"  width="1000"/></div><br>

Output Landscape of a randomly initialized six-layered fully connected network with co-ordinates as scalar inputs. 

<div style="text-align:center"><img src ="assets/landskape.png"  width="1000"/></div>

Variation of Test accuracy with increasing depth for MNIST classification and increasing Learning Rate for CIFAR-10 classification:

<p float="left">
  <img src="assets/layersacc2.png"  width="420"/>
  <img src="assets/lr_fin.png"  width="420"/>
</p>

Effect of Increasing Input Gaussian Noise on MNIST:

<div style="text-align:center"><img src ="assets/noise.png"  width="1000"/></div>

## CIFAR-10:

### ResNet 20

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin v1|82.6067%|7.8006%|0.6249444|0.292334031|
|SharkFin v2|**83.346%**|**7.0009%**|0.936814|0.3490056|
|Mish|81.85%|7.5327%|3.064647|1.1073503|
|Swish|80.64%|7.8447%|0.3747888|0.152951|
|ReLU|79.02%|8.5212%|2.048854|0.7663393|
|SELU|78.96%|8.0047%|2.156803|0.6439562|
|ELU|80.497%|7.7353%|0.527278|0.405108|
|TanH|66.643%|12.6799%|**0.3068478**|0.2829257|
|SoftPlus|74.57%|10.291%|1.1881919|0.7724417|
|Leaky ReLU|79.483%|8.0239%|2.1014492|0.6178107|
|PReLU|82.4%|7.3859%|0.623591|**0.043733**|

<div style="text-align:center"><img src ="assets/test_res20v1.png"  width="1000"/></div>

### ResNet 56

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin v1|**82.167%**|8.9934%|0.984626|0.4272043|
|SharkFin v2|81.726%|8.27379%|**0.7684327**|0.4026965|
|Swish|81.44%|**7.83062%**|0.7884584|**0.1659273**|
|ReLU|79.323%|8.7444%|1.082507|0.27063429|
|Mish|81.97%|7.8868%|0.803616|0.31262063|
|SELU|76.363%|9.380397%|2.0838639|0.6248774|
|ELU|80.387%|8.02079%|2.444931|0.8199566|
|Leaky ReLU|77.68%|8.79255%|1.0717275|0.4718626|
|PReLU|78.436%|8.82069%|1.506659|0.5329421|
|Tanh|61.783%|13.723%|6.305005|1.893993|
|SoftPlus|74.12%|10.71375%|4.335004|2.203364|

### ResNet 110

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|Mish|79.586%|8.935%|1.3276|0.7712|
|Swish|81.866%|7.768%|1.3733|0.5738|

### DenseNet 121:

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|Mish|88.72%|3.5036%|0.6205|0.2128|

### DenseNet 161:

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|Mish|88.056%|3.6893%|0.0492|0.0476|

### DenseNet 169:

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|Mish|88.043%|3.912%|0.7153|0.285|

### DenseNet 201:

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|Mish|88.923%|3.4056%|0.0865|0.0391|
|Swish|||||

### Squeeze Net:

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *1*

|Activation Function |Test Accuracy|Test Loss|
|:---:|:---:|:---:|
|SharkFin v1|83.41%|4.9%|
|SharkFin v2|**85.84%**|4.419%|
|ReLU|84.74%|4.503%|
|Mish|84.96%|4.381%|
|Swish|85.73%|**4.175%**|
|ELU|83.17%|4.875%|
|SELU|81.12%|5.581%|
|Leaky ReLU|84.08%|4.757%|
|PReLU|83.84%|4.831%|
|TanH|76.68%|6.75%|
|SoftPlus|83.83%|4.799%|

<div style="text-align:center"><img src ="assets/squeezenet1.png"  width="1000"/></div>
