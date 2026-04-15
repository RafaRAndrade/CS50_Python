
def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase

def main():
    user_phrase = input ()
    result = convert(user_phrase)
    print(result)
main()
