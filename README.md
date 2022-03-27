# weakpass
Very basic weak passwords generator for Red Teams


<br>

### Usage  <br>

For small list (330 possibilities)

```
python3 weakpass.py -d targetname
```

For big list (942 possibilities)

```
python3 weakpass.py -d targetname -b
```

If you made a small list and want to complete the big one
```
python3 weakpass.py -d targetname -c 
```