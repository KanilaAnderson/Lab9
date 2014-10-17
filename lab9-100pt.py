############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.


print "have you been sick in the last 24 hoours?"
sick = raw_input()

print "have you vistied west Afica?"
africaAnswer = raw_input()

print "what is your temperature?"
temp = raw_input()

print"if temperature is over 105F"
temp =raw_input()

print"then you will have to go to the hospital"
hospital = raw_input()
