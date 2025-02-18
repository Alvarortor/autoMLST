# autoMLST
Program to assist in rapid sequence typing of assembled or unassembled isolates

# README for autoMLST.py

## Overview

autoMLST is a tool designed to automatically determine the sequence type (ST) of sequenced isolates (can be assembled or unassembled). The program produced a file called MLST_results.txt which can then be pasted to the pubMLST batch lookup tool directly to rapidly get ST for specified isolates. 

## Important

MUST be in same directory as MUMmer to work, you can also change the file locations in line 33 of the code. 
---MUMmer only works with macOS or linux systems---

## System Requirements

**Operating System**: Compatible with Windows, macOS
**Python Version**: Python 3.6 or higher is required.
**MUMmer Version**: MUMmer 3.23

##How to use the program
1. Ensure MUMmer is on your device and is in the same location (unless modified) as the contents from the autoMLST folder
2. Create a file with isolate names you want to obtain the ST of, limit is one isolate per line.
3. Run "python autoMLST.py <your-isolate-file.txt>

## License

This program is distributed under the MIT License.
