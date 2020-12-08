import subprocess as s

filename = input("What is the filename? ")

s.run(["git", "add", filename])

comments = input("What comments do you have? ")
comments.split()

s.run(["git", "commit", "-m", comments])

s.run("git", "pull")

s.run("git", "push", "origin", "main")
