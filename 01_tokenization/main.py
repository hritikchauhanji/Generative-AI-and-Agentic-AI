import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, world! This is a test of the tiktoken library."

encoded = enc.encode(text)

print("Encoded tokens:", encoded)
# Encoded tokens: [13225, 11, 2375, 0, 1328, 382, 261, 1746, 328, 290, 260, 8251, 2488, 11282, 13]

decoded = enc.decode([13225, 11, 2375, 0, 1328, 382, 261, 1746, 328, 290, 260, 8251, 2488, 11282, 13])

print("Decoded text:", decoded)