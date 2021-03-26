# importing csv library to use its features to make csv file
import csv

# basic function for writing in to csv file
def writing_data_into_csv(info_list):
    with open('Student_informations.csv', 'a', newline='') as csv_file:

        write = csv.writer(csv_file)
        obj = []
        
        # this if condition is for if our csv file is empty or its not existing then it writes this row
        # for creating our data very clear which data belongs to which
        if csv_file.tell() == 0:
            # inserting first row as header of data
            write.writerow(["Sr. No", "Name", "Surname", "Age", "Stream", "Contact_Number"])

        write.writerow(info_list)


if __name__ == '__main__':

    condition = True
    Student_num = 1

    while(condition):
        # Taking inputs from user for data
        Name = input("Enter student name : ")
        Surname = input("Enter student surname : ")
        Age = input("Enter student age : ")
        Stream = input("Enter student stream which student is studing : ")
        Contact_number = input("Enter student contact_number : ")
        
        student_info_list = []
        student_list = [Student_num, Name, Surname, Age, Stream, Contact_number]
        student_info_list.append(student_list)
    
        check = input("\nAre these inserted informations correct ? [ yes / no ] --> ")

        if check == "yes":
            # function call if all data are correct n writing in csv file
            writing_data_into_csv(student_list)

            choice = input("\nDo you want to insert another information for student ? [ yes / no ] --> ")

            if choice == "yes":
                condition = True
                Student_num = Student_num + 1
            elif choice == "no":
                print("\nYour data enetered successfully...")
                condition = False
        
        elif check == "no":
            print("\nRe-enter values very carefully !!!!")


