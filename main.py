from profanity_detector import ProfanityDetector

if __name__ == '__main__':
    sentences = ["Hello profanity profity profityprofanity"]
    slurs = ["profanity", "profity"]
    detector = ProfanityDetector(slurs, sentences)
    print(detector.get_scores())