from tensorflow import keras
from tensorflow.keras import layers

def get_data_augmentation():
    return keras.Sequential(
        [
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.2),
            layers.RandomContrast(0.2),
            layers.RandomBrightness(factor=0.2),
            layers.RandomTranslation(0.1, 0.1),
        ]
    )