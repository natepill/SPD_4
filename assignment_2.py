"""

Twitter Follow Suggestions
You’re working an internship at Twitter and are tasked to improve suggestions
for accounts to follow, which already works great for established accounts because
it uses content from your tweets and other accounts you follow to suggest new ones.
However, when a new user signs up none of this information exists yet,
but Twitter still wants to make some follow suggestions.
Your team asked you to implement a function that accepts a new user’s handle
and an array of many other users’ handles, which could be very long
– Twitter has over 330 million active accounts!

You need to calculate a similarity
score between a pair of handles by looking at the letters each contains, scoring +1
for each letter in the alphabet that occurs in both handles but scoring –1 for each
letter that occurs in only one handle.

Your function should return k handles from the
array that have the highest similarity score to the new user’s handle.

Example execution:
handles = ['Dogex`Coin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']


Solution:
init most_similar_handles of size K
calculate sum of the union of A and B
Subtract that sum with the set difference between B and A
*Probably optimize with max heap* Place value in most_similar_handles array (if possible)
return most_similar_handles


"""


def follower_suggestions(user_handle, handles, k=1):

    # store most similar handles
    most_similar_handles = []
    # store handles by score<int>:handle<str>
    scores_and_handles = {}
    for handle in handles:
        # number of same chars
        same_chars = char_counter(set(user_handle).union(set(handle)))
        # calculate similarity score by Subtracting # similar chars with # of different chars
        similarity_score = same_chars - char_counter(set(handle).difference(set(user_handle)))

        most_similar_handles[similarity_score] = handle


    all_scores = scores_and_handles.keys()
    # determine if handle should be placed in most_similar_handles
    for _ in range(k):
        # find, remove max score from all_scores and put in most_similar_handles
        most_similar_handles.append(scores_and_handles[all_scores.pop(max(all_scores))])


    return most_similar_handles

def char_counter(input):

    char_sum = 0
    for char in input:
        char_sum += 1

    return char_sum



if __name__ == "__main__":
    # suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

    handles = ['Dogex`Coin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']

    print(follower_suggestions('iLoveDogs', handles, k=2))
