from wtmod import ro_0d, md_0d, pump

for mod in (pump, ro_0d, md_0d):
    y = mod.run()
    print(mod.__name__, y)
