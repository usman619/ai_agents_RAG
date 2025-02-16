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

- Input: What is the current population of Pakistan?
```bash
    Enter a prompt (q to quite): What is the current population of Pakistan?
    > Running step 36e1d99c-c7f1-4eb9-89b5-d2859ec4703c. Step input: What is the current population of Pakistan?
    Thought: The current language of the user is: English. I need to use the `pakistan_data` tool to get the current population of Pakistan.
    Action: pakistan_data
    Action Input: {'input': 'What is the current population of Pakistan?'}
    Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.24it/s]
    Observation: According to the final results of the 2023 Census, Pakistan's population is 241,495,112.  This includes the four provinces, as well as Islamabad Capital Territory.  Census data for Azad Jammu and Kashmir and Gilgit-Baltistan is still pending approval.

    > Running step 95237206-846a-4fd3-b472-2bd151abb1f9. Step input: None
    Thought: I can answer without using any more tools. I'll use the user's language to answer
    Answer: The current population of Pakistan, according to the final results of the 2023 Census, is 241,495,112.  This includes the four provinces and Islamabad Capital Territory.  Data for Azad Jammu and Kashmir and Gilgit-Baltistan is still pending approval.
```

- Input:  What is the role of Islam in Pakistan?
```bash
    Enter a prompt (q to quite): What is the role of Islam in Pakistan?
    > Running step e73d4337-61d3-4f0e-b586-00f5ea842321. Step input: What is the role of Islam in Pakistan?
    Thought: The current language of the user is: English. I need to use a tool to help me answer the question about the role of Islam in Pakistan.
    Action: pakistan_data
    Action Input: {'input': 'What is the role of Islam in Pakistan?'}
    Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.96it/s]
    Observation: In the West wing of the country in 1969, a significantly larger percentage of educated professionals identified with an Islamic identity compared to a secular one.  Conversely, in the East wing,  a greater number identified with their ethnicity rather than Islam.  The 1973 constitution established institutions to guide the application and interpretation of Islam, including the Council of Islamic Ideology and the Shariat Court.  The Shariat courts were added to the constitution later, in 1979.

    > Running step 7f8e66b4-b8f3-4f25-b6d4-6b80745b7707. Step input: None
    Thought: I can answer without using any more tools. I'll use the user's language to answer.
    Answer: Islam plays a significant role in Pakistan.  While the balance between religious and secular identities varied regionally even in the past (with a stronger Islamic identification among educated professionals in the West wing compared to the East wing in 1969), the 1973 constitution formalized the role of Islam by establishing institutions like the Council of Islamic Ideology and the Shariat Court (added in 1979) to guide its interpretation and application within the country.  This indicates a constitutional and institutional framework designed to integrate Islamic principles into Pakistani law and governance.
```

- Input: What are the Administrative units of Pakistan?
```bash
    Enter a prompt (q to quite): What are the Administrative units of Pakistan?
    > Running step 0fe07854-97d7-488c-b3e5-f4e3f2900976. Step input: What are the Administrative units of Pakistan?
    Thought: The current language of the user is: English. I need to use a tool to get information about the administrative units of Pakistan.
    Action: pakistan_data
    Action Input: {'input': 'What are the administrative units of Pakistan?'}
    Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.46it/s]
    Observation: The provided text mentions Pakistan's four provinces: Punjab, Sindh, KPK, and Balochistan, as well as Islamabad Capital Territory.  It also notes that census data for Azad Jammu and Kashmir (AJK) and Gilgit-Baltistan is pending approval.

    > Running step fe10249a-fb35-451d-b850-9acb3d289c7d. Step input: None
    Thought: I can answer without using any more tools. I'll use the user's language to answer
    Answer: Pakistan's administrative units consist of four provinces: Punjab, Sindh, Khyber Pakhtunkhwa (KPK), and Balochistan.  Additionally, Islamabad Capital Territory serves as the federal capital.  The status of Azad Jammu and Kashmir (AJK) and Gilgit-Baltistan is currently pending official census approval.
```

- Input: What are the Administrative Units of Pakistan and Please save a note of it.
```bash
    Enter a prompt (q to quite): What are the Administrative Units of Pakistan and Please save a note of it.
    > Running step b7883d5a-7e82-461e-aa38-a917816a0520. Step input: What are the Administrative Units of Pakistan and Please save a note of it.
    Thought: The current language of the user is: English. I need to use `pakistan_data` to get information about the administrative units of Pakistan, and then `note_saver` to save a note of it.
    Action: pakistan_data
    Action Input: {'input': 'What are the administrative units of Pakistan?'}
    Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.45it/s]
    Observation: The provided text mentions Pakistan's four provinces: Punjab, Sindh, KPK, and Balochistan, as well as Islamabad Capital Territory.  It also notes that census data for Azad Jammu and Kashmir (AJK) and Gilgit-Baltistan is pending approval.

    > Running step f2c099ab-1d77-4acc-9263-db08cf969494. Step input: None
    Thought: I have the information about Pakistan's administrative units. Now I will use the `note_saver` tool to save a note.
    Action: note_saver
    Action Input: {'note': AttributedDict([('title', "Pakistan's Administrative Units"), ('content', "Pakistan's administrative units include four provinces: Punjab, Sindh, Khyber Pakhtunkhwa (KPK), and Balochistan; Islamabad Capital Territory; and the territories of Azad Jammu and Kashmir (AJK) and Gilgit-Baltistan (census data pending approval).")])}
    Observation: Note Saved
    > Running step e7e581df-e6b1-4108-b9e1-19534e8038a5. Step input: None
    Thought: I can answer without using any more tools. I'll use the user's language to answer
    Answer: Pakistan's administrative units are four provinces: Punjab, Sindh, Khyber Pakhtunkhwa (KPK), and Balochistan; Islamabad Capital Territory; and the territories of Azad Jammu and Kashmir (AJK) and Gilgit-Baltistan (census data pending approval).  A note of this information has been saved.
```