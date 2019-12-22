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
|Swish|88.516%|3.647%|0.29488|0.12399|

### DenseNet 201:

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|Mish|88.923%|3.4056%|0.0865|0.0391|
|Swish|88.223%|3.734%|0.8794|0.3249|

### MobileNet v1

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin v1|82.943%|5.304%|0.2597|0.0845|
|SharkFin v2|82.49%|5.3683%|**0.0694**|0.114|
|Mish|83.84%|5.424%|0.4899|0.2323|
|Swish|83.16%|5.3826%|0.3747|0.2046|
|ReLU|81.71%|5.7143%|1.2709|0.0541|
|SELU|81.52%|5.5006%|0.3842|0.1192|
|ELU|**84.016%**|**4.863%**|0.0974|0.0969|
|TanH|75.846%|7.23%|0.1643|0.0569|
|SoftPlus|83.323%|5.288%|0.3564|0.2323|
|Leaky ReLU|81.983%|5.5903%|0.3147|0.1404|
|PReLU|83.03%|5.2273%|0.0804|**0.0442**|

### MobileNet v2

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin v1|80.926%|5.596%|0.3583|0.18|
|SharkFin v2|82.36%|5.2873%|0.8311|0.1468|
|Mish|82.57%|5.1986%|0.6265|0.1873|
|Swish|**83.123%**|**5.0693%**|**0.1369**|0.0275|
|ReLU|81.1%|5.5467%|0.5062|0.1236|
|SELU|78.603%|6.215%|0.4018|0.1679|
|ELU|80.69%|5.5603%|0.312|0.07998|
|TanH|74.836%|7.317%|0.996|0.3141|
|SoftPlus|80.86%|5.887%|0.2613|0.1298|
|Leaky ReLU|81.68%|5.3856%|0.3323|0.0991|
|PReLU|82.043%|5.2526%|0.4224|**0.0205**|

### Squeeze Excite ResNet-18

- Epoch - *20*
- Optimizer - *Adam*
- Number of Runs - *3*

|Activation Function|μ <sub>Test Accuracy</sub>|μ <sub>Test Loss</sub>|σ <sub>accuracy</sub>|σ <sub>loss</sub>|
|:---:|:---:|:---:|:---:|:---:|
|SharkFin v1|88.49%|3.718%|0.2174|0.0857|
|SharkFin v2|88.42%|3.822%|0.4846|0.149|
|Mish|88.603%|3.7193%|0.087|0.0314|
|Swish|**88.706%**|3.713%|0.1211|0.1843|
|ReLU|88.513%|**3.659%**|0.3231|0.1573|
|SELU|84.48%|4.76%|**0.0531**|0.0432|
|ELU|86.33%|4.174%|0.1388|**0.0151**|
|TanH|80.22%|5.9376%|0.5416|0.214|
|SoftPlus|82.596%|5.6286%|1.3666|0.6517|
|Leaky ReLU|88.02%|3.795%|0.304|0.0898|
|PReLU|86.213%|4.848%|1.0642|0.5222|

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
