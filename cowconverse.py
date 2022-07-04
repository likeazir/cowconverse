#! /usr/bin/env python3

import re
import subprocess
import itertools
import random


def random_cow_name() -> str:
    return random.choice(
        subprocess.run(["cowsay -l"], capture_output=True, shell=True)
        .stdout.decode()
        .split("\n")
    )


def get_cow(cow_name: str = random_cow_name()):
    return subprocess.run(
        [f"fortune | cowsay -f {cow_name}"], capture_output=True, shell=True
    ).stdout.decode()


def get_conversing_cows(
    cowleft_name: str = random_cow_name(), cowright_name: str = random_cow_name()
) -> str:
    cowleft = get_cow(cowleft_name)
    cowright = get_cow(cowright_name)
    cowleft_l = cowleft.split("\n")
    max_line_len_l = max(map(len, cowleft_l))
    speechbubble = True
    conversation = []
    for l, r in itertools.zip_longest(cowleft_l, cowright.split("\n"), fillvalue=""):
        if not speechbubble:
            l = l.rstrip().ljust(max_line_len_l, " ")
            l = l.translate(str.maketrans(
                {"\\": "/", "/": "\\", "(": ")", ")": "("}))
            l = l[::-1]
        if re.match(r" *-+ *", l):
            speechbubble = False
        conversation.append(l + " " * 5 + r)
    return "\n".join(conversation)


def main():
    print(get_conversing_cows())


if __name__ == "__main__":
    main()
