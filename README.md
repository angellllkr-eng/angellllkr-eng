<p align="center">
  <img src="https://raw.githubusercontent.com/angellllkr-eng/angellllkr-eng/main/avatar.svg" width="80" height="80" alt="MindReply" />
</p>

<p align="center">
  <strong>Angel K — MindReply Ecosystem</strong>
</p>

---

## 🎯 Canonical Repository

All active development is consolidated in the **unified canonical monorepo**:

### ⭐ [mind-reply-core](https://github.com/angellllkr-eng/mind-reply-core)

**Official source of truth** for the MindReply platform and all branded surfaces.

- **MindReply Core:** [mindreply.com](https://mindreply.com) — Central intelligence platform
- **A11-K Surface:** [a11-k.space](https://a11-k.space) — Voice-first AI companion
- **Experimental:** Design studio (Brushworks), Business engine (Forge)
- **Infrastructure:** AEGIS control plane (Nexus Core)

---

## 📊 Estate Overview

| Component | Status | Location |
|-----------|--------|----------|
| **MindReply Core Platform** | ✅ Production | `mind-reply-core/apps/web-replycontrol/` |
| **A11-K Branded Surface** | ✅ Production | `mind-reply-core/apps/a11k/` |
| **RWA Bridge (Python)** | ✅ Production | `mind-reply-core/services/rwa-bridge/` |
| **Brushworks (Design Studio)** | 🚀 Staging | `mind-reply-core/apps/experimental/brushworks/` |
| **Forge (Scaffolding)** | 🚀 Staging | `mind-reply-core/apps/experimental/forge/` |
| **Nexus Control Plane** | ✅ Internal | `mind-reply-core/infrastructure/nexus/` |

---

## 🏗️ Architecture

**Monorepo structure:**
```
mind-reply-core/
├── apps/                    # Consumer products
│   ├── web-replycontrol/   # Core UI (mindreply.com)
│   ├── a11k/               # A11-K UI (a11-k.space)
│   ├── marketing/          # Landing pages
│   └── experimental/       # Staging for new products
├── services/               # Backend services
│   └── rwa-bridge/        # Python RWA engine
├── infrastructure/         # Internal systems
│   └── nexus/             # Orchestration
└── docs/                   # Documentation
```

**Deployment topology:**
- **mindreply.com** → Docker (self-hosted or cloud)
- **a11-k.space** → Vercel (serverless)
- **Shared backend** → PostgreSQL + Redis

---

## 🚀 Quick Links

- **Documentation:** [mind-reply-core/docs](https://github.com/angellllkr-eng/mind-reply-core/tree/main/docs)
- **Architecture:** [ARCHITECTURE.md](https://github.com/angellllkr-eng/mind-reply-core/blob/main/docs/ARCHITECTURE.md)
- **Deployment:** [DEPLOYMENT.md](https://github.com/angellllkr-eng/mind-reply-core/blob/main/docs/DEPLOYMENT.md)
- **Troubleshooting:** [TROUBLESHOOTING.md](https://github.com/angellllkr-eng/mind-reply-core/blob/main/docs/TROUBLESHOOTING.md)

---

## 📦 Archived Repos

The following repos have been consolidated into `mind-reply-core`:

| Repo | Status | Why |
|------|--------|-----|
| `a11k-surface` | Merged | Now `mind-reply-core/apps/a11k/` |
| `brushworks` | Merged | Now `mind-reply-core/apps/experimental/brushworks/` |
| `forge` | Merged | Now `mind-reply-core/apps/experimental/forge/` |
| `nexus-core` | Merged | Now `mind-reply-core/infrastructure/nexus/` |
| `chatbot` | Archived | Superseded by A11-K surface |
| `chatbot1` | Archived | Duplicate (removed) |
| `agent-control-plane` | Archived | Replaced by Nexus Core |
| `linear-card-interaction` | Archived | R&D only |

---

## 🔗 Brand Ecosystem

| Brand | Purpose | Status |
|-------|---------|--------|
| **MindReply** | Intelligence infrastructure & owner-system | Production |
| **A11-K** | Voice-first AI companion engine | Production |
| **AUREL** | Luxury AI lifestyle & visual trust standard | Planning |
| **AM Service** | Automotive service portal | Planned |
| **Asset Forge** | Portfolio experimentation | Experimental |

---

## 📝 License

Proprietary © MindReply. All rights reserved.

---

**Last Updated:** 2026-08-05  
**Maintainer:** Angel Krastev
