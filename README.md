<!-- README.md -->
# GitHub Secure CI/CD Demo

This repo demonstrates a step‑by‑step POC for building a secure CI/CD pipeline on GitHub, evolving through commits:

1. Repo hardening - setup approvals and environment
2. Branch protection - using ruleset called defult on the default branch (main)
3. Build & test - this runs in the CI workflow
4. Security gates - auto running the default code ql statis analysis scan
5. Deployment - manual gate requires approval on the environment
6. Monitoring & audit
