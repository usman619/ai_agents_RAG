# AI Agents RAG
Creating a basic AI Agents using Gemini API or locally downloaded LLMs using Ollama to extract information using available dataset and PDF file. The following are the steps to run this repo:
- Create the python virtual environment using the following commands:
    ```bash
    python -m venv env
    source env/bin/activate
    ```
- Install the required packages using the requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```

## Example Outputs:
- Input: What is the population of Pakistan?
```bash
    ❯ python main.py
    > Pandas Instructions:
    ```python
    df[df['Country'] == 'Pakistan']['Population2023'].iloc[0]
    ```
    > Pandas Output: 240485658
```
- Input: Save a note saying "I love coding in Python"
```bash
    ❯ python main.py
    Enter a prompt (q to quite): Save a note saying "I love coding in Python"
    > Running step 687679b4-d0ca-4a21-a61b-f4c8c5e99ad3. Step input: Save a note saying "I love coding in Python"
    Thought: The current language of the user is: English. I need to use the note_saver tool to save the note.
    Action: note_saver
    Action Input: {'note': AttributedDict([('title', 'Coding Note'), ('content', 'I love coding in Python')])}
    Observation: Note Saved
    > Running step f5e96726-60cc-48f9-a21f-d8f40a0f818f. Step input: None
    Thought: I can answer without using any more tools. I'll use the user's language to answer
    Answer: Note saved successfully.
    Save a note saying "I love coding in Python"
```