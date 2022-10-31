import spacy
import listen

# nlp = spacy.load("de_core_news_sm")
nlp = spacy.load("de_core_news_lg")

token5 = nlp("scheiß")
token6 = nlp("ja")
print(token6.similarity(token5))



def checkSimilarity(token1):
    for word in listen.profane_words:
        wordtoken = nlp(word)
        if wordtoken.similarity(token1) > 0.8:
            return True
    # for word in listen.offensive_words:
    #     wordtoken = nlp(word)
    #     if wordtoken.similarity(token1) > 0.6:
    #         return True
    return False


# doc = nlp("pener")[0]
# doc1 = nlp("penner")[0]
# print(doc.similarity(doc1))

textin = open('germeval2018.training500.txt', 'r', encoding='utf-8')
lines = textin.readlines()
textin.close()
hate_speech = []  # 1688
not_hate_speech = []
counterall = 0

for line in lines:
    line = line.lower()
    doc = nlp(line)
    if "other" in line:
        counterall = counterall + 1
    for token in doc:
        if checkSimilarity(token):
            if line not in hate_speech:
                hate_speech.append(line)
                break
        # elif line not in not_hate_speech:
        #     not_hate_speech.append(line)

counter = 0

for line in hate_speech:
    if "other" in line:
        counter = counter + 1

print("All Posts: " + str(len(lines)))
print("All Other: " + str(counterall))
print("Other in Hate Speech: " + str(counter))
print("Count Hate Speech: " + str(len(hate_speech)))
print("Percentage: " + str(counter/len(hate_speech)))
