🎬 One-Handed DaVinci Resolve Hackpad
Overview

This project is a one-handed, ergonomic hackpad designed specifically to improve the video editing workflow in DaVinci Resolve, with a strong focus on the Cut Page and Edit Page.

The goal of this hackpad is to replace most keyboard interactions during editing, allowing the user to work efficiently with one hand on the hackpad and the other hand on the mouse.
It is optimized for reportage and documentary-style editing, where fast navigation, precise trimming, and clip management are essential.

The hackpad uses a key matrix, two rotary encoders, and a minimal number of inputs to stay within competition constraints while still offering advanced functionality through layer-based firmware logic.

🧠 Design Philosophy

One-handed operation (left hand)

Short finger travel and intuitive layout

Encoder-based timeline control for speed and precision

Minimal number of inputs, maximum functionality

Designed specifically around DaVinci Resolve shortcuts

📸 Overall Hackpad

Screenshot of the assembled hackpad

(Insert screenshot or rendered image of the full hackpad here)

⌨️ Input Layout & Functions

The hackpad consists of 12 mechanical keys and 2 rotary encoders.

Key Layout (4×3 Matrix)
Position	Function
Undo	Previous Cut
Up	Encoder 1 Push
In	Out
Cut	Ripple Delete
Encoder Functions

Encoder 1 (Jog / Playback)

Rotate: Move timeline (coarse)

Press: Play / Pause

Press + Rotate: Move timeline (fine)

Encoder 2 (Timeline / Clip)

Rotate: Timeline zoom

Press: Select clip

Press + Rotate: Move selected clip

🧩 Firmware

The firmware is written in KMK (CircuitPython-based) and uses:

A key matrix to reduce GPIO usage

Multiple layers to enable encoder context switching

Momentary layers triggered by encoder push buttons

The firmware allows complex behavior without exceeding the GPIO limitations of the Seeed XIAO RP2040.

📐 Schematic

Screenshot of the schematic

(Insert screenshot of the full schematic here)

Notes:

4×3 key matrix with per-switch diodes

Column-to-row diode orientation

Encoder pins wired directly to GPIOs

Encoder push buttons integrated into the matrix

🟩 PCB Design

Screenshot of the PCB

(Insert screenshot of the PCB layout here)

PCB Details:

2-layer PCB

Size ≤ 100mm × 100mm

Through-hole components only

Matrix-based switch routing

Designed specifically for easy soldering

🖨️ Case Design & Assembly

Screenshot of the case and assembly view

(Insert exploded view or assembled case screenshot here)

Case Characteristics:

Fully 3D printed (no acrylic or laser-cut parts)

Ergonomic tilt (~10–15°)

Designed for left-hand use

Heatset inserts for durability

Compact footprint for desk use

📦 Bill of Materials (BOM)
Part	Quantity
Seeed XIAO RP2040 (through-hole)	1
MX-style mechanical switches	12
EC11 rotary encoders	2
1N4148 diodes (through-hole)	12
0.91" OLED display	1
SK6812 MINI-E LEDs	up to 12
Blank DSA keycaps	12
M3x16mm screws	4
M3 heatset inserts	4
3D printed case parts	1 set
✅ Competition Requirements Checklist

✔ Approved parts only

✔ Through-hole XIAO RP2040

✔ PCB ≤ 100×100mm

✔ Case ≤ 200×200×100mm

✔ ≤ 16 inputs

✔ 2-layer PCB

✔ Fully 3D printed case

🚀 Conclusion

This hackpad is designed as a practical, real-world editing tool, not just a macro pad.
By combining a well-thought-out physical layout with intelligent firmware design, it enables fast, precise, and ergonomic editing in DaVinci Resolve.
