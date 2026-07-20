class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1: str, text2: str = None):
        if not text2 is None:
            return text1 + text2
        return text1.upper()
        

    # def format_text(self, text1: str, ):
        



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
