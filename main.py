import argparse
import os
import re


def sloc(path):
    total_lines = 0
    blank_lines = 0
    comment_lines = 0
    for root, dirs, files in os.walk(os.path.normpath(path)):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    total_lines += len(lines)
                    for line in lines:
                        if line == "\n":
                            blank_lines += 1
                            continue
                        if re.findall(r'(#=[^!].*)|(?:\"\"\"(.|\n*)*?\"\"\")|(?:\'\'\'(.|\n*)*?\'\'\')', line):
                            comment_lines += 1
    if blank_lines / total_lines * 100 > 25:
        blank_lines = total_lines * 0.25
    comment_statistics = comment_lines / total_lines
    return total_lines, blank_lines, comment_lines, comment_statistics


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog="SLOC")
    arg_parser.add_argument('-p', '--path', default=".", required=False)
    args = arg_parser.parse_args()
    sloc = sloc(f"{args.path}")
    print(
        f'Physical SLOC: total lines {sloc[0]}, blank lines {sloc[1]}, comment lines {sloc[2]}, comment_ratio {sloc[3]}')
