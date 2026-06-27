# search notes 

import os

def search_notes():
    print("==================================")
    print("STUDYPILOT CLI")
    print("==================================")
    print("\nYou can search your notes here.")

    keyword = input("Enter a keyword to search for: ").lower()

    # List all available note files
    note_files = [f for f in os.listdir('notes') if f.endswith('.txt')]
    
    if not note_files:
        print("No notes available.")
        return

    found = False
    for filename in note_files:
        with open(f"notes/{filename}", 'r') as file:
            content = file.read().lower()
            if keyword in content:
                found = True
                print(f"\nKeyword '{keyword}' found in {filename}:")
                print(content)

    if not found:
        print(f"No notes found containing the keyword '{keyword}'.")