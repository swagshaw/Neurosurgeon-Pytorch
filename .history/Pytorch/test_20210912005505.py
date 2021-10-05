'''
Descripttion: 
version: 
Author: Yang Xiao(YXIAO009@e.ntu.edu.sg)
Date: 2021-09-12 00:53:56
LastEditors: Yang Xiao
LastEditTime: 2021-09-12 00:55:05
'''
from torchvision import models



original_model = models.alexnet(pretrained=True)
print(*list(original_model.features.children())[:-3])