def extraction(args):
    import spacy
    nlp = spacy.load('en_core_web_lg')
    with open(args.input_file,'w') as file_out:
        with open(args.input_SOP_file) as file_in:
            for sentence in file_in.readlines():
                doc = nlp(sentence)
                subject_phrase = get_subject_phrase(doc)
                object_phrase = get_object_phrase(doc)
                if subject_phrase is None or object_phrase is None:
                    print("The sentence \'" + sentence.replace("\n",
                                                               "") + "\' will not be added, because subj or dobj is None")
                    continue
                sentence = sentence.replace(subject_phrase.text, '<e1> ' + subject_phrase.text + ' </e1>', 1)
                sentence = sentence.replace(object_phrase.text, '<e2> ' + object_phrase.text + ' </e2>', 1)
                file_out.write(sentence)


def get_subject_phrase(doc):
    for token in doc:
        if ("subj" in token.dep_):
            return token


def get_object_phrase(doc):
    for token in doc:
        if ("dobj" in token.dep_):
            return token
