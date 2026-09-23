# Write code that builds an APA book citation given:
#
# - Author
# - Title
# - Publication year
# - Publisher
#
# Format: `Author. (Year). Title of Book. Publisher.`
#
# Example:
#
# Author: Tate, Bruce
# Title: Seven Languages in Seven Weeks
# Year: 2010
# Publisher: The Pragmatic Bookshelf
#
# Tate, Bruce. (2010). Seven Languages in Seven Weeks. The Pragmatic Bookshelf.

author = input("Author: ")
title = input("Title: ")
year = input("Year: ")
publisher = input("Publisher: ")

print(f"{author} ({year}). {title}. {publisher}.")
