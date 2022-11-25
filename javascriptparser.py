from argparse import ArgumentParser
from regrex import create_token
from grammarly import read_grammar
from cfgcnf import CFG_to_CNF
from cmyk import CYK_parse

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("javascriptfile", type=str, help="Nama File yang hendak diparse.")
    args = argument_parser.parse_args()
    if CYK_parse(CFG_to_CNF(read_grammar("grammar.txt")), create_token(args.javascriptfile)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")