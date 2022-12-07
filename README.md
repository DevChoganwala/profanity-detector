# Profanity Detector

Does a basic profanity check on a file with sentences (may be tweets).

## Assumptions

1. Maximum tweet length is 240 characters.
2. All the words present in the tweet are either concatination of meaningful words or meaningful words themselves.
3. Tweets are provided in `tweets.txt`, racial slurs in `slurs.txt`
4. There are no cases like "h0p3" instead of "hope", if "hope" is a racial slur. 

## Metrics
- `Binary`: This metric can be {0, 1}. It is 1 when a sentence contains profanity, 0 otherwise.
- `simple`: This metric is a float between [0, 1]. It is the ratio of number of tokens containing racial slurs to the number of tokens.
- `charprof`: This metric is a float between [0, 1]. It is the ratio of total number of characters used by racial slurs to the total number of characters all the tokens use in the sentence.

Assuming that the maximum tweet length is 240 chars, a minimum slur of length 3 will give minimum metric in the case of `charprof` which is 0.01

## Pipeline
This is a very basic pipeline (with possible improvements) that gets the task done:
1. Text Normalization - converting all the text to lowercase
2. Tokenization - generation of tokens from the sentences
3. profanity_score generation

## Dependencies
No external dependencies required for the basic task here. No requirements.txt

## Possible improvements
1. Tokenization may be punctuation based, punctuations do not convey any special meaning and may not be considered when calculating profanity score.
2. Emojis can be considered as profanities and may also be tokenized and supported.
3. Tweet may contain arbitrary text (say a single repeated letter) and a single profanity, since this arbitrary text has no meaning, profanity score for this tweet should be high.
4. a single word containing multiple meaningful english words may be seperated.
5. Profanity score can also be higher if the racial slur is closer to the beginning.
6. Profanities may also be hidden, for example if the slur contains 1 instead of i. This should also be detected.