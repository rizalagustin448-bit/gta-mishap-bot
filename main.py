"""Funniest AI Agent Mishap: GTA 6 Launch Week entry.

Writes a single original sentence about the funniest true-to-life
thing an AI coding agent did while its human was busy playing GTA 6
on launch week, to /output/entry.txt, exactly as the competition
requires. The sentence is 175 characters, inside the 1-240 gate,
with no trailing newline so the file holds the sentence and nothing
else. The joke lands on the last clause: the agent faithfully did
exactly what the TODO comments asked, including the one that told
it never to do the thing.
"""

import os

SENTENCE = "While I was busy in Vice City, my agent decided my 47 TODO comments were 'unfinished business' and implemented all of them \u2014 including the one that said 'TODO: never do this.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
