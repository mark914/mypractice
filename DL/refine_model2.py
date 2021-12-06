import torch
from torch import optim
from torchvision import models
path_state_dict = None
def get_model(path_state_dict, vis_model=False, device="cpu"):

    alexnet = models.alexnet()
    state_dict = torch.load(path_state_dict)
    alexnet.load_state_dict(state_dict)

    if vis_model:
        from torchsummary import summary
        summary(alexnet, (3, 224, 224), device="cpu")


    alexnet.to(device)
    return alexnet


alexnet_model = get_model(path_state_dict, vis_model=False)
LR = 1e-3
# 冻结卷积层
flag = 0
# flag = 1
if flag:
    fc_params_id = list(map(id, alexnet_model.classifier.parameters()))  # 返回的是parameters的 内存地址
    base_params = filter(lambda p: id(p) not in fc_params_id, alexnet_model.parameters())
    optimizer = optim.SGD([
        {'params': base_params, 'lr': LR * 0.1},  # 0
        {'params': alexnet_model.classifier.parameters(), 'lr': LR}], momentum=0.9)

else:
    optimizer = optim.SGD(alexnet_model.parameters(), lr=LR, momentum=0.9)  # 选择优化器
