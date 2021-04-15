from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def check_spelling():
    input = request.form.get("input")
    each_word = input.split(" ")
    misspelled_words = []
    
    with open("dictionary.txt") as file:
        dictionary = [line.strip() for line in file]
        file.close()
    
    for word in each_word:
        formatted_word = remove_punctuation(word)
        if formatted_word.lower() not in dictionary:
            misspelled_words.append(word)

    print(str(misspelled_words))
    
    return render_template("results.html", misspelled_words = misspelled_words)
    

#function that removes non alpha characters from beginning or end of word, or both
def remove_punctuation(text):
    #extra spaces are treated as a word, so change to a valid word to avoid error!
    if text == "":
        return "a"

    first_char = text[0]
    last_char = text[-1]

    if not alpha_character(ord(first_char)):
        text = text.replace(first_char, "")
    if not alpha_character(ord(last_char)):
        text =  text.replace(last_char, "") 
    return text
        
def alpha_character(character):
    if ((character >= 65 and character <= 90) or (character >= 97 and character <= 122)):
        return True


""" if __name__ == "__main__":
    print(check_spelling("I am a.............           gorilla!")) """