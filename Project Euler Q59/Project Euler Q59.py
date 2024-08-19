## Project Euler Q59 Solution
## Find the sum of the ASCII values in the original text, if the decrypted text contains common English words.
## lowercase a-z is 97-122

cipher = [int(x) for x in open('Q59 Cipher.txt').read().split(',')]

def decrypt(cipher, key):
    return [c ^ key[i % len(key)] for i, c in enumerate(cipher)]

def is_english(text):
    return all(32 <= c < 128 for c in text)
ascii_to_english = lambda text: ''.join(chr(c) for c in text)
def contains_common_words(text):
    common_words = ["the", "and", "to", "of", "a", "in", "that", "is", "it", "with", "have", "this"]
    decrypted_text = ''.join(chr(c) for c in text)
    count = sum(1 for word in common_words if word in decrypted_text)
    return count > 8



for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            key = [a, b, c]
            decrypted = decrypt(cipher, key)
            if is_english(decrypted) and contains_common_words(decrypted):
                print(f"Key: {key}, Decrypted Text: {ascii_to_english(decrypted)}")
                print(sum(decrypted))

