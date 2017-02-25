# my_utils

Utility functions frequently used in many projects.


## get_seq
```
my_utils get_seq [-h] reference.fa region
```

Example script for using in individual scripts.
```
import my_utils.seq

seq = my_utils.seq("reference.fa", "1:1-10000")
print seq
```
where, "reference.fa" is the path to the reference genome file.


## reverse_complement

```
my_utils reverse_complement [-h] seq_str
```


