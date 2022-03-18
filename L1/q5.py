def is_palindrome(s):
    """ Check if {s} is a palindrome (case sensitive)
    """
    s_inverted = ""
    for l in s:
        s_inverted = l + s_inverted
    
    return s == s_inverted