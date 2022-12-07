"""Contains ProfanityDetector class to detect profanity in a string or a list of strings."""

class ProfanityDetector:
    """
    Detects profanity in a string or a list of strings.

    Attributes:
        tokens: list of str
            A list of words considered to be racial slurs.
        sentences: list of str, optional
            A list of sentences to be checked for profanity.
    """

    def __init__(self, tokens, sentences=None):
        self.sentences = sentences
        self.tokens = tokens

    def normalize(self, sentence):
        """
        Normalizes a string to lower case.

        Parameters:
            sentence: str
                A string to normalize.
        
        Returns:
            sentence: str
                The normalized string.
        """
        sentence = sentence.lower()
        #Cast every token to lowercase
        self.tokens = [token.lower() for token in self.tokens]
        return sentence
    
    def tokenize(self, sentence):
        """
        Tokenizes a string. Uses whitespace as default seperator.

        Parameters:
            sentence: str
                A string to tokenize.

        Returns:
            sentence: str
                The tokenized string.
        """
        #splitting about whitespaces
        sentence_tokens = sentence.split()
        return sentence_tokens

    def match_tokens(self, sentence_tokens):
        """
        Matches the racial slur tokens with the tokens of the string.

        Parameters:
            sentence_tokens: list of str
                List of tokens to be compared with the racial slur words.

        Returns:
            match_count: int
                The number of tokens containing racial slurs.
        """
        match_count = 0
        #if any slur is found in a sentence_token match_count is incremented by 1
        for sentence_token in sentence_tokens:
            match_count += any(token in sentence_token for token in self.tokens)
        return match_count

    def profanity_score(self, sentence):
        """
        Outputs the profanity score of a sentence.

        Parameters:
            sentence: str
                sentence to be checked for profanity.
        
        Returns:
            profanity_score: float
                A float rounded to 2 decimal places denoting the profanity score.
        """
        sentence = self.normalize(sentence)
        sentence_tokens = self.tokenize(sentence)
        match_count = self.match_tokens(sentence_tokens)
        return round(match_count/len(sentence_tokens), 2)

    def get_scores(self):
        """
        Get profanity scores for all the sentences in a list (only valid with sentences is set during initialization).

        Returns
            scores: list of float
                A list of profanity scores corresponding to each sentences.
        """
        if self.sentences is None:
            raise Exception('''Cannot call get_scores if the object is not initialized with a list of sentences\n
            Try calling profanity_score(sentence)''')
        scores = [self.profanity_score(sentence) for sentence in self.sentences]
        return scores