import sys
import re

# list token untuk syntax ke token
tokenregex = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Integer and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "FLOAT"),
    (r'[\+\-]?[1-9][0-9]+',     "INTEGER"),
    (r'[\+\-]?[0-9]',           "INTEGER"),

    # Delimiter
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "OPEN_ROUND_BRACKET"), # Kurung Biasa KIri
    (r'\)',                     "CLOSE_ROUND_BRACKET"),
    (r'\[',                     "OPEN_SQUARE_BRACKET"), # Kurung Siku KIri
    (r'\]',                     "CLOSE_SQUARE_BRACKET"),
    (r'\{',                     "OPEN_CURLY_BRACKET"), # Kurung Kurawal Kiri
    (r'\}',                     "CLOSE_CURLY_BRACKET"),
    (r'\;',                     "SEMICOLON"), 
    (r'\:',                     "COLON"),

    # Operator
    
    (r'\*=',                    "MULTIPLY_EQUAL"),
    (r'/=',                     "DIVIDE_EQUAL"),
    (r'\+=',                    "PLUS_EQUAL"),
    (r'-=',                     "MINUS_EQUAL"),
    (r'%=',                     "MODULO_EQUAL"),
    (r'\+',                     "PLUS"),
    (r'\-',                     "MINUS"),
    (r'\*',                     "MULTIPLY"),
    (r'/',                      "DIVIDE"),
    (r'%',                      "MODULO"),
    (r'<=',                     "LESS_EQUAL"),
    (r'<',                      "LESS"),
    (r'>=',                     "GREATER_EQUAL"),
    (r'>',                      "GREATER"),
    (r'!=',                     "NOT_EQUAL"),
    (r'\===',                   "TYPE_EQUAL"),
    (r'\==',                    "IS_EQUAL"),
    (r'\=',                      "EQUAL"),
    
    
    
    # Keyword
    (r'\band\b',                "AND"),
    (r'\bor\b',                 "OR"),
    (r'\bnot\b',                "NOT"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\belse if\b',            "ELSE_IF"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),
    (r'\bnull\b',               "NULL"),
    (r'\bin\b',                 "IN"),
    (r'\bvar\b',                "VAR"),
    (r'\blet\b',                "LET"),
    (r'\bconst\b',              "CONST"),
    (r'\bclass\b',              "CLASS"),
    (r'\bdef\b',                "DEF"),
    (r'\breturn\b',             "RETURN"),
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bwith\b',               "WITH"),
    (r'\bdict\b',               "DICTIONARY"),
    (r'\,',                     "COMMA"),
    (r'\.',                     "DOT"),
    (r'\bswitch\b',            "SWITCH"),
    (r'\bcase\b',            "CASE"),
    (r'\bdefault\b',            "DEFAULT"),
    (r'\bdelete\b',            "DELETE"),
    (r'\bfunction\b',            "FUNCTION"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "VARIABLE"),

]


# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, tokenregex):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in tokenregex:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,tokenregex)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)

if __name__ == "__main__":
    create_token('test.txt')