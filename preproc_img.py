import PIL.Image
import torchvision.transforms as transforms
import torch


def load_training_img(fname):
    rgba_image = PIL.Image.open(fname)
    rgb_image = rgba_image.convert('RGB')
    img = rgb_image

    # Write your code here
    transform = transforms.Compose([
        transforms.PILToTensor(),
        transforms.Lambda(lambda x: x / 255),
        transforms.ConvertImageDtype(torch.float32),
        transforms.Resize((224, 224)),  # Resize to a consistent input size
        transforms.RandomHorizontalFlip(p=0.5),  # 50% chance of flipping
        transforms.ColorJitter(brightness=0.1,  # Slight color adjustments
                               contrast=0.1,
                               saturation=0.1,
                               hue=0.05),
        transforms.RandomRotation(degrees=5),  # Small rotation to keep natural orientation
        transforms.Normalize(mean=[0.485, 0.456, 0.406],  # ImageNet normalization
                             std=[0.229, 0.224, 0.225]),
        transforms.ConvertImageDtype(torch.float32)
    ])  # Convert to float32 for model compatibility
    transforms.ToPILImage()(transform(img)).show()

    return transform(img)
