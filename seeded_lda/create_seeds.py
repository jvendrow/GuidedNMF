import csv

baseball_words = ["pitch", "baseball", "team", "ball", "game", "season", "base", "field", "runs"]
medical_words = ["medical", "disease", "doctor", "health", "patient", "medicine", "clinic", "diet", "tests"]
space_words = ["space", "lunar", "nasa", "launch", "rocket", "moon", "shuttle", "orbit", "solar"]


for i in range(len(baseball_words)):
    with open('seeds' + str(i+1) + '.txt', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(baseball_words[0:(i+1)])
        spamwriter.writerow(medical_words[0:(i+1)])
        spamwriter.writerow(space_words[0:(i+1)])
