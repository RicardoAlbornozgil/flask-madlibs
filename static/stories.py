"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code 
        self.title = title 
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

# Stories


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

story3 = Story(
    "location",
    "A Day at the ...",
    ["name", "location" ,"adjective", "noun"],
    """Once upon a time, {name} decided to spend a day at the {location}. Little did they know, they would encounter a {adjective} {noun} that would change their day forever."""
)

story4 = Story(
    "animal_quest",
    "The Mysterious ... Quest",
    ["name", "adjective", "noun1", "color", "noun2"],
    """Join {name} on an exciting quest to find the legendary {adjective} {noun1}. Along the way, they'll meet a {color} {noun2} who offers unexpected help."""
)

story5 = Story(
    "lost_city",
    "Lost in ...",
    ["name", "setting", "adjective", "item", "occupation", "hobby"],
    """{Name} found themselves lost in the bustling city of {setting}. With only a {adjective} {item} and a map, they embarked on a journey filled with surprises, meeting quirky characters like a {occupation} with a penchant for {hobby}."""
)

story6 = Story(
    "magical_object",
    "The Magical ...",
    ["name", "object", "number"],
    """Once upon a time, {name} stumbled upon a mysterious {object} that granted them {number} wishes. However, each wish led to a hilarious and unexpected consequence, leaving {name} in fits of laughter."""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3, story4, story5, story6]}
