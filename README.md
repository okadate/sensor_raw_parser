# sensor_raw_parser
Measurement sensor's raw data parser
(c) 2021 OKADA Teruhisa

## Sensors
- CA       CastAway CTD
- HOBO     U20 water level loger, U26 DO loger
- AT600    Aqua Troll 600
- RINKO    RINKO Profiler
- AAQ      RINKO AAQ 
- Infinity RINKO W
- DEFI     DEFI2-L
- MFL      Multi-excitation fluorometer

## Example
```py
from sensor_raw_parser import CA

df = CA.read_csv(f)
```

## Requirements

- seawater (CA)
```
conda install -c conda-forge seawater
```

- bs4 (AT600)
```
conda install -c conda-forge beautifulsoup4
```
