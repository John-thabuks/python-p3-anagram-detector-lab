# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        my_word = sorted(self.word.lower())
        # print(my_word)
        found_anagram = []
        for wl in word_list:
            sorted_wl = sorted(wl.lower())
            print(sorted_wl)
            if my_word == sorted_wl:
                found_anagram.append(wl) 
        return found_anagram

ana = Anagram("listen") 
ana.match(['enlists', 'google', 'inlets', 'banana'])