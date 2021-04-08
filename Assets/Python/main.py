import sys
import os
from movements import *
from contours import write_image_contours

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Pass the name of an image as argument. The image must be in Images/Originals/ folder.")
    image_name = sys.argv[1]
    write_image_contours(image_name)

    print("Contours image done.")

    print("Generating moves sequence: this may take a few minutes.")

    figure = LoadImage(image_name)
    firstPos, first_moves = FirstPosition(figure)
    sequence = Play(figure, firstPos)
    if len(first_moves) != 0:
        moves = np.concatenate((np.array(first_moves), np.array(sequence)))
    else:
        moves = sequence
    
    gcode_destination = "../GCode/"+os.path.splitext(image_name)[0]+"_moves.gcode"
    ExportGCode(moves, gcode_destination)

    print("Moves generated. You can now use the "+os.path.splitext(image_name)[0]+"_moves.gcode file in Unity.")
