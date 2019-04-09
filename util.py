import re


def replace_string(matchobj):
    return '<span class="bg-success" style="margin-right:0;">' + matchobj.group(0) + '</span>'


def highlight_search_term(searched_term, sequence):
    new_sequence = re.sub(searched_term, replace_string, sequence, flags=re.I)
    return new_sequence
