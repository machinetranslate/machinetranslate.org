---
description: Adaptive machine translation
---

# Adaptive machine translation

**Adaptive machine translation** is a machine translation system that learns from human feedback and adapts its output on the fly. This paradigm is focused in the [post-editing](post-editing.md) phase.

Adaptive machine translation requires two language models: a static model and a dynamic model. The static model helps to generate translations as close to human translations as possible. The dynamic model is updated with the newly-learned fragments.
When translating, the system gives more weight to the dynamic model.

### Workflow

1. The engine generates a machine translated output.

2. The output is fixed.

3. The engine learns from the correction.

4. The system reduces the chance of repeating the error.

Adaptive machine translation reduces the time a human takes to edit a machine translation suggestion.
