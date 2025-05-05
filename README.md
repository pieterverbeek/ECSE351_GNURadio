# ECSE351_GNURadio

## Problem 2.3 - Thresholding Demonstration

**Criteria:**
1. Signal source blocks with modulation index and other controls
2. Gain state to set relative amplitudes
3. Receiver block per modulation mode
4. Visualization and audio output

**Ran into serious roadblock**
For the scaling between the two signals, I intended to use the Python Block to convert a slider in dB to a decimal scaling factor. I ran into issues with not being able to edit to code on Mac. I implemented several strategies which did not ultimately work.

- Used different text editors: XCode, VSCode, TextEditor, TextMate, RStudio(desperation), Chrome, Notepad, Terminal
- Directly edit the .grc code to insert a code block in without placing it and move it around later. This had some success in the sense that I made a code block that was on the screen, but it was a struggle to make all the connections correct. I can tell this approach would take hours to do what would take minutes ordinarily, but would probably work eventually
- Create and edit config files for GNURadio Companion to default to different text editor apps
- Edit the .py flow code to make temporary changes each run

Many of these methods were inspired by this thread and related ones:
[Link](https://github.com/gnuradio/gnuradio/issues/7115)

There were no eureka moments on this thread either. and I think that I would rather use anything else than Mac if I were to try and solve this in the future. For now I will just have an entry based scaling setup between the signals as dB will be difficult without the Python block.

