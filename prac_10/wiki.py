import wikipedia

# Modify your program so that when it gets the page, it prints the title, summary and the URL.
page_title = str(input("Please enter a page to visit: "))
if page_title != "":
    wikipedia.search(page_title)
    wikipedia.page(page_title)
    print(wikipedia.search)
else:
    print("Goodbye.")
