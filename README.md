# sensor_raw_parser
Measurement sensor's raw data parser
(c) 2021 OKADA Teruhisa

## Sensors
- CastAway CTD
- HOBO water level loger
- HOBO DO loger
- Aqua Troll 600
- Rinko Profiler
- Rinko AAQ

## Example
```py
from sensor_raw_parser import CA

df = CA.read_csv(f)
```
