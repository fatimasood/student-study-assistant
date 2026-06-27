# view notes - show all notes then user select any one of them then show the content of that note(open it)

import os

def view_notes():
    print("==================================")
    print("STUDYPILOT CLI")
    print("==================================")
    print("\nYour all saved notes here.")

    # List all available note files

    note_files = [f for f in os.listdir('notes') if f.endswith('.txt')]
    
    if not note_files:
        print("No notes available.")
        return

    print("\nAvailable notes:")
    for i, filename in enumerate(note_files, start=1):
        print(f"{i}. {filename}")

    # select notes
    try:
        choice = int(input("\nEnter the number of the note you want to view: "))
        if 1 <= choice <= len(note_files):
            selected_file = note_files[choice - 1]
            with open(f"notes/{selected_file}", 'r') as file:
                print(f"\nContent of {selected_file}:")
                print(file.read())
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")