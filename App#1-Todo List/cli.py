import logic

brain = logic.Logic()
while brain.running:
    brain.write_todos("walk the dog")
    brain.get_todos()
