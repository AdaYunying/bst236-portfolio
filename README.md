# Homework 1 - Code with AI

## 🌐 Live Website
 
 https://AdaYunying.github.io/bst236-portfolio/
  
  ---

## Overview

This homework explores AI-assisted coding and the agentic programming paradigm.  
Rather than treating AI as a code generator, I approached it as an implementation agent operating under explicit design constraints.

---

## Tools Used

- **Claude** (planning & structured decomposition)
- **Claude Code** (VS Code agent implementation)
- **GitHub Copilot CLI** (command-line agent)
- **ChatGPT** (high-level planning & installation guidance)
- **VS Code Copilot** (inline refinement)
- **Gemini** (textual and stylistic refinement for website content )

---

# Problem 1 — Static Website Setup

### Strategy

Instead of directly generating HTML, I first asked the agent to:

1. Decompose the repository structure  
2. Explain static website architecture at a high level  
3. Propose design styles before implementation  

Key prompting technique:

> Ask for design options first, then select and refine.

Implementation was handled primarily by Claude (structure) and Copilot (refinement).  
Textual content was iteratively improved using Gemini.   
This structured approach reduced ambiguity and allowed the initial implementation to closely match design expectations.

---

# Problem 2 — Pac-Man Game

### Strategy

1. I first collaborated with Claude to co-design the full game specification prior to implementation. The finalized requirements were consolidated into a structured .md prompt document (pacman-prompt.md), which was then provided to Claude Code as the implementation reference.
2. Before allowing Claude Code to generate any code, I required it to outline its implementation plan. This “plan-first” constraint ensured alignment between design intent and technical execution.
3. After the initial implementation, I repeatedly play-tested the game and iteratively refined behavior. For each requested change, I asked the agent to explain its intended modification logic before editing the code. This reduced unintended side effects and made debugging more controlled and efficient.  

Key prompting technique:

> Plan-first enforcement:  
> “Don’t write code yet. First outline your implementation plan.”

Most core mechanics were correctly implemented in the first pass.

---

# Problem 3 — Auto-Updating arXiv Feed

### Strategy

This problem was implemented using Copilot CLI in a phased workflow:

1. Data fetching script  
2. GitHub Actions automation  
3. Frontend rendering  

Instead of incremental improvisation, I first clarified the overall architecture and provided a detailed specification to the agent, including:

- Explicit query definitions aligned with my research focus
- A clearly defined JSON schema for output
- Automation constraints (scheduled runs, conditional commits)
- Frontend rendering expectations

Before each phase, I ensured that the task scope was fully defined. During implementation, I validated outputs at every stage—for example, manually inspecting retrieved paper titles and abstracts to confirm query relevance, reviewing the JSON structure for correctness, and checking workflow logic before proceeding.

Key prompting technique:

> Provide complete specification before execution, and validate each stage before proceeding.

This phased and specification-driven approach reduced unnecessary iteration and allowed most components to reach high completeness in their initial implementation.

---

# Agentic Programming Takeaways

Across all three problems, I consistently applied:

1. Task decomposition before coding  
2. Clear specification before generation  
3. Plan-first constraints for complex tasks  
4. Phase-based implementation  
5. Structured validation before iteration  

This approach transformed unfamiliar domains into structured and manageable workflows.







