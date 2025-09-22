# This section of the code is for creation of a notes management CLI using Click.

from datetime import datetime  # For handling date and time
from pathlib import Path    # File system path manipulations

import click

NOTES_DB = Path.home() / ".notes" / "notes.txt" # Define the path to the notes database file. This is where notes will be stored.

DISPLAY_FMT = "{:<3} {:16} {:16} {:40}" # Format string for displaying notes in a tabular format with fixed-width columns.

def print_header():
    click.echo(DISPLAY_FMT.format("ID", "Created", "Updated", "Contents")) # Print the header row for the notes display.
    click.echo("-"*3 + " " + "-"*16 + " " + "-"*16 + " " + "-"*40) # Print a separator line for clarity.

def print_note(idx, note):
    created, updated, contents = note.split("\t")
    dt_fmt = "%b-%d %I:%M %p" # Date-time format for displaying created and updated timestamps.
    created = datetime.fromisoformat(created).strftime(dt_fmt)
    updated = datetime.fromisoformat(updated).strftime(dt_fmt)
    click.echo(DISPLAY_FMT.format(idx, created, updated, contents)) # Print a single note in the formatted style.


def load_notes():   # Function to load notes from the database file
    notes = []
    with open(NOTES_DB) as fo:
        for line in fo:
            notes.append(line.strip())
    return notes

def save_notes(notes): # Function to save notes to the database file
    with open(NOTES_DB, 'w') as fo:
        for note in notes:
            fo.write(f"{note}\n")

@click.group() # Invoke as a group to hold multiple commands with order of execution
@click.pass_context # Pass the context to the command group, addding data to the context object (called obj) if needed
def main(ctx): # Defining the method name to be wrapped by the Click group
    """Program to manage notes."""
    if not NOTES_DB.parent.exists(): # Check if the parent directory exists. If not, it creates it.
        NOTES_DB.parent.mkdir()
        NOTES_DB.touch() # Create the notes database file if it doesn't exist.

    ctx.ensure_object(dict) # Ensure that the context object is a dictionary.
    ctx.obj["notes"] = load_notes() # Load notes from the database file and store them in the context object.

# Registering the nested commands with the method defined to the Click group above:
@main.command() 
@click.pass_context
def show(ctx):
    """Shows notes in the database."""
    notes = ctx.obj["notes"] # Retrieve the notes from the context object.
    print_header()
    for i, note in enumerate(notes, start=1):
        print_note(i, note)
        
@main.command()
@click.pass_context 
def add(ctx):
    """Adds a note to the database."""
    notes = ctx.obj["notes"]
    created = datetime.now().isoformat()
    contents = click.prompt("Enter note contents") # Prompt the user to enter the note contents.
    notes.append(f"{created}\t{created}\t{contents}") # Append the new note to the list with created and updated timestamps.
    save_notes(notes) # Save the updated list of notes back to the database file.

@main.command()
@click.pass_context
def update(ctx):
    """Updates a note in the database."""
    notes = ctx.obj["notes"]
    print_header()
    for i, note in enumerate(notes, start=1):
        print_note(i, note)
    idx = click.prompt("Enter note ID to update or -1 to exit", type=int) # Prompt the user
    if idx == -1:
        click.echo("Exiting without updating any notes.")
        return
    updated_content = click.prompt("Updated content")
    idx -= 1 # Convert to zero-based index
    updated = datetime.now().isoformat()
    created = notes[idx].split("\t")[0] # Preserve the original created timestamp
    notes[idx] = f"{created}\t{updated}\t{updated_content}" # Update the selected note with new content and updated timestamp.
    save_notes(notes) # Save the updated list of notes back to the database file.

@main.command()
@click.pass_context
def delete(ctx):
    """Deletes a note from the database."""
    notes = ctx.obj["notes"]
    print_header()
    for i, note in enumerate(notes, start=1):
        print_note(i, note)
    idx = click.prompt("Enter note ID to delete or -1 to exit", type=int) # Prompt the user
    if idx == -1:
        click.echo("Exiting without deleting any notes.")
        return
    idx -= 1 # Convert to zero-based index
    notes.remove(notes[idx]) # Remove the selected note from the list.
    save_notes(notes) # Save the updated list of notes back to the database file.
