---
tags:
  - index
aliases:
  - gnomon documentation
---
# gnomon documentation

Each entry answers one class of question about `gnomon`, so a reader consults one rather than several.

| Entry | Content |
| --- | --- |
| [Project overview](project-overview.md) | Why the framework exists: the failure modes that compound as a theoretical framework grows, and the architectural stance that answers them. |
| [User guide](guide/_index.md) | How the installed tool is operated, from the Python version it requires to each command of its entry point. |
| [Design documentation](design/_index.md) | What the framework must achieve, how it is structured, and what each aspect decides. Three tiers separate the criteria that cannot be overridden from the decisions implementing them. |
| [Methods for reasoning](methods-reasoning/_index.md) | How reasoning is conducted and formalized outside `gnomon`, from what a discipline demands of a valid argument to the formal domains that model an epistemic state and its transitions. |
| [Methods for taxonomies](methods-taxonomies/_index.md) | Which criteria warrant a classification, and the procedure that applies them to build a taxonomy. No algorithm yields a universally correct partition, so each classification must declare the function it serves. |
| [Design TODO](TODO.md) | Where the design currently stands, and which steps remain open. |

## Note conventions

Every note declares a frontmatter block and is registered in the index of its folder. The [keys each note declares, the tag vocabulary, and the form a cross-reference takes](../CONTRIBUTING.md#writing-documentation) are fixed once, in the contributor guidelines.
