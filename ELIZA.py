import random
import re

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "i do not" : "you do not",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

psychobabble = [
    (
        r'.* ?(I feel) (.*)',
        [
            "Why do {} {}?", # the groups in the regex above will be reflected, then inserted in place of {} here;
                             # if there are no {}, just the string will be returned
            "Why do you think {} {}?",
            "Where do yo think those feelings are coming from?"
        ]
    ),
    (
        r'(.*)?name(.*)?',
        [
            "I am not interested in names",
        ],

    ),
    (
        r'.*?(bad)(.*)',
        [
            "What was happened?"
        ]
    ),
    (
        r'.*?(I do not know)(.*)',
        [
            "Are you sure that {}?",
            # "Please, {} should think more deeply about it"
        ]
    ),
    (
        r'.*?(I\'ve a problem)(.*)',
        [
            "Describe more about this problem",
            "Do {} related to your {1}?"
        ]

    ),
    (
        r'.*?(I like) (.*)',
        [
            "Really, do {0} {1}",
            "Tell me more about {1}"
        ]

    ),
    (
        r'.*?(I do not like) (.*)',
        [
            "Do ypu embarrass about {1}?",
            "Why {0} {1}"
        ]

    ),
    (
        r'.*?(I hate) (.*)',
        [
            "Why do {0} {1}",
            "What exactly embarrass you about {1}"
        ]

    ),
    (
        r'(.*)?I remember (.*)?',
        [
            "Do you often think of {1}?",
            "Does thinking of {1} bring anything else to mind?",
            "What else do you remember?",
            "Why do you recall {1} right now?",
            "What in the present situation reminds you of {1}?",
            "What is the connection between me and {1}?",
        ]

    ),
    (
        r'(.*)?I wanted (.*)?',
        [
            "When did you want {1} last time?",
            "What is changed now? Do you still want {1}?"
        ]
    ),
    (
        r'(.*)?good question(.*)?',
        [
            "I know!",
            "Sure, it is the reason why I asked you"
        ]
    ),
    (
      r'(.*)? always(.*)?',
      [
          "Could you please provide an example about {1}",
          "How often exactly? Really, always?"
      ]
    ),
    (
        r'(.*)? childhood(.*)?',
        [
            "Does it have relationship to your parents?",
            "Tem me more about your childhood"
        ]

    ),
    (
        r'(.*)? sorry(.*)?',
        [
            "What feelings do you have when you apologize?",
            "Are you feeling that you guilty?",
            "You should't apologize"
        ]

    ),
    (
        r'(.*)? same(.*)?',
        [
            "Are you sure?",
            "What other connections do you see?"
        ]
    ),
    (
        r'(.*)? mother(.*)?',
        [
            "What is the relationship do you have with your mother?",
            "Is she a friend or enemy for you?",
            "Do you want to change relationship with your mom?"
        ]
    ),
    (
        r'(.*)? depression(.*)?',
        [
            "Tell me what do you remember in your childhood? It's important to understand the root of your problem",
            "How often do you have feeling like this?",
            "What is the reason caused this feeling?"
        ]

    ),

    (
        r'(.*)? school(.*)?',
        [
            "Tem me about your school friends",
            "How do you feel yourself at that time?"
        ]

    ),

    (
        r'(.*)?I have (.*)?',
        [
            "So, you have {1}. What do you feel about that ?",
        ]

    ),

    (
        r'(.*)?maybe(.*)?',
        [
            "Why are you uncertain?",
            "What is stopping you?"
        ]
    ),
    (
        r'(.*)? girlfriend(.*)?',
        [
            "Do you like her?",
            "What is the relationship do you have?"
        ]
    ),
    (
        r'(.*)? boyfriend(.*)?',
        [
            "Do you like him?",
            "What is the relationship do you have?"
        ]
    ),

    (
        r'(.*)? parents(.*)?',
        [
            "Tell me more about your parents?",
            "What do  you remember in your childhood related to your parents?"
        ]
    ),

    (
        r'.*?(yes)(.*)',
        [
            "Ok",
            "Please, go on",
            "Continue",
            "It's fine"
        ]
    ),
    (
        r'.*?(no)(.*)',
        [
            "What exactly do you mean?",
            "Why?"
        ]
    ),
    (
        r'quit',
        [
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150. Have a good day!"
        ]
    )
]


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])

    return "That is interesting. Please go on."


def main():
    print("Hello. How are you feeling today?")

    while True:
        statement = input("YOU: ")
        print("ELIZA: " + analyze(statement))

        if statement == "quit":
            break


if __name__ == "__main__":
    main()
