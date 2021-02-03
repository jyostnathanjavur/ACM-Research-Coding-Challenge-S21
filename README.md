# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

SOLUTION 

First, I saw a couple of youtube videos and website information on how to analyze,download and read a genome sequence using programming languages and get more informaion from the DNA sequence alone. I came across the basic genomic visualization known as Circoletto and CGView API. From this, I was able to figure out how the gene mapping works and featuring each gene with specific colors and lengths. There were several different programming languages such as C++, Java and Python being used to draw a genome map and I have prior experience to all of them but Python was the easiest language to implement.So, I used Python to form the map. For Python, the genome mapping method was GenomeDiagram and and I installed the relevant libraries such as biopython and reportlibrary gave me a better understanding of the creation of the map and reading the genomic sequence.I went through several sample codes on how to use the GenomeDiagram and samples on the creation of the maps. The biopython library needed additional C++ Visual Studio Build Tools to run through the code. The main approach was that I initially read the genome file and used the GenBank file. Then, created and edded an empty diagram and stored an empty feature set. Bsed on the feature type, the code will continue and alternate colors on each section of the map for each gene based on the length of the gene. Finally, specified the format of the map as circular. 

The libraries used are: 
reportlab, biopython

Sources Used: 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6728899/'
https://www.youtube.com/watch?v=FEvaKOZDDBk
https://academic.oup.com/bioinformatics/article/22/5/616/205776
https://biopython.org/wiki/Download
https://www.youtube.com/watch?v=IUPX0-BPl4c
