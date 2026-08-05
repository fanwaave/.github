# Fanwaave marketing site

Complete Astro source staged for the future public repository `fanwaave/fanwaave.github.io` and URL `https://fanwaave.github.io/`.

## Canonical planning

- Linear project: `github.com/fanwaave`
- GitHub Project: [fanwaave project #1](https://github.com/orgs/fanwaave/projects/1)
- Organization: [fanwaave](https://github.com/fanwaave)

## Product context

Fanwaave is being positioned as an audience-signal and campaign-moment platform: ingest consented audience events, normalize identities and channels, deduplicate moments, score relevance, route time-sensitive opportunities, and expose observable delivery outcomes.

There is not yet a public `fanwaave-clients` repository. The TypeScript, curl, event-document, and webhook examples are therefore labeled as an **API preview**, not released SDKs. Payloads must be reconciled with the final public interface contract before production publication.

## Publish

1. Create public repository `fanwaave.github.io` in the `fanwaave` organization.
2. Copy this directory to the new repository root.
3. Run `npm install && npm run build`.
4. Add the standard Astro GitHub Pages workflow and enable GitHub Actions as the Pages source.
5. Verify `https://fanwaave.github.io/` and update the linked GitHub and Linear tickets.
