# # from django.test import TestCase
#
# # Create your tests here.
# from profanity_filter import ProfanityFilter
#
# pf = ProfanityFilter()
#
# pf.censor("That's bullshit!")
# # "That's ********!"
#
# pf.censor_word('fuck')
# pf.is_profane('fuck')


# better profanity
from better_profanity import profanity

if __name__ == "__main__":
    dirty_text = "That l3sbi4n did a very good H4ndjob."

    x = profanity.contains_profanity(dirty_text)
    print(x)