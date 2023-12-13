# I declare that my work contains no examples of misconduct, such as plagiarism, collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1990840/20222405
# Date: 20.04.2023
import os
progression_outcome = {"[120, 0, 0]": "Progress",
                       "[100, 20, 0]": "Progress (module trailer)",
                       "[100, 0, 20]": "Progress (module trailer)",
                       "[80, 40, 0": "Do not Progress - module retriever",
                       "[80, 20, 20]": "Do not Progress - module retriever",
                       "[80, 0, 40]": "Do not Progress - module retriever",
                       "[60, 60, 0]": "Do not Progress - module retriever",
                       "[60, 40, 20]": "Do not Progress - module retriever",
                       "[60, 20, 40]": "Do not Progress - module retriever",
                       "[60, 0, 60]": "Do not Progress - module retriever",
                       "[40, 80, 0]": "Do not Progress - module retriever",
                       "[40, 60, 20]": "Do not Progress - module retriever",
                       "[40, 40, 40]": "Do not Progress - module retriever",
                       "[40, 20, 60]": "Do not Progress - module retriever",
                       "[40, 0, 80]": "Exclude",
                       "[20, 100, 0]": "Do not Progress - module retriever",
                       "[20, 80, 20]": "Do not Progress - module retriever",
                       "[20, 60, 40]": "Do not Progress - module retriever",
                       "[20, 40, 60]": "Do not Progress - module retriever",
                       "[20, 20, 80]": "Exclude",
                       "[20, 0, 100]": "Exclude",
                       "[0, 120, 0]": "Do not Progress - module retriever",
                       "[0, 100, 20]": "Do not Progress - module retriever",
                       "[0, 80, 40]": "Do not Progress - module retriever",
                       "[0, 60, 60]": "Do not Progress - module retriever",
                       "[0, 40, 80]": "Exclude",
                       "[0, 20, 100]": "Exclude",
                       "[0, 0, 120]": "Exclude"}

#Initialize counters for each outcome category
Progress_count = 0
Trailer_count = 0
Retriever_count = 0
Exclude_count = 0

# clear existing text file
if os.path.exists("Student_Progression_Details.txt"):
    os.remove("Student_Progression_Details.txt")

# creating 'checking' function
def checking(word):
    word_for_describe = word
    while True:
        try:
            word = int(input("Please enter your credits at " + word_for_describe + ": "))
            if word == 0 or word == 20 or word == 40 or word == 60 or word == 80 or word == 100 or word == 120:
                return word
            else:
                print("Out of range")
                print()
                continue
        except ValueError:
            print("Integer required")
            print()


while True:
    word1 = checking("PASS")
    word2 = checking("DEFER")
    word3 = checking("FAIL")       # calling 'checking' function

    Total = word1 + word2 + word3
    if Total != 120:
        print("Total incorrect")     # Check if total is 120
        print()
    else:
        result = progression_outcome[f"[{word1}, {word2}, {word3}]"]
        print(result)
        print("\n")

        # create 'Student_Progression_Details.txt' file and save input data
        details_file = open("Student_Progression_Details.txt", "a")
        details_file.write(result + " - " + str(word1) + ", " + str(word2) + ", " + str(word3) + "\n")     
        details_file.close()

        # caluculate count  based on result
        if result == "Progress":
            Progress_count += 1
        elif result == "Progress (module trailer)":
            Trailer_count += 1
        elif result == "Do not Progress - module retriever":
            Retriever_count += 1
        else:
            Exclude_count += 1

        # Ask if user wants to enter another set of data or quit    
        print("Would like to enter another set of data?")
        while True:
            choice = input("Enter 'y' for yes or 'q' to quit and view results: ")
            if choice.lower() == 'q':     # capital or simple q or y should work
                break
            elif choice.lower() == "y":   # capital or simple q or y should work
                print("\n")
                break
            else:
                print("Try Again")
                print()
                continue
        if choice == "q":
           break
        else:
           continue
        
# Print histogram
print("---------------------------------------------------------------")        
print("Histogram")
print("Progress", Progress_count, "\t"":", "*"*Progress_count)
print("Trailer", Trailer_count, "\t"":", "*"*Trailer_count)
print("Retriever", Retriever_count, "\t"":", "*"*Retriever_count)
print("Exclude", Exclude_count, "\t"":", "*"*Exclude_count)
Total_outcomes = Progress_count + Trailer_count + Retriever_count + Exclude_count
print()
print(Total_outcomes, "Outcome/s in total")
print("---------------------------------------------------------------")
print()

# open 'Student_Progression_Details.txt' file in read mode and print all contents in that file
details_file = open("Student_Progression_Details.txt", "r")        
contents = details_file.read()
print(contents)
details_file.close()
