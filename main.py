def get_num_words(content_string):
    words = content_string.split()
    num = len(words)
    return num

def count_characters(content_string):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    results = {}
    input_sting = content_string.lower()

    for c in input_sting:
        if c in alpha:
            if c in results:
                results[c] += 1
            else:
                results[c] = 1

    return results

def sort_on_count(dict):
    #kees = dict.keys()
    #print(kees)
    #kee = kees[1]
    return dict["count"]

def main():
    document = "books/frankenstein.txt"
    counts_dict, counts_list = {}, []

    with open(document) as f:
        file_contents = f.read()
        #print(file_contents)
        number = get_num_words(file_contents)
        counts_dict = count_characters(file_contents)

    for key in counts_dict:
        counts_list.append({"character" : key, "count" : counts_dict[key]})

    counts_list.sort(reverse = True, key=sort_on_count)

    #print(number, counts)
    print(f"--- Begin report of {document} ---")
    print(f"{number} words found in the document")
    print()
    for d in counts_list:
        c = d["character"]
        n = d["count"]
        print(f"The '{c}' character was found {n} times")

main()