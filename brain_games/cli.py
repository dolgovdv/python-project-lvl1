#!/usr/bin/env python
import prompt


def say_hi():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
