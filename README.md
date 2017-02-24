# MirrorAI
AI-bot aiming to pass the Mirror test

## Usage
Since this package is still under development,  
you can use the development mode:
```
python setup.py develop
```
This command will make the `MirrorAI` module
available to you.

## Example
```python
from MirrorAI import dataset
count = 100 # total number of samples
height = 3  # image height
width = 2   # image width
low = 1     # lowest category ID
high = 9    # highest category ID
d = dataset.symmetric.sample(count, height, width, low, high)
```

The output `d` is dictionary of this structure:
```
{
    "data": [[1,2], ...],
    "labels": [[0,1],[1,0], ...]
}
```

