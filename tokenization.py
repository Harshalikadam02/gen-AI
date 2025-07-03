import re

class CustomTokenizer:
    def __init__(self, language='english'):
        self.language = language
        self.vocab = {}
        self.reverse_vocab = {}
        self.vocab_index = 0

    def tokenize(self, text):
        if self.language == 'english':
            # Basic English tokenizer: words and punctuation
            tokens = re.findall(r"\b\w+\b|[^\w\s]", text.lower())
        elif self.language == 'hindi':
            # Simple Hindi tokenizer: split by whitespace
            tokens = text.strip().split()
        else:
            raise ValueError("Unsupported language")
        return tokens

    def build_vocab(self, text):
        tokens = self.tokenize(text)
        for token in tokens:
            if token not in self.vocab:
                self.vocab[token] = self.vocab_index
                self.reverse_vocab[self.vocab_index] = token
                self.vocab_index += 1

    def encode(self, text):
        self.build_vocab(text)
        tokens = self.tokenize(text)
        return [self.vocab[token] for token in tokens]

    def decode(self, token_ids):
        return ' '.join([self.reverse_vocab[i] for i in token_ids])

if __name__ == "__main__":
    print("----- ENGLISH TEST -----")
    eng_text = "The cat sat on the mat."
    eng_tokenizer = CustomTokenizer(language='english')
    eng_encoded = eng_tokenizer.encode(eng_text)
    print("Tokens:", eng_encoded)
    print("Decoded:", eng_tokenizer.decode(eng_encoded))

    print("\n----- HINDI TEST -----")
    hindi_text = "बिल्ली चटाई पर बैठी थी।"
    hindi_tokenizer = CustomTokenizer(language='hindi')
    hindi_encoded = hindi_tokenizer.encode(hindi_text)
    print("Tokens:", hindi_encoded)
    print("Decoded:", hindi_tokenizer.decode(hindi_encoded))
