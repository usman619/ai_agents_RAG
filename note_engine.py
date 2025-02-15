from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join('data', 'notes.txt')

def save_note(note):
    # If the input is dict-like, extract title and content.
    if isinstance(note, dict):
        title = note.get("title", "")
        content = note.get("content", "")
        # Combine title and content in a readable format.
        note_text = f"{title}: {content}" if title else content
    else:
        note_text = str(note)
    
    if not os.path.exists(note_file):
        open(note_file, 'w').close()
    
    with open(note_file, 'a') as f:
        f.write(note_text + "\n")
    
    return "Note Saved"

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="This tools can save notes in a file for the user."
)