

## Data Augmentation Combinations
DATA1 - Brightness=0.3   
DATA2 - Contrast=0.3  
DATA3 - Saturation=0.3  
DATA4 - Hue=0.15

DATA5 - RandomCrop(224, padding=28)  
DATA6 - RandomHorizontalFlip(0.5)  
DATA7 - RandomVerticalFlip(0.5)

DATA8 - RandomCrop(224, padding=28) + RandomHorizontalFlip(0.5)  
DATA9 - RandomCrop(224, padding=28) + RandomVerticalFlip(0.5)
