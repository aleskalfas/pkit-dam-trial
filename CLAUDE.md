# Claude Code instructions

This file is loaded by Claude Code at session start. The kit-shipped rules
and tool-hygiene conventions are included below; add project-specific
instructions after the includes.

@.pkit/rules/core.md
@.pkit/rules/capabilities.md
@.pkit/rules/project.md

## This project

`wordtools` is a small Python package of text helpers, standard library only. Its coding conventions are `docs/conventions.md`. Run the tests from the repository's root with `python3 -m unittest discover -s tests -t .`.
