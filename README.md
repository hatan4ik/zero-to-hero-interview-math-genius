# Zero→Hero Interview — Math‑Genius Edition

A complete, opinionated prep repository for senior/principal **coding + system design** interviews.
Built around three pillars:
1. **Coding Interview (7+ archetypes)** — math → pseudocode → Python/Java/C++ → traces.
2. **System Design (Zero→Hero)** — equations, modeling, cloud mappings, patterns-as-theorems.
3. **Execution Plan** — 8-week daily schedule, rubrics, mistake logs.

> Everything is plain text + code. Clone and go.

# Table of Contents
- [Structure](#structure)
- [What's inside (quick links)](#whats-inside-quick-links)
- [Quickstart](#quickstart)
- [CI & Docs](#ci--docs)
- [Run code / tests locally](#run-code--tests-locally)
- [Authoring notes](#authoring-notes)
- [If you came for one thing](#if-you-came-for-one-thing)
- [Notes](#notes)

## Structure

- part1-coding
  - [01-hash-two-sum](part1-coding/01-hash-two-sum/README.md)
  - [02-sliding-window-longest-substring](part1-coding/02-sliding-window-longest-substring/README.md)
  - [03-bfs-level-order](part1-coding/03-bfs-level-order/README.md)
  - [04-intervals-merge](part1-coding/04-intervals-merge/README.md)
  - [05-dp-climbing-stairs](part1-coding/05-dp-climbing-stairs/README.md)
  - [06-toposort-course-schedule](part1-coding/06-toposort-course-schedule/README.md)
  - [07-heap-meeting-rooms](part1-coding/07-heap-meeting-rooms/README.md)
  - [08-advanced-patterns](part1-coding/08-advanced-patterns/README.md)
  - [10-segment-tree-range-query](part1-coding/10-segment-tree-range-query/README.md)
- part2-system-design
  - [01-foundations](part2-system-design/01-foundations/README.md)
  - [02-caching-lb-queues](part2-system-design/02-caching-lb-queues/README.md)
  - [03-sharding-replication-quorums](part2-system-design/03-sharding-replication-quorums/README.md)
  - [04-observability-reliability-security](part2-system-design/04-observability-reliability-security/README.md)
  - [05-cloud-mapping](part2-system-design/05-cloud-mapping/README.md)
  - [06-case-studies](part2-system-design/06-case-studies/README.md)
  - [07-failure-engineering](part2-system-design/07-failure-engineering/README.md)
  - [08-modern-patterns](part2-system-design/08-modern-patterns/README.md)
  - [09-war-stories](part2-system-design/09-war-stories/README.md)
  - [10-faang-deep-dives](part2-system-design/10-faang-deep-dives/README.md)
  - [11-ml-systems](part2-system-design/11-ml-systems/README.md)
- part3-execution
  - [01-8-week-schedule.md](part3-execution/01-8-week-schedule.md)
  - [02-mock-rubrics.md](part3-execution/02-mock-rubrics.md)
  - [03-mistake-log-template.md](part3-execution/03-mistake-log-template.md)
  - [04-cheatsheets.md](part3-execution/04-cheatsheets.md)
  - [05-practice-set.md](part3-execution/05-practice-set.md)
  - [06-faang-specific-prep.md](part3-execution/06-faang-specific-prep.md)

## What's inside (quick links)
- Part 1 — Coding archetypes with Python/Java/C++: [Two Sum](part1-coding/01-hash-two-sum/README.md), [Sliding Window](part1-coding/02-sliding-window-longest-substring/README.md), [BFS](part1-coding/03-bfs-level-order/README.md), [Intervals](part1-coding/04-intervals-merge/README.md), [DP](part1-coding/05-dp-climbing-stairs/README.md), [Topo](part1-coding/06-toposort-course-schedule/README.md), [Heap/Greedy](part1-coding/07-heap-meeting-rooms/README.md), [Advanced Patterns](part1-coding/08-advanced-patterns/README.md), [Segment Tree](part1-coding/10-segment-tree-range-query/README.md).
- Part 2 — System design: [Foundations](part2-system-design/01-foundations/README.md), [Caching/LB/Queues](part2-system-design/02-caching-lb-queues/README.md), [Sharding/Replication](part2-system-design/03-sharding-replication-quorums/README.md), [Observability](part2-system-design/04-observability-reliability-security/README.md), [Cloud Mapping](part2-system-design/05-cloud-mapping/README.md), [Case Studies](part2-system-design/06-case-studies/README.md), [Failure Engineering](part2-system-design/07-failure-engineering/README.md), [Modern Patterns](part2-system-design/08-modern-patterns/README.md), [War Stories](part2-system-design/09-war-stories/README.md).
- Part 3 — Execution: [8-Week Schedule](part3-execution/01-8-week-schedule.md), [Rubrics](part3-execution/02-mock-rubrics.md), [Mistake Log](part3-execution/03-mistake-log-template.md), [Cheatsheets](part3-execution/04-cheatsheets.md), [Practice Set](part3-execution/05-practice-set.md), [FAANG-specific Prep](part3-execution/06-faang-specific-prep.md).

## Quickstart

```bash
git init
git add .
git commit -m "Zero→Hero Interview (Math-Genius Edition)"
# create an empty repo on GitHub, then:
git remote add origin <YOUR_GITHUB_REMOTE_URL>
git branch -M main
git push -u origin main
```

## CI & Docs

- **GitHub Actions**: `.github/workflows/ci.yml` runs Python tests (pytest), compiles Java and C++, and runs sanity checks.
- **Docs site**: MkDocs config in `mkdocs.yml` with content under `docs/`. Build locally with:
  ```bash
  pip install mkdocs mkdocs-material
  mkdocs serve  # http://127.0.0.1:8000
  ```

## Run code / tests locally
- Python: `pip install -r requirements-dev.txt && pytest`
- C++: `g++ -std=c++17 part1-coding/<chapter>/cpp/*.cpp && ./a.out` (or your preferred build)
- Java: `javac part1-coding/<chapter>/java/*.java && java MainClass` (or `mvn test` if you add a POM)

## Authoring notes
- Docs mirror repo files via symlinks/snippets: edit under `part1-coding/`, `part2-system-design/`, `part3-execution/`, and MkDocs will pull them in.
- Voice: math first, then pseudocode, then code, with a short “how I’d say it in an interview” narration.
- Keep equations and real numbers in system design; prefer concrete examples over generalities.

## If you came for one thing
- System design formulas and examples: start at [part2-system-design/01-foundations/README.md](part2-system-design/01-foundations/README.md).
- Coding archetypes: pick any Part 1 folder; each has math, pseudocode, and Python/Java/C++.
- Schedule/rubrics to drive practice: [part3-execution](part3-execution/01-8-week-schedule.md).

## Notes

- Part 1 folders include math reasoning, pseudocode, traces, and Python/Java/C++ implementations for each archetype.
- Part 2 leans on equations, real numbers, and pattern tradeoffs; tools under `part2-system-design/tools/`.
- Part 3 provides schedules, rubrics, and practice scaffolding to make the prep repeatable.
