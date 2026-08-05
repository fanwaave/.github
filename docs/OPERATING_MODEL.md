# Fanwaave GitHub and Linear operating model

## Canonical systems

- GitHub organization: https://github.com/fanwaave
- GitHub Project: https://github.com/orgs/fanwaave/projects/1
- Linear project: https://linear.app/denman/project/githubcomfanwaave-6ba038b59dbc
- Migration issue: https://linear.app/denman/issue/DEN-1874
- Reliability issue: https://linear.app/denman/issue/DEN-1875

## Repository ownership

`fanwaave/push-notification-server.rs` owns push and contact delivery implementation, provider adapters, contracts, tests, CI, security controls, and release artifacts.

`fanwaave/.github` owns the public organization profile, community-health defaults, branching and deployment policy, repository boundaries, security guidance, semantic conflict-resolution rules, and the GitHub/Linear relationship declaration.

Infrastructure repositories remain separate from application source. A `*-infra` repository must not be nested under `*-monorepo/apps` as a Git submodule. Cross-repository integration uses versioned interfaces, SDKs, events, immutable artifacts, and explicitly owned deployment configuration.

## Planning and delivery

Linear is the planning and dependency source of record. GitHub repositories own source code, pull-request review, exact-head checks, release evidence, and immutable artifact provenance. `fanwaave-project` provides the public organization execution view across repositories.

Work flows from a Linear issue to a focused feature branch and reviewed GitHub pull request. Promotion follows [`../BRANCHING_AND_DEPLOYMENT.md`](../BRANCHING_AND_DEPLOYMENT.md), including the checked-in `dev`/GitFlow/GitOps requirements, validation thresholds, immutable artifact identity, deployment impact, and rollback or roll-forward evidence.

## Conflict resolution

Conflicts are resolved semantically. Review the merge base, both complete sides, surrounding contracts and tests, path-scoped history, and normally 3–10 relevant commits. Inspect related repositories when a shared contract or deployment boundary changes. Never select all of `ours` or `theirs` as a shortcut, rebase shared history, or force-push a protected branch.

## Security and credentials

No access token, private key, provider credential, customer data, device token, phone number, email address, or capability-bearing push endpoint belongs in source, workflow YAML, CI output, issues, GitHub Projects, or Linear. Use managed secret systems and private vulnerability reporting.

## Relationship evidence

[`../repository-relationships.json`](../repository-relationships.json) records the organization ID, canonical repositories, Linear project, and GitHub Project using stable identifiers. Update it through a reviewed pull request whenever ownership or routing changes.
