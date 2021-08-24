import torch
import torchvision

class WeakFewshot_Segmentation(nn.Module):
    def __init__(self):
        super(WeakFewshot_Segmentation, self).__init__()
 		self.encoder = torchvision.models.resnet50(pretrained=True)
        pass

    def forward(self, x_query, y_support, if_sameClass)

    	# x_query: [batchsize, 3, 256, 256]
    	# y_support: [batchsize, 3, 256, 256]
    	# if_sameClass: [batchsize]

    	pass

