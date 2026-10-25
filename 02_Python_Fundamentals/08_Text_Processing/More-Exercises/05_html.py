def print_in_html(info: dict, tag: dict):
    for key in info.keys():
        for i in range(len(info[key])):
            print(tag[key][0])
            print("    " + info[key][i])
            print(tag[key][1])

tags = {
    "title" : ["<h1>", "</h1>"],
    "article" : ["<article>", "</article>"],
    "comments" : ["<div>", "</div>"]
}

information = {
    "title" : [],
    "article" : [],
    "comments" : []
}

information["title"].append(input())
information["article"].append(input())

while True:
    comment = input()
    if comment == "end of comments":
        break
    information["comments"].append(comment)

print_in_html(information, tags)