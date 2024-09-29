from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

def get_callbacks(checkpoint_path, patience=10):
    early_stopping = EarlyStopping(
        monitor="val_loss", 
        patience=patience, 
        restore_best_weights=True
    )

    model_checkpoint = ModelCheckpoint(
        filepath=checkpoint_path,
        monitor="val_loss",
        save_best_only=True
    )

    return [early_stopping, model_checkpoint]
