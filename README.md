# Entropy-Optimal Sorting For Random-Shuffled Sequences With Shot Change Robustness
Final Project for CMU 11-785 Deep Learning  
Team 17: I-Tsun Cheng, Tz-Ruei Liu, Yuanyuan Wang, Tianrun Wang

This is the official codebase for our project. The code can be structured into two components: ``Data`` and ``Models``.

## Data
The ``data`` folder contains the following three folders:
- ``data``: the datasets used for different input sequence configurations for our main experiments (1+1, 2+1, 3+1, 4+1, 5+1)
- ``utilities``: the data utilties used for generating the datasets

To generate the ``.csv`` files for each input configuration in the ``data`` folder, navigate to the ``utilities`` folder. Run ``get_shot_lists.py`` which will take ``knnw_labels.csv`` and output a list of shots in ``shot_list.csv``. Then, run ``get_data.py`` to generate all the ``.csv`` dataset files by inputting ``shot_list.csv``.

## Models
The ``models`` folder contains all of the models that are implemented and tested in our experiments. Here is an overview of the ``models`` folder:
- ``direct``: The models we implemented and trained for our main set of experiments
    - ``baseline_approach``: The models implemented using the baseline approach
    - ``proposed_approach``: The models implemented using our proposed approach
    - ``data_augmentation``: The best model trained using our proposed approach with different data augmentation techniques (.README file provided in the respective folder for more details)
- ``pairwise``: The models that we attempted using the pairwise prediction approach mentioned in our ablation study



## Code Citations
Here we would like to attribute the code that we referenced for our model implementations:

EfficientNet from scratch reference: https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/tree/master/pytorch_classification/Test9_efficientNet  
RegNet code reference: https://github.com/facebookresearch/ClassyVision/blob/main/classy_vision/models/regnet.py


