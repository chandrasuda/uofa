# Nairobi Dataset:
---
Dataset consists of passive and forced cough sounds and features (coughs = 33K) of participatants with Tuberculosis (TB) or other underlying pulmonary health conditions (non-TB). 



## Description of the Data and file structure
The dataset consists of two sets of cough - passive (natural) coughs and forced (voluntary) coughs. Coughs have been recorded using three devices: smartphone(pixel), boundary microphone(codec), and high end condenser microphone (yeti). 

Audio files were annotated by human annotators at the University of Washington using Audacity software. Coughs with background noise such as fan, door, speech, or other respiratory sounds like a sneeze or clearing of nose/throat were discarded. Each cough sound was processed to have a fixed length of 1 second and stored as wave file. Recordings greater than a second were divided into multiple audio files and audios with length less than 1 second were centered and padded with zeroes to make them one second long. Scalograms are generated using complex Morlet transform.Mel spectrogram features are generated using Pytorch's torchaudio and additionally using vggish embeddings. These features are stored as numpy files.

Some cough audio files have been removed based on subject consent. Cough features of all the coughs are shared. 

Metadata.csv contains subject details, symptoms reported by subjects, and various test results related to TB. Column names and associated key is provided in Dataset_key.csv.

Passive_coughs.csv and Forced_coughs.csv contains path to files in Passive coughs and Forced coughs along with subject metadata. Raw audio (.wav) files exist only for rows that have Permission_sound =='yes'.

<pre>
├── Forced_Coughs
    ├── Audio_files
    ├── Scalogram_numpy
    ├── Melspectrogram_numpy
        ├── Vggish_embeddings
        ├── pytorch_embeddings
    └── Forced_coughs.csv
├── Passive Coughs
    ├── Audio_files
    ├── Scalogram_numpy
    ├── Melspectrogram_numpy
        ├── Vggish_embeddings
        ├── pytorch_embeddings
    └── Passive_coughs.csv
├── Metadata.csv
├── Dataset_key.csv
└── README.md
    
</pre>


## Sharing/access Information
Cite "TBscreen: Sharma et. al. A Passive Cough Classifier for Tuberculosis Screening with a Controlled Dataset. Science Advances, 2024". for any use of data or code.


## Code/Software
Accompanying code to generate features and load dataset are provided at: https://doi.org/10.5281/zenodo.10431329.

<pre>
├── audio_preprocessing
    ├── cough_processing.py
    ├── generate_melspec.py
    ├── generate_vggish.py
    ├── generate_wavelet.py
    ├── generate_waveletImages.py
    └── wavelet_to_image_params
├── dataset_loaders
    ├── datasetload_spectralfeatures.py
    └── datasetload_waveletImage.py
├── Figures
    ├── datacsv
        ├── folds
        ├── result_baseline
        ├── result_scalogram
        └── result_tb_multiclass
    ├── R_scripts
        ├── ci_bootstrap.R
        └── ROC_CI.R
    ├── Binary_model_metrics.ipynb
    ├── Fig2_coughCounts.py
    ├── Fig4_ROC.py
    ├── SupplementalFig2_ROC.ipynb
    ├── SupplementalFig3a.ipynb
    ├── SupplementalFig3b.ipynb
    └── SupplementalFig3c.ipynb
├── train_scripts
    ├── earlystopping.py
    ├── prediction.py
    ├── train_tb.py
    └── train_tb_multiclass.py
├── utils
    ├── audioset
        ├── mel_features.py
        ├── vggish_input.py
        ├── vggish_params.py
        ├── vggish_postprocess.py
        └── vggish_slim.py
    ├── model
        ├── Modelresnet.py
        ├── pytorch_vggish.pth
        └── vggish.py
    └── TB_multiclass_foldsGen.ipynb    
├── predict_k_fold_scalogram.py
├── train_k_fold_scalogram.py
├── train_k_fold_scalogram_multiclass.py
├── train_k_fold_mspec.py
├── train_k_fold_vggish.py
├── requirements
└── README.md
    
</pre>



