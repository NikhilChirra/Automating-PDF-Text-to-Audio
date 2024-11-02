import pyttsx3, PyPDF2

# Open the PDF file (QWQWQ.PDF)
pdfreader = PyPDF2.PdfReader(open('qwqwq.pdf', 'rb'))
speaker = pyttsx3.init()

# Empty string to hold the entire text
full_text = ''

# Extract text from each page
for page_num in range(len(pdfreader.pages)):
        page = pdfreader.pages[page_num]
        text = page.extract_text()

        # Ensure the page contains text
        if text:  
            clean_text = text.strip().replace('\n', ' ')
            full_text += clean_text + ' '

# Checking if any text was extracted
if full_text:
        # Saving the text to an audio file
        speaker.save_to_file(full_text, 'audio.mp3')
        speaker.runAndWait()
        print("Audio saved as 'audio.mp3'")
else:
        print("Text not found in the PDF.")

speaker.stop()