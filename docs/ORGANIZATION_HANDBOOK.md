# fanwaave organization handbook

> Shared operating defaults for repositories maintained under **fanwaave**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

fanwaave maintains fan, community, and audience-engagement software. This `.github` repository is the canonical home for organization-wide community health files, reusable templates, engineering policy, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported environments, development and test commands, authoritative interfaces, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Audience-facing components should also document moderation, privacy, consent, rate limits, notification behavior, retries, analytics boundaries, and degraded modes.

## Change and review workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, risk, validation, compatibility, migration, and rollback.
4. Test success, failure, duplicate, timeout, permission, and abuse paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence and quality

Pull requests should include reproducible commands, environments, expected and observed results, negative-path coverage, documentation updates, and CI or local-equivalent evidence. Breaking changes require consumer analysis, versioning, migration guidance, and rollback.

## Security and data

Never commit credentials, customer or community data, provider tokens, private keys, or sensitive logs. Follow `SECURITY.md` for private vulnerability reporting. Pin dependencies, actions, containers, and generated inputs where supply-chain integrity or reproducibility matters.

## Documentation and decisions

Keep examples executable, links current, assumptions explicit, and repository boundaries clear. Record architectural, provider, compatibility, privacy, consent, moderation, and operational decisions that future maintainers would otherwise have to rediscover.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profile, descriptions, topics, and READMEs are current.
- [ ] Contribution, security, support, governance, issue, and PR guidance is present.
- [ ] Required checks reflect current delivery and security risk.
- [ ] Stale repositories are archived or explicitly marked.
- [ ] Project links resolve and completed work is reflected in GitHub and Linear.
- [ ] Shared workflows and templates are versioned, tested, and backwards compatible.
