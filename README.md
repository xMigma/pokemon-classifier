# Pokemon Image Classifier

A deep learning project for classifying Generation 1 Pokémon images using TensorFlow and Keras.

## Overview

This project implements a Convolutional Neural Network (CNN) to classify images of 149 different Pokémon from Generation 1. It includes both a custom CNN architecture and transfer learning using VGG16.

## Features

- **Data Pipeline**: Automated dataset download from Kaggle and train/val/test splitting (70/20/10)
- **Data Augmentation**: Random flips, rotations, zoom, contrast, brightness, and translations
- **Model Architectures**: Custom CNN and VGG16-based transfer learning
- **Training Utilities**: Early stopping and model checkpointing callbacks
- **Visualization**: Training metrics plotting and class distribution analysis

## Project Structure

```
├── pokemon_classifier.ipynb   # Main notebook with full pipeline
├── utils/
│   ├── callbacks.py           # Training callbacks (EarlyStopping, ModelCheckpoint)
│   ├── data_augmentation.py   # Data augmentation layers
│   ├── evalutation.py         # Model evaluation utilities
│   └── visualization.py       # Plotting functions
└── README.md
```

## Requirements

- Python 3.x
- TensorFlow / Keras
- NumPy
- Matplotlib
- Pillow
- Kaggle API (for dataset download)

## Usage

1. Configure Kaggle API credentials
2. Run the notebook cells sequentially to:
   - Download and extract the dataset
   - Split data into train/validation/test sets
   - Train and evaluate the model

## Dataset

The dataset is sourced from [Kaggle - Pokemon Generation One](https://www.kaggle.com/datasets/thedagger/pokemon-generation-one) and contains images of all 149 Generation 1 Pokémon.

## License

MIT
