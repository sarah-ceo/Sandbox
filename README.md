# Sandbox

This is a school project: a marble draws an image in the sand in Unity. 

(After the 3D simulation, we were supposed to build a physical sandbox and use Arduino-controlled DC motors with a magnetic marble. However, we never got to this phase due to COVID-19 and the closing of our school.)

## Instructions

1- Generate moves sequences using Python:

Place your image in Assets/Images/Originals/ folder. 

Run Assets/Python/main.py with your image name in argument.

Example: 
![](/Demonstrations/python-command.png)

This will create a contours image in the Assets/Images/Contours/ folder and a .gcode text file in the Assets/GCode folder.


2- Choose the GCode file in Unity:

In the Marble object inspector: scroll down to the "Marble Tracks (Script)" component and drag-and-drop the new .gcode text file in the GCodeFile field.

Example:

<img src="/Demonstrations/unity-editor.png" width="574" height="343">

Make sure to activate "Maximize on Play" within the Unity Game panel.

## Demonstrations

<img src="/Demonstrations/dog.png" width="306" height="234">
<img src="/Demonstrations/dog_contour.png" width="306" height="234">
<img src="/Demonstrations/dog_demo.gif" width="450" height="300">


<img src="/Demonstrations/world.jpg" width="300" height="300">
<img src="/Demonstrations/world_contour.jpg" width="300" height="300">
<img src="/Demonstrations/world_demo.gif" width="450" height="300">
