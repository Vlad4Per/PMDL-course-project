import torch.nn as nn
from torchvision import models, transforms


class CNNClassificationModel(nn.Module):
    def __init__(self, num_classes=11):
        super(CNNClassificationModel, self).__init__()
        self.model = models.efficientnet_b0(pretrained=True)
        self.model.classifier[1] = nn.Linear(self.model.classifier[1].in_features, num_classes)

    def forward(self, x):
        return self.model(x)
