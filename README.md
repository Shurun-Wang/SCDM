# SCDM
PyTorch Source code for "A Robust Denoising Diffusion Architecture for Completing Missing Regions of Multiple Physiological Signals", Under Review. 

We will release the code when the article is accepted. You can also find other open-sourced biomedical signal analysis projects in my [academic](https://shurun-wang.github.io/) page. :relaxed: :relaxed: :relaxed:

## Requirements
<details>
  <summary>
    :point_left: python packages
  </summary>

   - dtw==1.4.0
   - einops==0.6.1
   - ipython==8.14.0
   - ipywidgets==7.6.5
   - matplotlib==3.5.1
   - numpy==1.23.5
   - pandas==1.4.2
   - pypots==0.1.1
   - scikit_learn==1.1.3
   - scipy==1.11.2
   - seaborn==0.11.2
   - torch==2.0.1
   - tqdm==4.64.0
</details>

## Data Preparation

 - ECG/EMG/EEG data have been already processed in
  
    `Dataset/ECG/processed_data/`
 
    `Dataset/EMG/processed_data/`

    `Dataset/EEG/processed_data/`

## How to run this project
This project contains four main files as follows:

### Step 1: Completing the signals through the proposed methods
`python main_signal.py `
- Here, you can train/validate/test the proposed model.
  - The training procedure is used to record the model under different cases
  - The validation procedure is used to select the proper model structure
  - The testing procedure is used for investigating the coupling effect and the reults can be used to compare with other methods
- Also, you can configure the parameter for different settings.
  - The corresponding files are in  `/Core`

### Step 2: Completing the signals through tensor-based methods
`python main_tensor.py `
- Here, you can complete the missing regions through LATC/LAMC/BTMF/TRMF.
  - The corresponding files are in  `/Baseline`

### Step 3: The prediction results through dl-based methods 
`python main_predictor.py `
- Here, you can predict the missing regions through SAITS/Transformer/BRITS.
  - The corresponding files are in  `/Predictor`

### Step 4: Checking the classification results after completion 
`python main_classifier.py `
- Before run this file, you should finish step 1, step 2, and step 3.
  - The corresponding files are in  `/Classifier`


## Results
