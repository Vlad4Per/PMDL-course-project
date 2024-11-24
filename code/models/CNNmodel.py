import torch.nn as nn
from torchvision import models, transforms


class CNNClassificationModel(nn.Module):
    def init(self, num_classes=11):
        super(CNNClassificationModel, self).init()
        self.model = models.efficientnet_b0(pretrained=True)  # Use EfficientNet-B0
        self.model.classifier[1] = nn.Linear(self.model.classifier[1].in_features, num_classes)

    def forward(self, x):
        return self.model(x)
