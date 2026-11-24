[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/kunala23/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/kunala23/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

<sub>Entered on [make.fun](https://make.fun/?ref=t1ajmem7&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards</sub>

# Seventeen Syllables of Debugging

One haiku about debugging, written by a small Python program.

## The haiku

```
Cursor blinks at three
the log line says nothing new
and the bug was me
```

Three lines, 5-7-5 syllables, 71 characters. The picture at the centre
is concrete — a cursor blinking at three in the morning, a log line
that says nothing new — and the last line turns the poem: after a night
of hunting, the bug was the person hunting it.

## How it works

`main.py` holds the haiku as a fixed list of three lines and checks its
own work before writing anything out:

- exactly 3 lines,
- syllable counts of 5, 7 and 5 (counted with a small vowel-group
  counter plus a short exceptions table),
- at most 200 characters, and more than white space.

If any check fails, the program exits with an error and writes no file.
When the checks pass it writes the haiku to `/output/entry.txt`.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.txt`. To write somewhere else (for a local
test, for example), set `MAKEFUN_OUTPUT`:

```sh
MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
```

No network access, no dependencies, no secrets — just Python 3 and the
standard library.

## License

MIT. See [LICENSE](LICENSE).
