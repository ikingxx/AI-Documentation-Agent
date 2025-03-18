# src/summarize.py
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


import nltk
nltk.data.path.append("C:/Users/hp.DESKTOP-0U7M644/anaconda3/envs/doc-agent/nltk_data")
nltk.download('punkt', download_dir='C:/Users/hp.DESKTOP-0U7M644/anaconda3/envs/doc-agent/nltk_data')


def summarize_text(text, sentences_count=10):
    """
    Summarize the input text using LexRank algorithm.

    :param text: The text to summarize.
    :param sentences_count: Number of sentences in the summary.
    :return: A string summary of the input text.
    """
    try:
        # Create a parser from the raw text
        parser = PlaintextParser.from_string(text, Tokenizer("english"))

        # Initialize LexRank summarizer
        summarizer = LexRankSummarizer()

        # Generate the summary (list of sentence objects)
        summary_sentences = summarizer(parser.document, sentences_count)

        # Combine sentences into a single string
        summary = ' '.join([str(sentence) for sentence in summary_sentences])

        return summary
    
    except Exception as e:
        print(f"An error occurred during summarization: {e}")
        return None
