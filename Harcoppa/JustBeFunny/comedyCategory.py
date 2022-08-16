categories = ['Alternative Comedy', 'Anecdotal Comedy', 'Anti-Humor', 'Dark Comedy', 'Blue Comedy', 'Character Comedy',
              'Cringe Comedy',
              'Deadpan Comedy', 'Heritage Comedy', 'Improvisational Comedy', 'Insult Comedy', 'Musical Comedy',
              'Observational Comedy', 'One-liners', 'Physical Comedy', 'Prop Comedy', 'Shock Humor', 'Sketch Comedy',
              'Spoof',
              'Surreal Comedy', 'Topical Comedy / Satire', 'Wit / Wordplay']


def display_categories():
    for category in categories:
        print("\t*%s\n" % category)


def category_description(round_category):
    if round_category == 'Alternative Comedy':
        description = "Differs from traditional punchline jokes which features many other forms of comedy " \
                      "such as observation, satire, surrealism, slapstick and improvisation. In its content, " \
                      "Alternative Comedy emerged as a counter to the establishment entertainment figures " \
                      "from the previous generation: It was often cited for its disregard to established " \
                      "comedic movements and ranged from the surreal to slapstick, usually with a " \
                      "combination of both.\n "

    elif round_category == 'Anecdotal Comedy':
        description = "Named after the word anecdote (which stems from the Greek term meaning " \
                      "“unpublished”); refers to comic personal stories that may be true or partly true but " \
                      "embellished.\n "

    elif round_category == 'Anti-Humor':
        description = "A type of indirect humor that involves the joke-teller delivering something which is " \
                      "intentionally not funny, or lacking in intrinsic meaning.\n "

    elif round_category == 'Dark Comedy':
        description = "Deals with disturbing subjects such as death, drugs, terrorism, rape, and war; can " \
                      "sometimes be related to the horror movie genre.\n "

    elif round_category == 'Blue Comedy':
        description = "Typically sexual in nature (risqué) and/or using profane language; sometimes using " \
                      "gender or race based humor.\n "

    elif round_category == 'Character Comedy':
        description = "Derives humor from a persona invented by a performer; often from stereotypes.\n"

    elif round_category == 'Cringe Comedy':
        description = "A comedy of embarrassment, in which the humor comes from inappropriate actions or " \
                      "words; usually popular in television shows and film, but occasionally in stand-up as " \
                      "well.\n "

    elif round_category == 'Deadpan Comedy':
        description = "Not strictly a style of comedy, it is telling jokes without a change in facial " \
                      "expression or change of emotion.\n "

    elif round_category == 'Heritage Comedy':
        description = "A method or genre in which a comedian discus humorous traits or stereotypes about " \
                      "their own culture or heritage.\n "

    elif round_category == 'Improvisational Comedy':
        description = "Improv is when the plot, characters and dialogue of a game, scene or story are made " \
                      "up in the moment. Make sure you don't use old material for this one. \n "

    elif round_category == 'Insult Comedy':
        description = "A form which consists mainly of offensive insults directed at the performer's " \
                      "audience and/or other performers. \n "

    elif round_category == 'Musical Comedy':
        description = "A form of alternative comedy where humor is mostly derived from music with (or " \
                      "sometimes without) lyrics.\n "

    elif round_category == 'Observational Comedy':
        description = "Pokes fun at everyday life, often by inflating the importance of trivial things or by " \
                      "observing the silliness of something that society accepts as normal.\n "

    elif round_category == 'One-liners':
        description = "A joke that is delivered in a single line. A good one-liner is said to be pithy - " \
                      "concise and meaningful.\n "

    elif round_category == 'Physical Comedy':
        description = "Somewhat similar to slapstick, this form uses physical movement and gestures; often " \
                      "influenced by clowning.\n "

    elif round_category == 'Prop Comedy':
        description = "Relies on ridiculous props, casual jackets or everyday objects used in humorous ways.\n"

    elif round_category == 'Shock Humor':
        description = "A style of comedy that uses Shock value to invoke a strong negative emotion as well " \
                      "as a comedic.\n "

    elif round_category == 'Sketch Comedy':
        description = "A shorter version of a sitcom, practised and typically performed live.\n"

    elif round_category == 'Spoof':
        description = "The recreating of a book, film or play for humor; it can be used to make fun of, " \
                      "or ridicule, a certain production.\n "

    elif round_category == 'Surreal Comedy':
        description = "A form of humor based on bizarre juxtapositions, absurd situations, and nonsense " \
                      "logic.\n "

    elif round_category == 'Topical Comedy / Satire':
        description = "Relies on headlining/important news and current affairs; it dates quickly, but is a " \
                      "popular form for late night talk-variety shows.\n "

    elif round_category == 'Wit / Wordplay':
        description = "More intellectual forms based on clever, often subtle manipulation of language (" \
                      "though puns can be crude and farcical).\n "
    print(description)


