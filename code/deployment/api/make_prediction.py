import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from CNNmodel import CNNClassificationModel
from preproc_img import load_training_img

def predicted_age(madel_path, img_path):
    def predict(model, test_loader, device):
        """
        Run model inference on test data
        """
        predictions = []
        with torch.no_grad():
            model.eval()  # evaluation mode
            test_loop = tqdm(enumerate(test_loader, 0), total=len(test_loader), desc="Test")

            for inputs in test_loop:
                # Write your code here
                # Similar to validation part in training cell
                id, pred = inputs
                pred = pred.to(device)
                _, predicted = torch.max(model(pred).data, 1)

                # Extend overall predictions by prediction for a batch
                predictions.extend([i.item() for i in predicted])
            return predictions


    model = CNNClassificationModel()
    ckpt = torch.load(madel_path)
    model.load_state_dict(ckpt)

    batch_size = 128
    # process test data and run inference on it
    images = torch.stack(
        [load_training_img(img_path)])

    test_loader = DataLoader(images, batch_size=batch_size, shuffle=False)
    predictions = predict(model, test_loader, device='cpu')

    decode = {
        0: "1-5", 1: "5-10", 2: "10-15", 3: "15-20", 4: "20-25", 5: "25-30", 6: "30-40", 7: "40-50", 8: "50-60", 9: "60-70",
        10: "70+"
    }

    print(f"Predicted age for the person on the picture: {decode[predictions[0]]}")
    return decode[predictions[0]]