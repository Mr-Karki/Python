#########################################
# PYTHON FOR AI: LESSON 1 - FUNDAMENTALS
#########################################

# Section 1: Basic Data Types for AI

print ("SECTION 1: BASIC DATA TYPES FOR AI") 
print("------------------------------------")

# 1.1 Numbers - for measurements, counts, predictions

temperature = 98.6  #floating-point numbers
patient_count = 5000   #integer

print ("Temperature:", temperature, "Type:", type(temperature))
print("Patient count:", patient_count, "Type:", type(patient_count))

# section for string
print ("\nSECTION 1.1:Strings") 
print("------------------------------------")
# Text for language processing

paitent_name = "Arun Bhomi"
medical_notes = "Reports of being a bitch" 

print ("\nPatient name:", paitent_name, "Type:", type(paitent_name))
print("\nMedical notes:", medical_notes, "Type:", type(medical_notes))

# section for list

temperatures = [98.6, 99, 97, 96.8, 99.9]
paitent_names = ["Ram", "Shyam", "Hari", "Om"]

print ("Temperatures", temperatures, "Type:", type(temperatures))
print ("\nFirst Temperature: ", temperatures [0])

print ("Paitent names:", paitent_names, "Type:", type(paitent_names))
print ("Number of Patients:", len(paitent_names))
