# sensor_raw_parser

Measurement sensor's raw data parser
(c) 2021 OKADA Teruhisa

## Sensors

|Class    |Sensor
|---------|-----------------------------------
|CA       |CastAway CTD
|HOBO     |U20 water level loger, U26 DO loger
|AT600    |Aqua Troll 600
|RINKO    |RINKO-Profiler
|AAQ      |AAQ-RINKO
|Infinity |RINKO W (DO logger with wiper)
|DEFI     |DEFI2-L
|MFL      |Multi-excitation fluorometer

## Example

```py
from sensor_raw_parser import CA

df = CA.read_csv(f)
```

## Requirements

```
conda install -c conda-forge seawater
conda install -c conda-forge beautifulsoup4
```
