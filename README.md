# Description
The script simulates Conway's Game of Life.
It is a simple GUI application based on Qt framework. 

# Pre-requirments 
- `python >= 3.8` installed in the system

# How to install
This package is managed by `setuptool`, but for some unidentified reason the installation of QT5 via setuptool does not work properly, so simply use requirements.txt.
To install dependencies use:
 
```shell
cd game_of_life_simulation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
python3 setup.py install
```

# How to run 

Activate `venv` if not already active:
```shell
cd game_of_life_simulation
source venv/bin/activate
```

Run python command line script with all args:
```shell
python3 game_of_life_simulation_package/main.py'
```

Provide simulation parameters in the GUI window, generate first state using 'Generate Life' button and run the simulation using 'Run' button.

# How it works
Script:
1) opens the GUI window 
2) generate first state of alive cells based on provided arguments in text edits widgets
3) paints generated alive cells in canvas when 'Generate Life' button is clicked
4) run the simulation based on Conway's rules when 'Run' button is clicked
5) pause the simulation when 'Stop' button is clicked
6) 'revive' additional cell when spot in the canvas is clicked.
