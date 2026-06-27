
def show_menu():

    print("You can select an option according to your need:")
    print("1: Upload Notes")
    print("2: View Notes")
    print("3: Search Notes")
   # print("4: Save Answers")
   # print("5: View Saved Answers")
    print("4: Exit")

def main():
    print("==============================")
    print("WELCOME TO THE STUDYPILOT CLI")
    print("==============================")

    show_menu()

    choice = input("Enter your choice (1-4): ")

    while choice != '4':
        if choice == '1':
            upload_notes()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
       # elif choice == '4':
       #     save_answers()
       # elif choice == '5':
        #    view_saved_answers()
        elif choice == '4':
            print("Thank you for using StudyPilot CLI. Goodbye!")

        else:
            print("Invalid choice. Please choose carefully.")


        show_menu()
        choice = input("Enter your choice (1-4): ")


if __name__ == "__main__":
    main()