# Sandbox

This is a school project: a marble draws an image in the sand in Unity.

Instructions:

1- Generate moves sequences using Python

Place your image in Assets/Images/Originals/ folder. 

Run Assets/Python/main.py with your image name in argument.

Example: 
![](/Demonstrations/python-command.png)

This will create a contours image in the Assets/Images/Contours/ folder and a .gcode text file in the Assets/GCode folder.

2- Choose the GCode file in Unity

In the Marble object inspector: scroll down to the "Marble Tracks (Script)" component and drag-and-drop the new .gcode text file in the GCodeFile field.

Example:
![](/Demonstrations/unity-editor.png)

Make sure to activate "Maximize on Play" within the Unity Game panel.

Demonstrations:
![](/Demonstrations/dog.png)
![](/Demonstrations/dog_contour.png)
![](/Demonstrations/dog_demo.gif)

![](/Demonstrations/world.png)
![](/Demonstrations/world_contour.png)
![](/Demonstrations/world_demo.gif)
