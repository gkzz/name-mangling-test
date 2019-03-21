class SecretString:
    """A not-at-all secure way to store a secret string."""

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only show the string if the pass_phrase is correct."""
    
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""

if __name__ == "__main__":
    obj = SecretString("ACME: Top Secret", "antwerp")
    print('obj.decrypt("antwerp"): {}'.format(obj.decrypt("antwerp")))
    #obj_secret_string.decrypt("antwerp"): ACME: Top Secret
    print('-------------------------')
    print('obj._SecretString__plain_string: {}'.format(obj._SecretString__plain_string))