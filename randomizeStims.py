
#################################################################

######################
###  Description
######################

# BCD Lab 2015, Jim Calabro
# For assistance email jcalabro@umass.edu

# Program designed to generate a pseudo-randomly ordered
# excel sheet of stimuli

# SPECIFICATIONS:
#   Objects:
#      -No two "species" should be paired together
#      -Don't want colors to be the same
#      -Once pairing has happened, it shouldn't happen again
#   Faces:
#      -One trained, one untrained
#      -Don't have consecutive faces of the same race
#      -Have each race look in each direction
#      -Don't look consecutively in the same direction more than once

#################################################################

######################
###  Configuration
######################

# import statements
from openpyxl import load_workbook

# where to read and write the excel files
read_location = 'C:/Users/Jim/Code/LOTR/'
write_location = read_location

# name of the workbook to be read
bird_workbook_name = 'ObjectsUsed_bird_color.xlsx'

# the number of birds in 
number_of_birds = 24

#################################################################

######################
###  Execution
######################

bird_workbook = load_workbook('{0}{1}'.format(read_location, bird_workbook_name))

bird_worksheet = workbook.active

bird_list = []


