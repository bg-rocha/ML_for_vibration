# Machine Learning for predictive maintenance on rotating machinery
Bruno Gonçalves Rocha and João Guilherme Cotta Machado de Souza, 2021

This repository stands for our final project at UFPR (Universidade Federal do Paraná) Mechanical Engineering.

## ABSTRACT
The application of concepts and tools of Industry 4.0 is fundamental to potentialize the competitiveness in companies. The use of technologies and methodologies such as machine learning is fundamental in this process. Considered a significant factor in an organization's cost structure, maintenance can and should be improved through these methods, aplying what is now called predictive maintenance. Due to the applicability of this concept, this work has as main objective classifying failure modes in rotating machines through machine learning and predicting possible failures with the trained algorithm. To achieve this, a MAchinery FAUlt DAtabase (MAFAULDA) will be used, serving as input for the training of the machine, as well as data collected through bench top experiments, which will be sorted by the algorithm. The experimental phase had 70 experiments, carried out with different configurations of accelerometer positioning, rotation and failure modes. With Python, the comparison of the accuracy obtained by distinct machine learning models in the dataset classification allowed defining the Random Forest Classifier model for the final classification of the experiments. To perform this, it was necessary to generalize the available dataset, since it was highly specific to the system involved and resulted in unsatisfactory levels of accuracy for the classification of dissimilar systems. Fundamental for this stage was the analysis of acceleration by time and frequency domain plots generated from the information collected on the bench. The selected model reached accuracy of 100% for MAFAULDA and 87.14% in the classification of the experiments. Once the objectives were met, it could be concluded that it is possible to classify failure modes in rotating machines through machine learning and to apply this tool in predictive maintenance, predicting machinery failures and avoiding additional costs.

## What was done?
This work can be splited in 3 main parts:
  * Download, analysis, extract, create, train and validate a machine learning model for MAFAULDA
  * Perform experiments in a different machine to simulate MAFAULDA, and create a new dataset
  * Merge, transform and generalize, the two datasets to perform a new classification

![flowchart](https://github.com/bg-rocha/imgs/blob/main/TCC.png?raw=true)
 

### About MAFAULDA

MAFAULDA stands for Machinery Fault Database. It's a project from UFRJ that makes available a large dataset (+13GB) with diferent condition of operation and faults for a rotating machinery. For more information visit [MAFAULDA's web page](http://www02.smt.ufrj.br/~offshore/mfs/page_01.html).


### Experiments

Due to physical limitation of the setup avaliable we only simulate normal and imbalance conditions. The results of this are 70 excel files with acceleration and FFT data.
For more information about the experiments please read the full work in PDF (portuguese only) avaliable on github.

## Final Classifier:

Our final classifier is avaliable via Heroku [here](https://ml-vibration-classifier.herokuapp.com/) (portuguese only)
