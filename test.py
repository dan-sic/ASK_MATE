# do we need this file?
query = [('1c489e5b-9fe2-4aa8-af93-036ee57cfa5f', None, 1, 0, 'pytanie', 'odpowiedz', None), ('84e72737-b4ff-4c10-9c35-0a7236e35990', None, 1, 0, 'pytanie', 'odpowiedz', None), ('72314464-9b8e-4808-9523-580545e07f62', None, 1, 0, 'pytanie', 'odpowiedz', None), ('410529e3-ddf7-4451-b224-abe298040707', None, 1, 0, 'nowe pytanie', 'to jest najnowsze pytanie', None), ('f33f277f-a78e-401c-af0f-b62d97e8c1f5', None, 1, 0, 'to jest nowe pytanie', 'lorem ipsum', None), ('399b4bba-85b2-475f-8613-571c56250e93', None, 1, 0, 'test', 'dksladklskdl', None)]



def convert_query_to_dictionary():
    keys = ['id', 'vote_number', 'view_number', 'title', 'message', 'image']
    result = []
    for element in query:
        new_zip = zip(keys, element)
        new_dictionary = dict(new_zip)
        result.append(new_dictionary)
    return result


