import torch

def F1(groundtruth_mask, pred_mask):
    intersect = torch.sum(pred_mask * groundtruth_mask, axis=[1, 2, 3])
    total_sum = torch.sum(pred_mask, axis=[1, 2, 3]) + torch.sum(groundtruth_mask, axis=[1, 2, 3])
    dice = 2*intersect / total_sum
    return dice.numpy()