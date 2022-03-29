from SafeNotes import Note
a = Note("test", "this is a note", "pass")
print(a.content)
print(a.decode("pass"))

b = Note("test", "this is another", "pass1")
print(b.decode("pass"))
print(b.content)
