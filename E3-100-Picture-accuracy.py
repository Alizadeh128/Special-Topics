import torch
from torchvision import transforms, models
from PIL import Image
import urllib.request

def preprocess_image(image_url):
    fpath = 'temp_image.jpg'
    urllib.request.urlretrieve(image_url, fpath)
    img = Image.open(fpath)
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225])])
    img_tensor = transform(img)
    batch = torch.unsqueeze(img_tensor, 0)
    return batch

def predict_image(model, batch):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.eval()
    model.to(device)
    with torch.no_grad():
        batch = batch.to(device)
        y = model(batch)
        return y

model = models.alexnet(pretrained=True)

url = "https://raw.githubusercontent.com/joe-papa/pytorch-book/main/files/imagenet_class_labels.txt"
fpath = 'imagenet_class_labels.txt'
urllib.request.urlretrieve(url, fpath)
with open(fpath) as f:
    classes = [line.strip() for line in f.readlines()]

correct_count = 0

image_urls = [...]  # لیستی از آدرس‌های تصاویر آزمون

for image_url in image_urls:
    batch = preprocess_image(image_url)
    y = predict_image(model, batch)
    _, index = torch.max(y, 1)
    predicted_class = classes[index.item()]
    actual_class = "desired_class"  # کلاس مورد نظر خود را اینجا قرار دهید
    if predicted_class == actual_class:
        correct_count += 1

accuracy = (correct_count / len(image_urls)) * 100
print("Model Accuracy: {:.2f}%".format(accuracy))
