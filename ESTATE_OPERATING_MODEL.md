# A.K. Estate Operating Model

## Separation of concerns

**Personal:** private context, self-development, personal goals, private notes, owner decisions.

**Products:** customer-facing applications and commercial assets.

**Operations:** release, monitoring, security, evidence, recovery, and automation.

**Experiments:** disposable research that must earn promotion into a canonical product.

## Naming principle

A repository name is an address. A product name should explain the human outcome. Internal agent names should explain responsibility and boundary. Avoid a single repeated vocabulary across unrelated surfaces.

## Owner communication

The preferred monitoring model is event-driven:

`system event -> policy filter -> severity -> owner notification -> acknowledgement -> proof`

Recommended notification classes:

- critical: immediate;
- important: batched hourly;
- routine: daily digest;
- informational: dashboard only.

No automation should infer permission to contact the owner through a new channel. The channel must be explicitly configured and tested.

## Domain policy

Use canonical product domains for public products. Avoid proliferating subdomains merely to represent internal components. Internal tools may use private deployment URLs or access-controlled routes until a public domain has a clear user purpose.

## Compliance posture

Maintain an inventory of data categories, processors, retention periods, access roles, consent/notice requirements, incident procedures, terms, privacy notice, cookie policy where applicable, and processor agreements. Do not claim certification unless independently obtained and current.
