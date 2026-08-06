# .github

Organization-wide GitHub, branching, agent, and delivery policy for Fanwaave.

## Canonical systems

- Organization: https://github.com/fanwaave
- Push notification server: https://github.com/fanwaave/push-notification-server.rs
- GitHub Project: https://github.com/orgs/fanwaave/projects/1
- Linear project: https://linear.app/denman/project/githubcomfanwaave-6ba038b59dbc

This repository preserves Fanwaave's durable engineering, repository-boundary, GitFlow/GitOps, security, and semantic-conflict policies while providing the public organization profile and shared community-health defaults.

Start with:

- [`BRANCHING_AND_DEPLOYMENT.md`](BRANCHING_AND_DEPLOYMENT.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`REPOSITORY_BOUNDARIES.md`](REPOSITORY_BOUNDARIES.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`SECURITY.md`](SECURITY.md)
- [`docs/ORGANIZATION_HANDBOOK.md`](docs/ORGANIZATION_HANDBOOK.md)
- [`docs/PROJECTS.md`](docs/PROJECTS.md)
- [`docs/OPERATING_MODEL.md`](docs/OPERATING_MODEL.md)

<!-- ore-org-baseline:begin -->
## Account-wide defaults

This public repository is the canonical source for GitHub-supported fallback community files, organization profile content, reusable workflow examples, and public contributor guidance for [`fanwaave`](https://github.com/fanwaave).

- GitHub owner: [`fanwaave`](https://github.com/fanwaave)
- Linear project: [github.com/fanwaave](https://linear.app/denman/project/githubcomfanwaave-6ba038b59dbc)
- Public context: [`ORG_CONTEXT.md`](ORG_CONTEXT.md)
- Canonical agent policy for this repository: [`agents.md`](agents.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Public repository graph: [`repository-relationships.json`](repository-relationships.json)
- Relationship guide: [`docs/REPOSITORY_RELATIONSHIPS.md`](docs/REPOSITORY_RELATIONSHIPS.md)
- Security reporting: [`SECURITY.md`](SECURITY.md)

GitHub applies only its documented fallback community files automatically. Agent instructions, relationship files, and reusable workflows are **not copied into sibling repositories**; repositories that need local enforcement must carry their own lowercase `agents.md` and explicitly call or copy the provided workflow.

`repository-relationships.json` retains the owner's existing contract. A generated public graph is staged under `.github-hardening/proposed/relationship-graph-v1/` for semantic compatibility review. It is public-safe: private repository names are omitted. The complete graph is synchronized separately to the approved private project registry.

## Safety baseline

Changes are pull-request driven. Contributors and agents must preserve concurrent work, avoid destructive Git operations, resolve conflicts semantically with full history and cross-repository context, validate affected contracts, and never claim a remote action completed without authoritative evidence.

Generated baseline version: `2026-08-04`.
<!-- ore-org-baseline:end -->
