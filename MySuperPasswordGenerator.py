
import random
import string

randstring = '' .join(random.sample(string.ascii_letters + string.digits + string.punctuation, 24))
print("Here's ur password, silly goose:", randstring)
