from rply import LexerGenerator


lg = LexerGenerator()

lg.add("STEP", r"s")
lg.add("TURN_LEFT", r"l")
lg.add("TURN_RIGHT", r"r")
lg.add("FUNC", r"a|b|c|d|e|f|g|h|i|j|k|m|n|o|p|q|t|u|v|w|x|y|z")
lg.add("COLON", r"\:")
lg.add("NEWLINE", r"\n+ *\n*")
lg.add("DIGIT", r"\d+")
lg.add("NAME", r"[A-Z]")
lg.add("(", r"\(")
lg.add(")", r"\)")
lg.add(",", r"\,")

lg.ignore(r" +")
lg.ignore(r"\#.*")

TOKENS = [r.name for r in lg.rules]

lexer = lg.build()
