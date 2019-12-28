"""
Python module for holding our PyTorch trainers.

Trainers here inherit from the BaseTrainer and implement the logic for
constructing the model as well as training and evaluation.
"""

def get_trainer(name, **trainer_args):
    """
    Factory function for retrieving a trainer.
    """
    if name == 'generic':
        from .generic import GenericTrainer
        return GenericTrainer(**trainer_args)
    else:
        raise Exception('Trainer %s unknown' % name)
