# GUI CanSat

Graphical User Interface (GUI) using the Tkinter library for controlling a CanSat (Can Satellite) station named "Meteor Racers", in the 2023 PEU UNAM Iberoamerican Canned Satellites Competition. The GUI is designed to display various information and control options related to the CanSat system.

The GUI window is created with a title and resizable dimensions, and it includes background images and logos using the Canvas widget. It features a menu for selecting a variable to be graphed, such as temperature, pressure, or orientation. The selected variable is then plotted on a graph using Matplotlib.

Additionally, the GUI includes indicators for the state of the gyro (autogyro) and data transmission, represented by colored circles. Other elements, such as measured values for temperature, orientation, pressure, velocity, and distances, are displayed as text on the interface. A real-time watch is also included to display the mission time in hours, minutes, and seconds.
