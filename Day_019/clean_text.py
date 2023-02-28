import re
from stop_words import stop_words

 # Let's deffine a function to clean texts
    # It normalizes case, removes unicode characters and stop words
def clean_text(text):
        # normalizing case
        case_normal = text.lower()
        # removing unicode characters
        unicode_removed = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", case_normal)
        # removing stopwords
        stop = stop_words
        stop_words_removed = " ".join([word for word in unicode_removed.split() if word not in (stop)])
        return stop_words_removed