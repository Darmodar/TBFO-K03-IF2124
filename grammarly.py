def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    line = file.readline()
    while line != "":
        head, body = line.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))

        line = file.readline()

    file.close()

    return cfg

def is_terminal(string):
    list_of_terminal = [
        "EQUAL",
        "IS_EQUAL",
        "TYPE_EQUAL",
        "OPEN_ROUND_BRACKET",
        "CLOSE_ROUND_BRACKET",
        "SEMICOLON",
        "COLON",
        "PLUS",
        "MINUS",
        "MULTIPLY",
        "DIVIDE",
        "MODULO",
        "PLUS_EQUAL",
        "MINUS_EQUAL",
        "MULTIPLY_EQUAL",
        "DIVIDE_EQUAL",
        "MODULO_EQUAL",
        "LESS_EQUAL",
        "LESS",
        "GREATER_EQUAL",
        "GREATER",
        "NOT_EQUAL",
        "AND",
        "OR",
        "NOT",
        "LET",
        "VAR",
        "CONST",
        "IF",
        "ELSE",
        "TRY",
        "CATCH",
        "FINALLY",
        "WHILE",
        "FALSE",
        "TRUE",
        "NULL",
        "BREAK",
        "CONTINUE",
        "FUNCTION",
        "FOR",
        "FROM",
        "IMPORT",
        "IN",
        "RETURN",
        "WITH",
        "COMMA",
        "DOT",
        "FUNCTION",
        "OPEN_SQUARE_BRACKET",
        "CLOSE_SQUARE_BRACKET",
        "OPEN_CURLY_BRACKET",
        "CLOSE_CURLY_BRACKET",
        "SINGLE_Q",
        "DOUBLE_Q",
        "VARIABLE",
        "INTEGER",
        "STRING",
        "FLOAT",
        "NEWLINE",
        "MULTILINE",
        "SWITCH",
        "CASE",
        "DEFAULT",
        "DELETE",
        "FUNCTION",
    ]
    
    return string in list_of_terminal

def is_variables(string):
    return not is_terminal(string)