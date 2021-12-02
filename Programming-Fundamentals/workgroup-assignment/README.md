# Group assignment 1

Due date **December 3rd, 22:00 Madrid time**.  Do your solutions to the
exercises in **`exercises.py`**.

All members of the group **must** participate, there should be at
least one commit by each member of the group in your final submission.
In order to submit your assignment, just make sure to push the latest
changes **before the deadline**.


## Exercise 1

**(2 points) maximum value between two indices**.

Create a function called `max_between` that takes an unsorted list and two
indices and returns what's the maximum in the segment contained between those
two indices.

Can you think of a faster implementation of your algorithm if you're ensured
that the list is sorted?  Reason it in a comment after the function.

## Exercise 2

**(2 points) value appears in both lists**.

Create a function `appears_in_both` that receives two unsorted lists and one
integer. The function should return True if the integer appears in both lists
and False otherwise.

Create another version of the function in which the lists are sorted.

## Exercise 3

**(2 points) intersection**.

Create a function intersection that receives two lists as parameters and
returns the intersection of them (intersection meaning a list with the elements
they have in common).

Could you find a faster implementation if you're sure that the two lists you
receive are sorted?   Reason idt in a comment after the function.

## Exercise 4

**(2 points) difference**.

Create a function difference that receives two lists as parameters and returns
the difference of them (difference meaning a list with the elements they don't
have in common).

could you find a faster implementation if you're sure that the two lists you
receive are sorted?   Reason it in a comment after the function.


## Exercise 5

**(2 points) dictionary search**.

Imagine we implemented a dictionary (the one with word
definitions, not Python`s dictionary) using a list of dictionaries, where each
internal dictionary represents a word. I.E:

```python
dictionary = [
    {
        "word": "A",
        "definition": "the 1st letter of the English alphabet"
    },
    {
        "word": "Absent",
        "definition": "non-existent, lacking"
    },
    {
        "word": "Battlestar Galactica",
        "definition": "Battlestar Galactica is an American science fiction media franchise created by Glen A. Larson. The franchise began with the original television series in 1978 and was followed by a short-run sequel series (Galactica 1980), a line of book adaptations, original novels, comic books, a board game, and video games. A re-imagined version of Battlestar Galactica aired as a two-part, three-hour miniseries developed by Ronald D. Moore and David Eick in 2003. That miniseries led to a weekly television series, which aired until 2009. A prequel series, Caprica, aired in 2010. "
    },
    {
        "word": "Bear",
        "definition": "any of a family (Ursidae of the order Carnivora) of large heavy mammals of America and Eurasia that have long shaggy hair, rudimentary tails, and plantigrade feet and feed largely on fruit, plant matter, and insects as well as on flesh"
    },
    {
        "word": "Beet",
        "definition": "The beetroot is the taproot portion of a beet plant,[1] usually known in Canada and the USA as beets while the vegetable is referred to as beetroot in British English, and also known as the table beet, garden beet, red beet, dinner beet or golden beet. It is one of several cultivated varieties of Beta vulgaris grown for their edible taproots and leaves (called beet greens); they have been classified as B. vulgaris subsp. vulgaris 'Conditiva' Group.[2]"
    }
]
```

Implement the function `dictionary_lookup` that receives the whole dictionary as
an ordered list and a word and returns the word's definition in case it exists.
It should return None in case the word doesn't exist.

Given the above dictionary, the function should behave as follows:

```python
dictionary_lookup(dictionary, "A") # returns 'the 1st letter of the English alphabet'
dictionary_lookup(dictionary, "Absent") # returns 'non-existent, lacking'
dictionary_lookup(dictionary, "Potato") # returns None
```

What's the worst case runtime for your algorithm?  Why so?  Please answer these
questions in comments after your implementation.