def category_example(round_category):
    if round_category == 'Alternative Comedy':
        example = "Differs from traditional punchline jokes which features many other forms of comedy " \
                  "such as observation, satire, surrealism, slapstick and improvisation. In its content, " \
                  "Alternative Comedy emerged as a counter to the establishment entertainment figures " \
                  "from the previous generation: It was often cited for its disregard to established " \
                  "comedic movements and ranged from the surreal to slapstick, usually with a " \
                  "combination of both.\n "

    elif round_category == 'Anecdotal Comedy':
        example = "Named after the word anecdote (which stems from the Greek term meaning " \
                  "“unpublished”); refers to comic personal stories that may be true or partly true but " \
                  "embellished.\n "

    elif round_category == 'Anti-Humor':
        example = "A type of indirect humor that involves the joke-teller delivering something which is " \
                  "intentionally not funny, or lacking in intrinsic meaning.\n "

    elif round_category == 'Dark Comedy':
        example = "Deals with disturbing subjects such as death, drugs, terrorism, rape, and war; can " \
                  "sometimes be related to the horror movie genre.\n "

    elif round_category == 'Blue Comedy':
        example = "Typically sexual in nature (risqué) and/or using profane language; sometimes using " \
                  "gender or race based humor.\n "

    elif round_category == 'Character Comedy':
        example = "Derives humor from a persona invented by a performer; often from stereotypes.\n"

    elif round_category == 'Cringe Comedy':
        example = "A comedy of embarrassment, in which the humor comes from inappropriate actions or " \
                  "words; usually popular in television shows and film, but occasionally in stand-up as " \
                  "well.\n "

    elif round_category == 'Deadpan Comedy':
        example = "Not strictly a style of comedy, it is telling jokes without a change in facial " \
                  "expression or change of emotion.\n "

    elif round_category == 'Heritage Comedy':
        example = "A method or genre in which a comedian discus humorous traits or stereotypes about " \
                  "their own culture or heritage.\n "

    elif round_category == 'Improvisational Comedy':
        example = "Improv is when the plot, characters and dialogue of a game, scene or story are made " \
                  "up in the moment. Make sure you don't use old material for this one. \n "

    elif round_category == 'Insult Comedy':
        example = "A form which consists mainly of offensive insults directed at the performer's " \
                  "audience and/or other performers. \n "

    elif round_category == 'Musical Comedy':
        example = "A form of alternative comedy where humor is mostly derived from music with (or " \
                  "sometimes without) lyrics.\n "

    elif round_category == 'Observational Comedy':
        example = "Pokes fun at everyday life, often by inflating the importance of trivial things or by " \
                  "observing the silliness of something that society accepts as normal.\n "

    elif round_category == 'One-liners':
        example = "A joke that is delivered in a single line. A good one-liner is said to be pithy - " \
                  "concise and meaningful.\n "

    elif round_category == 'Physical Comedy':
        example = "Somewhat similar to slapstick, this form uses physical movement and gestures; often " \
                  "influenced by clowning.\n "

    elif round_category == 'Prop Comedy':
        example = "Relies on ridiculous props, casual jackets or everyday objects used in humorous ways.\n"

    elif round_category == 'Shock Humor':
        example = "A style of comedy that uses Shock value to invoke a strong negative emotion as well " \
                  "as a comedic.\n "

    elif round_category == 'Sketch Comedy':
        example = "A shorter version of a sitcom, practised and typically performed live.\n"

    elif round_category == 'Spoof':
        example = "The recreating of a book, film or play for humor; it can be used to make fun of, " \
                  "or ridicule, a certain production.\n "

    elif round_category == 'Surreal Comedy':
        example = "A form of humor based on bizarre juxtapositions, absurd situations, and nonsense " \
                  "logic.\n "

    elif round_category == 'Topical Comedy / Satire':
        example = "Relies on headlining/important news and current affairs; it dates quickly, but is a " \
                  "popular form for late night talk-variety shows.\n "

    elif round_category == 'Wit / Wordplay':
        example = "More intellectual forms based on clever, often subtle manipulation of language (" \
                  "though puns can be crude and farcical).\n "
    print(example)
