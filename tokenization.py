import tiktoken

encoding1 = tiktoken.encoding_for_model("o4-mini")
encoding2 = tiktoken.encoding_for_model("gpt-4")

tokens4o = encoding1.encode("Hello World, this is a bigger sentence to see any drastic difference but i am still trying to create any difference in the ugabuga rabbit racoon type shit")
tokens4 = encoding2.encode("Hello World, this is a bigger sentence to see any drastic difference but i am still trying to create any difference in the ugabuga rabbit racoon type shit")

print(f"The tokens for 4o are {tokens4o} and for 4 is {tokens4}")
print(f"And the length of tokens of 4o are {len(tokens4o)} and for 4 are {len(tokens4)}")