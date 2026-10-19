# resistor color code checker

Small Python script that turns the color bands on a resistor into a value and checks if your multimeter reading is within tolerance.

I'm learning electronics and robotics from zero. Built with AI help, but I didn't just run it: I went through the code step by step until I could explain every line and how it all fits together. Then I tested it against my own multimeter readings and added the german color names and purple myself. The commit history shows each step.

## usage

```
python3 resistor_color_code.py
```

```
Colors (e.g. yellow violet brown gold): gelb violett braun gold
Value: 470 Ω ±5 %
Allowed: 446.5 Ω to 493.5 Ω
Measured value in ohms (Enter to skip): 463.8
463.8 Ω is within tolerance.
```

- 4 and 5 band resistors work
- english or german color names (grey/gray and purple are fine too)
- comma or dot for the measured value

## why

I measured my first resistor at 463.8 Ω and wanted to know if that's actually a 470 Ω one. Reading the bands by hand got old fast.
