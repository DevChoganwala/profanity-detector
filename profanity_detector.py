"""Contains ProfanityDetector class to detect profanity in a string or a list of strings."""


class ProfanityDetector:
    """
    Detects profanity in a string or a list of strings.

    Attributes:
        tokens: list of str
            A list of words considered to be racial slurs.
        sentences: list of str, optional
            A list of sentences to be checked for profanity.
        metric: str
            An evaluation metric for degree of profanity.
                simple: Ratio of number of tokens containing racial slurs to all the tokens in the sentence.
                charprof: Ratio of Number of total characters used by racial slurs to total number of characters total number of characters all the tokens used in the sentence.
                binary (Default): Returns 1 if there is profanity in the sentence otherwise 0.
    """

    def __init__(self, tokens, sentences=None, metric='binary'):
        self.sentences = sentences
        self.tokens = tokens
        self.metric = metric

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
        # Cast every token to lowercase
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
        # splitting about whitespaces
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
        if self.metric == 'simple':
            # if any slur is found in a sentence_token match_count is incremented by 1
            for sentence_token in sentence_tokens:
                match_count += any(token in sentence_token for token in self.tokens)
        elif self.metric == 'charprof':
            for token in self.tokens:
                for sentence_token in sentence_tokens:
                    if token in sentence_token:
                        match_count += len(token)
        elif self.metric == 'binary':
            for sentence_token in sentence_tokens:
                if any(token in sentence_token for token in self.tokens):
                    match_count = 1
                    break
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
        if self.metric == 'simple':
            return round(match_count/len(sentence_tokens), 2)
        elif self.metric == 'charprof':
            return round(match_count/sum(len(token) for token in sentence_tokens), 2)
        elif self.metric == 'binary':
            return match_count

    def get_scores(self):
        """
        Get profanity scores for all the sentences in a list (only valid with sentences is set during initialization).

        Returns
            scores: list of float
                A list of profanity scores corresponding to each sentences.
        """
        if self.sentences is None:
            raise Exception('''Cannot call get_scores if the object is not initialized
            with a list of sentences\n
            Try calling profanity_score(sentence)''')
        scores = [self.profanity_score(sentence)
                  for sentence in self.sentences]
        return scores
