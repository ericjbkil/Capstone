pip install pdfminer

#make sure you're in the right directory (folder with your pdfs per patient)

#general layout for parsing of PDFs into plain text
pdf2txt.py -o name_of_output_file input_file.pdf

#removing ASCII characters
tr -cd '\11\12\15\40-\176' < file-with-binary-chars > clean-file

####metamap installation: from https://metamap.nlm.nih.gov/Installation.shtml #### 
# To extract the MetaMap distribution, use the following bunzip2 and tar commands substituting the appropriate 
# name of the file you downloaded (e.g., public_mm_linux_2010.tar.bz2, public_mm_macosx_2010.tar.bz2):

bunzip2 -c public_mm_<platform>_<year>.tar.bz2 | tar xvf - 

# This set of commands will create the distribution directory public_mm in the current working directory (<parent_directory>). 
# So you will have created <parent_directory>/public_mm.

# To begin the initial install, go to the directory created when you extracted the distribution (public_mm).
cd public_mm

# Tell the install program where your java installation is by setting the environment variable JAVA_HOME 
# to the Java installation directory.
# To find out where your java installation is located, use the following command:

which java

# To set the environment variable JAVA_HOME, use the information from the which command. For example, if the command: which java 
# returns /usr/local/jre1.8/bin/java, then JAVA_HOME should be set to /usr/local/jre1.8/.

# Bourne Shell (sh):
JAVA_HOME=/usr/local/jre1.8
export JAVA_HOME

# You also need to add the <parent dir>/public_mm/bin directory to your program path:

PATH=<parent dir>/public_mm/bin:$PATH
export PATH

# Run the installation script:
./bin/install.sh

#if prompted for where JRE resides in: use what you set your JAVA_HOME to (i.e. /usr/local/jre1.8)
#if prompted for home path of JRE: type in what is given

# MetaMap requires the use of a SKR/Medpost Part-of-Speech Tagger Server:
./bin/skrmedpostctl start

# to stop the server: 
./bin/skrmedpostctl stop

# YOU ARE READY TO USE METAMAP IN YOUR COMMAND LINE!
# Make sure you are in the right directory with all your cleaned PDFs

metamap -g -+ inputfilename desiredoutputfile #(-g = allow_concept_gaps, -+ = bracketed_output)



