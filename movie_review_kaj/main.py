# Advanced Code Challenge: Movie Review
# By Keith Alexander Jr.

def movie_review(rating):
  if (rating <= 5):
    quote = "Avoid at all costs!"
    return quote
  elif (rating > 5 and rating < 9):
    quote2 = "This one was fun."          
    return quote2
  else:
    quote3 = "Outstanding!"
    return quote3

# Uncomment each function calls to test the movie_review function:
print(movie_review(9))
# Result: print "Outstanding!"
print(movie_review(4))
# Result: print "Avoid at all costs!"
print(movie_review(6))
# Result: print "This one was fun."