from torchvision import models
import torch
from torch import nn

num_classes = 2
model_ft = models.vgg16(pretrained=True)

for param in model_ft.parameters():
    param.requires_grad = False

class Vgg_added_features(nn.Module):
    def __init__(self, originalModel):
        super(Vgg_added_features, self).__init__()
        self.features = nn.Sequential(*list(originalModel.features)[:-1])
        self.classifier = nn.Linear(512*512, num_classes)
        #self.avg_pool = nn.AdaptiveAvgPool2d((7,7))
    
    def forward(self, x):
        print(x.shape)
        x = self.features(x).view(-1,512,12*14*14)
        print(x.shape)
        x = torch.matmul(x, x.permute(0,2,1)).view(-1,512*512)/12*14*14.0
        print(x.shape)
        x = torch.mul(torch.sign(x),torch.sqrt(torch.abs(x)+1e-12))
        print(x.shape)
        x = F.normalize(x, p=2, dim=1)
        print(x.shape)
        x = self.classifier(x)
        print(x.shape)
        return x

model = Vgg_added_features(model_ft)
print(model)