from profanity_detector import ProfanityDetector

if __name__ == '__main__':

    #tweets.txt contains tweets seperated by newlines
    with open("tweets.txt", "r", encoding='UTF-8') as tweet_file:
        sentences = tweet_file.read().splitlines()
    
    #slurs.txt contains slurs seperated by newlines
    with open("slurs.txt", "r", encoding='UTF-8') as slurs_file:
        slurs = slurs_file.read().splitlines()
    
    detector = ProfanityDetector(slurs, sentences, 'binary')
    print(detector.get_scores())