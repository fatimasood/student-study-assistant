# upload notes 

def upload_notes():
    print("==================================")
    print("STUDYPILOT CLI")
    print("==================================")
    print("\nYou can upload your notes here.")

    subject = input("Enter the subject of the notes: ")

    # Create a file
    filename = f"{subject}.txt"
    print(f"Notes uploaded successfully as {filename}")

    # write the notes to a file
    with open(filename, 'a') as file:
        file.write(f"Subject: {subject}\n")
        file.write("Notes:\n")
        while True:
            note = input("Enter a note (or type 'done' to finish): ")
            if note.lower() == 'done':
                break
            file.write(f"- {note}\n")

    print(f"Notes for {subject} have been saved successfully.")
  
