# Predicting neural spike times from hippocampal local field potential features and mouse spatial position

This project investigates whether neural spike timing in the hippocampus can be predicted from theta-phase local field potential (LFP) features and mouse spatial position.

## Overview
Using hippocampal LFP and behavior data from the Allen Brain Observatory, trained a supervised linear regression model to predict neural spike times. Results suggest that theta phase and mouse position carry structured information about neural activity. This work supports the potential for decoding neural signals from non-invasive or indirect sources.

## Features
- Preprocesses spike times, LFPs, and running speed data
- Extracts theta-phase features from LFP using bandpass filter + Hilbert transform
- Estimates spatial position from running speed
- Aligns multimodal data by timestamp
- Trains and evaluates a linear regression model in Python (scikit-learn)
- Strong performance achieved (R^2 = 0.918)

## Installation
```bash
# Clone the repo
git clone https://github.com/user/hippocampal-spike-prediction.git
cd hippocampal-spike-prediction

# Install dependencies
pip install -r requirements.txt
```

## Acknowledgements
Thank you to Dr. Mayank Mehta from the UCLA Mehta Lab for his mentorship and guidance. Data provided by the Allen Brain Observatory (Visual Coding - Neuropixels).
