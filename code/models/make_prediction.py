import torch
from torch.utils.data import DataLoader

from CNNmodel import CNNClassificationModel
from preproc_img.preproc_img import load_training_img

decode = {
    0: "1-5", 1: "5-10", 2: "10-15", 3: "15-20", 4: "20-25", 5: "25-30", 6: "30-40", 7: "40-50", 8: "50-60", 9: "60-70",
    10: "70+"
}


def predicted_age(img_path, model_path='/models/best.pt'):
    def predict(model, test_loader, device):
        """
        Run model inference on test data
        """
        predictions = []
        with torch.no_grad():
            model.eval()  # evaluation mode

            for inputs in enumerate(test_loader, 0):
                id, pred = inputs
                pred = pred.to(device)
                _, predicted = torch.max(model(pred).data, 1)

                predictions.extend([i.item() for i in predicted])
            return predictions

    model = CNNClassificationModel()
    ckpt = torch.load(model_path)
    model.load_state_dict(ckpt)

    batch_size = 128

    images = torch.stack(
        [load_training_img(img_path)])

    test_loader = DataLoader(images, batch_size=batch_size, shuffle=False)
    predictions = predict(model, test_loader, device='cpu')

    return predictions[0]
