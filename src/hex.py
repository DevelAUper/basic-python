import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]


match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        for ch in x:
            encoding += hex(ord(ch))
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ''.join(chr(int(h, 16)) for h in x.strip().split('0x') if h)
        print(decoding)


#strip() cleans up stray newlines so they don’t leak into the output.
#split('0x') breaks the string at each 0x marker.
#if h filters out the leading empty chunk from the split.
#int(h, 16) parses each hex pair.
#chr(...) turns that code point into a character.
#''.join(...) stitches all characters back into the decoded string.
        
