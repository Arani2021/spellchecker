from spellchecker import SpellChecker

# Creating the app class
class SpellcheckerApp:
    def __init__(self):
        self.spell = SpellChecker()  # Corrected class name
    def correct_text(self, text):
        words = text.split()  # Split the input text into words
        corrected_words = []
        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)
        # Returning the corrected text
        return ' '.join(corrected_words)

    # Running the app
    def run(self):
        print("\n---Spell Checker---")
        while True:
            text = input('Enter text to check (or type "exit" to quit): ')
            if text.lower() == 'exit':
                print('Closing the program...')
                break
            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')

# Running the main program
if __name__ == "__main__":
    SpellcheckerApp().run()

