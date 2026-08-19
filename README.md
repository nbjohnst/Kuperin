# Kuperin

**A project exploring structured, persistent context for long-horizon collaboration with large language models.**

## The idea

Large language models are remarkably good at reconstructing context from natural language.

But in a long-running project, we repeatedly ask inference to do two different jobs:

1. reconstruct what is already known;
2. reason and create from that knowledge.

Kuperin asks whether some of the first job can be pulled outside the AI's black box and handled explicitly.

> **Stop spending the creative engine on plumbing.**

The working division of labor is simple:

**The database remembers.**  
**The graph connects.**  
**The compiler decides what matters right now.**  
**The LLM interprets and creates.**  
**The integrator records what changed.**  
**The human decides what becomes authoritative.**

## The loop

```text
Persistent State
      ↓
   Retrieval
      ↓
Context Compiler
      ↓
     LLM
      ↓
Generated Work
      ↓
State Integration
      ↓
  Evaluation
      ↓
Updated Persistent State
