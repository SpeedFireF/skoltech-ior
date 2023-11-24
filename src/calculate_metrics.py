import torch

def F1(groundtruth_mask, pred_mask):
    intersect = torch.sum(pred_mask * groundtruth_mask, dim=[1, 2])
    total_sum = torch.sum(pred_mask, dim=[1, 2]) + torch.sum(groundtruth_mask, dim=[1, 2])
    dice = 2*intersect / total_sum
    return dice