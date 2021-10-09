def describe_pet(name=None,animal="dog"):
	print(f"I have a {animal}")

	if name:
		print(f"Its called {name}")

print(describe_pet(animal="Cat"))

print(describe_pet())

print(describe_pet(name="Leo",animal="Lion"))

print(describe_pet("Squid","Tiger"))

