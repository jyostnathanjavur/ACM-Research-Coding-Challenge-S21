
#importing Python Libraries 

from reportlab.lib import colors #reportlab library for mapping colors and matplot library
from reportlab.lib.units import cm 
from Bio.Graphics import GenomeDiagram #biopython library for genomic diagram
from Bio import SeqIO #library to read file

#Reading the genome file using read function 
Store_File = SeqIO. read("Genome.gb", "genbank")

Gen_Diagram = GenomeDiagram.Diagram("Tomato curly stunt virus", "complete genome") #Creating empty diagram
Gen_Track = Gen_Diagram.new_track(1, name = "Annotated Features") #Adding empty Diagram 
Gen_newSet = Gen_Track.new_set() #Adding empty feature set 

#Initiating diagram features for the objects in the genome sequence file
#Switching colors between pink and green 

for feature in Store_File.features:
    if feature.type != "gene":
        continue
    if len(feature) % 9 == 0: #if length of genome multiple of 9 - the gene is represented by pink color
        color = colors.pink
    else:
        color = colors.green # else green

    Gen_newSet.add_feature(feature, color = color, label = True, label_size = 20) #Adding and labeling color and size features to the diagram

    #Creating the ouput file using write and draw functions
    Gen_Diagram.draw(format = "circular", circular = True, pagesize = (30 * cm, 30 * cm), start = 0, end = len(Store_File), circle_core = 0.8)
    Gen_Diagram.write("OutputFile.jpg", "JPG")