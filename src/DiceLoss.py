import torch
import torch.nn as nn
class DiceLoss(nn.Module):
    """
    Dice loss
    """

    def __init__(self):
        super(DiceLoss, self).__init__()

    def forward(self, inputs, targets, eps=1e-6):
        """
        Calculation of dice loss

        :param inputs: model predictions
        :param targets: target values
        :param eps: stability factor, defaults to 1e-6
        :return: loss value
        """
        predictions = torch.argmax(inputs, dim = 1)
        ground_truth = targets
        
        # implement dice loss
        dice_loss_per_channel = 1 - (2 * torch.sum(predictions * ground_truth, dim=(1, 2)) + 1) / (
        torch.sum(predictions, dim=(1, 2)) + torch.sum(ground_truth, dim=(1, 2)) + 1)

        return torch.mean(dice_loss_per_channel)