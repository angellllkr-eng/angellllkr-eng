# A.K. Personal GitHub Estate Registry

**Purpose:** one readable operating map for current and future agents.

## Authority

- **Personal account:** `angellllkr-eng`
- **MindReply product authority:** `Mind-Reply/mindreply`
- **Personal operational authority:** `angellllkr-eng/agent-control-plane`
- **Reconciliation authority:** `angellllkr-eng/estate-reconciliation`
- **Default active branch:** `main`
- **Rule:** do not create a second repository for an existing function without recording the reason and canonical relationship here.

## Canonical lanes

| Lane | Canonical repository | Status | Function |
|---|---|---|---|
| MindReply Product | `Mind-Reply/mindreply` | CANONICAL | Product/runtime source |
| Operations | `angellllkr-eng/agent-control-plane` | CANONICAL | Owner control, evidence, release and recovery |
| ResellerPro | `angellllkr-eng/resellerpro-platform` | CANONICAL CANDIDATE | Commerce/provisioning platform |
| A11 Systems | `angellllkr-eng/a11-enterprise` | CANONICAL CANDIDATE | Owner systems / advanced platform work |
| A11 Retrieval | `angellllkr-eng/a11-rag-platform` | ACTIVE MODULE | Retrieval/RAG |
| A11 Orchestration | `angellllkr-eng/a11k-orchestration` | ACTIVE MODULE | Orchestration |
| Registrar | `angellllkr-eng/registrar-control-plane` | ACTIVE MODULE | Registrar/domain control |
| Runtime | `angellllkr-eng/own` | ACTIVE | Reusable execution system |
| Runtime Agent | `angellllkr-eng/own-agent` | ACTIVE | Agent-specific runtime |
| Estate Ops | `angellllkr-eng/estate-reconciliation` | CANONICAL | Consolidation/evidence |

## Public/product surfaces

- `angellllkr-eng/a11-homepage` — public A11 homepage
- `angellllkr-eng/a11-evidence-surface` — public evidence surface
- `angellllkr-eng/mindreply-org-site` — MindReply organization/site surface
- `angellllkr-eng/enterprise-engine-radar` — research/strategy surface
- `angellllkr-eng/NEW-SIGNAL-check` — signal/check project
- `angellllkr-eng/burning-heart-launcher` — launcher project

## Technical/reusable

- `chrome-devtools-mcp` — browser/devtools integration
- `slack-github-action` — GitHub/Slack integration
- `PA-tech` — personal-agent technical system
- `megaagent-pc-studio` — workstation/lab project
- `openmontage` — large creative/source system
- `openmontage-source-mirror` — source mirror; keep separate unless provenance proves consolidation

## Templates / prototypes

- `brushworks` — UI/site construction source
- `saas-starter` — starter/template
- `eve-chat-template` — canonical Eve template
- `kody-eve-template` — separate/empty candidate; do not treat as canonical until content exists
- `nextjs-boilerplate` — canonical Next.js boilerplate
- `copy-of-a11-k-command-center` — prototype/copy; not a canonical runtime

## Duplicate / retirement register

These are **not** new production roots. They remain only until GitHub administration or a verified migration permits final retirement.

| Repository | Disposition | Canonical replacement |
|---|---|---|
| `chatbot1` | RETIRE / duplicate | `chatbot` (already archived) |
| `eve-chat-1` | RETIRE / duplicate | `eve-chat-template` |
| `nextjs1` | RETIRE / duplicate | `nextjs-boilerplate` |
| `hill-monarch-quiet-glade-project` | RETIRE / duplicate | `hill-monarch-quiet-glade` |
| `mind-repl` | RETIRE / empty/duplicate candidate | none until proven useful |
| `Own1` | RETIRE / empty duplicate candidate | `own` |
| `source1` | RETIRE / empty | none |
| `source2` | RETIRE / empty | none |

Previously archived historical repositories remain preserved and are not reopened merely to reduce repository count.

## Deliberately separate

- `a11-k-multiverse` and `a11-k-multiverse-5d` — retain until functionality comparison proves overlap.
- `mindreply` — personal legacy migration archive; canonical product is `Mind-Reply/mindreply`.
- `mind-reply-core` — archived provenance/rollback source; not production.
- `resellerpro-platform` and `reseller-pro-enterprise` — retain until architecture/deployment provenance proves one can retire.
- `own` and `own-agent` — separate runtime layers.
- `openmontage` and `openmontage-source-mirror` — separate provenance/source roles.

## Branch standard

Use `main` as the canonical integration branch for active repositories.

Use short-lived branches with one purpose:

- `feat/<scope>`
- `fix/<scope>`
- `ops/<scope>`
- `docs/<scope>`
- `reconcile/<scope>`
- `release/<version>`

Do not create permanent branches such as `final`, `latest`, `new`, `copy`, `backup`, `ready`, or `production`.

If a repository still uses `master`, create/verify `main` first and treat `master` as a migration alias until GitHub repository administration can change the default branch safely.

## Agent operating contract

1. Read this registry before creating or modifying a repository.
2. Locate the canonical repository before implementing a feature.
3. Inspect README, manifests, entrypoints, workflows, deployment configuration and recent commits.
4. Prefer a reversible change on a dedicated branch.
5. Never merge duplicate implementations by name alone.
6. Never delete or archive until unique files, deployment bindings and provenance are verified.
7. Verify runtime state before claiming live/production.
8. Record important changes in the canonical operations/reconciliation repository.

## Status vocabulary

`VERIFIED` · `READY` · `BLOCKED` · `FAILED` · `UNVERIFIED`

## Last reconciliation

2026-09-13 — personal account inventory reviewed and this registry established. GitHub connector currently does not expose repository-administration operations for rename/archive/default-branch changes, so those platform mutations are recorded as controlled follow-up actions rather than falsely marked complete.
