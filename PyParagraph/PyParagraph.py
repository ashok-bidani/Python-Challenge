# Incorporate regular expressions module (for splitting by punctuation)
import re

# Define the file to load and the file to output
file_to_load = 'data/MLK_I_Have_a_Dream.txt'
file_to_output = 'output/paragraph_analysis.txt'

# Create a paragraph variable to store the paragraph contents as a string (with no new lines)
paragraph = ""

with open(file_to_load) as txt_data:
    paragraph = txt_data.read().replace("\n", " ")

# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
word_count = len(word_split)

# Create a list of the letter counts of each word
letter_counts = []

for word in word_split:
    letter_counts.append(len(word))

# Calculate the avg letter count, based on this
avg_letter_count = sum(letter_counts)/float(len(letter_counts))

# Now, re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)
sentence_count = len(sentence_split)

# Create a list of the word counts of each sentence
words_per_sentence = []

for sentence in sentence_split:
    words_per_sentence.append(len(sentence.split(" ")))

# Calculate the avg word count (per sentence), based on this
avg_sentence_len = sum(words_per_sentence)/float(len(words_per_sentence))

# Generate Paragraph Analysis Output
output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence_len}\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)