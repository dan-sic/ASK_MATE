import re


def highlight_search_term(searched_term, sequence):
    # highlighted_text = '<span class="bg-success" style="margin-right:0;">' + searched_term + '</span>'
    # searched_term_re = re.compile(re.escape(searched_term), re.IGNORECASE)
    # replacement = lambda matchobj: '<span class="bg-success" style="margin-right:0;">' + matchobj + '</span>'
    # new_sequence = searched_term_re.sub(repl=lambda matchobj: '<span class="bg-success" style="margin-right:0;">' + matchobj + '</span>', string=sequence)
    new_sequence = re.sub(searched_term, repl=lambda matchobj: '<span class="bg-success" style="margin-right:0;">' + matchobj.group(0) + '</span>', string=sequence, flags=re.I)
    # new_sequence = sequence.replace(searched_term, highlighted_text)
    return new_sequence
