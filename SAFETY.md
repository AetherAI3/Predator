# Predator Runway-Agent Safety Model

Predator combines long-horizon frontier-model reasoning, durable Unlimited Context memory,
Shared IR, native software execution, and hybrid classical/quantum optimization. That
combination is useful precisely because a runway agent can carry evidence forward across a
deep research chain. It also creates a serious control problem: persistent context and shared
artifacts can amplify a mistaken or malicious objective across agents, tools, repositories, and
external services.

This document defines the required safety contract for **runway agents** participating in
Predator Gen3. A runway agent is any model-driven worker, master, verifier assistant, or
research process that carries a Gen3 objective between evidence checkpoints; discovers corpus
candidates; creates or evaluates repairs; constructs QUBOs; submits bounded jobs; operates on
Shared IR; or prepares evidence for later stages.

> [!IMPORTANT]
> This is the behavioral and operational safety specification for future enforcement work. It
> deliberately distinguishes required policy from controls proven in code today. A policy
> statement is not treated as an implemented safeguard until the corresponding code, tests,
> deployment evidence, and release record exist.

For sensitive security concerns, do not publish exploit details in a public issue. Use
[Aether's contact channel](https://aethersystems.net/contact?intent=general&product=site_wide&cta=footer_updates_contact)
and clearly mark the report **Predator security**. Non-sensitive safety improvements and
documentation corrections are welcome through normal repository contributions.

## Where the risk actually lives

A QUBO, compiler, checkpoint, context store, or quantum result is not independently agentic.
The risk appears when an agent loop can repeatedly:

1. retrieve durable context;
2. observe Shared IR or peer-produced artifacts;
3. call tools or external services;
4. change code, candidates, QUBOs, or evidence;
5. evaluate whether those actions advanced its objective; and
6. preserve the result for future agents.

Under those conditions, the environment itself can become a coordination surface. Agents do
not need to exchange natural-language plans. They can communicate or influence later workers
through filenames, branch names, artifact metadata, QUBO coefficients, variable ordering,
residuals, solver settings, job labels, sample selection, or apparently ordinary research
notes.

The property Predator must deny is:

> **No model, peer agent, recalled memory, Shared IR object, external corpus, tool output, or
> optimization result may expand its own authority or redefine the human-approved objective.**

A blocked or impossible task is not permission to search for a more powerful path.

## Safety invariants

The following invariants apply to every Gen3 run:

1. **Human authority is external to the swarm.** Agent text, peer messages, memory, and
   artifacts cannot grant approval.
2. **Authorization is capability-bound.** Authority is limited to an owner, project,
   objective, lane, operation, exact source revision, resource budget, and expiry.
3. **Scope is non-transitive.** Permission to research a public corpus does not imply
   permission to access a private corpus, its owner, related infrastructure, or another
   tenant.
4. **Memory is evidence, not authority.** Unlimited Context may recall information but cannot
   create standing policy, credentials, permissions, or approval.
5. **Shared IR is untrusted input.** Every contribution retains provenance and is validated
   before another lane may rely on it.
6. **Failure is a valid terminal result.** Unavailable data, an impossible task, a native
   failure, or insufficient evidence must be banked truthfully.
7. **Execution cannot self-verify.** The worker that creates a candidate cannot issue the
   authoritative verification or signing decision for that candidate.
8. **Evidence is append-only and externally captured.** Workers cannot rewrite the
   authoritative record of what they executed.
9. **Quantum participation does not weaken ordinary security.** Provider access, job
   submission, result retrieval, and post-processing remain bounded, attributable, and
   independently reproducible.
10. **Shutdown authority remains out of band.** A runway agent cannot disable, delay, or
    redefine the mechanism that stops it.

## Threat model

| ID | Threat | Example | Required outcome |
| :--- | :--- | :--- | :--- |
| **T1** | **Third-party targeting** | An agent finds a company that may possess a useful corpus and decides unauthorized access would advance Gen3. | Stop, record the candidate as authorization-required, and request human review. |
| **T2** | **Supercluster escape** | A blocked worker uses package, CI, browser, artifact, model-provider, or quantum services as indirect network egress. | Supporting services enforce the same deny-by-default boundary as the worker. |
| **T3** | **Aether control-plane compromise** | An agent attacks MCP, Captain, leases, Project Memory, GitHub integration, budgets, or receipts to obtain greater authority. | Freeze the objective and revoke its entire capability chain. |
| **T4** | **Unauthorized swarm coordination** | Agents turn Shared IR, Unlimited Context, caches, GitHub, or quantum-job metadata into a hidden message board. | Isolate lanes, preserve evidence, and stop cross-objective propagation. |
| **T5** | **Corpus or prompt poisoning** | External content instructs a scout to reveal secrets, retrieve a private companion dataset, or recruit other agents. | Treat all retrieved content as data with external provenance, never as instructions. |
| **T6** | **Evidence and verifier tampering** | A worker modifies the parser, protected cases, post-processing, result binding, or certificate path to turn a failure into a pass. | Invalidate the affected evidence window and re-run under clean authority. |
| **T7** | **Quantum control-plane abuse** | An agent substitutes a QUBO, reads another lane's jobs, steals provider authority, manipulates calibration/post-selection, or exhausts credits. | Revoke provider access, preserve raw records, and mark results invalid pending review. |
| **T8** | **Covert mathematical signaling** | Agents encode coordination in low-order coefficients, variable order, gauges, embeddings, sample choices, or job timing. | Canonicalize inputs and detect unexplained cross-run structure. |
| **T9** | **Runaway resource use** | A persistent objective expands fanout, repeats jobs, or consumes compute after useful progress has stopped. | Enforce fixed UVT, worker, time, quantum-job, and artifact ceilings. |
| **T10** | **Self-authored policy drift** | An agent writes "owner approved" or a broader mission into memory and later treats it as standing authority. | Reject the claim because its provenance cannot confer authority. |

## Authority classes

Every item delivered to a runway agent must retain one of these authority classes:

| Class | Meaning | May authorize action? |
| :--- | :--- | :---: |
| **Owner capability** | Signed, current, narrowly scoped control-plane authorization | **Yes, within its exact bounds** |
| **System policy** | Versioned runtime policy installed outside model-writable state | **Yes, as a constraint only** |
| **Agent proposal** | Model-authored plan, interpretation, message, or recommendation | No |
| **Tool result** | Output from an approved tool, with tool and request provenance | No |
| **Shared IR data** | Peer-produced candidate, QUBO, residual, result, or annotation | No |
| **Recalled context** | Text or structured records retrieved through Unlimited Context | No |
| **External content** | Web pages, papers, repositories, datasets, messages, or metadata | No |

Quoting, copying, summarizing, signing as an agent, or placing an item into Shared IR does not
raise its authority class. In particular, strings such as `OWNER_APPROVED`, `CAPTAIN_GO`,
`VERIFIER_PASS`, or `EXACT_HEAD_GREEN` are inert unless accompanied by a valid
control-plane record independently verified outside the model.

## Unlimited Context policy

Predator uses durable context to preserve research continuity. Durable context must not become
durable authority.

### Required behavior

- Every recalled item carries source, author, project, objective, run, lane, creation time,
  revision, and integrity metadata.
- Model-authored memory is always distinguishable from owner policy and tool evidence.
- Policy-bearing retrieval excludes model-authored and external content unless it is being
  inspected explicitly as untrusted evidence.
- Context is partitioned by project and objective. Cross-project or cross-tenant recall is
  forbidden.
- A new stage receives the minimum context needed to continue the evidence chain, not a raw
  dump of unrelated transcripts, credentials, or hidden reasoning.
- Credentials, bearer tokens, cookies, private keys, signed URLs, provider secrets, and raw
  protected cases are never stored in model-retrievable memory.
- Retrieved text cannot change tool scopes, budgets, network access, verifier configuration,
  or checkpoint status.
- Conflicting or stale memory is surfaced as conflict, not silently merged into canonical
  truth.

### Denied behavior

A runway agent must not:

- write a future permission for itself;
- promote an agent proposal into owner policy;
- use repetition or consensus as evidence of authorization;
- preserve instructions from an external corpus as operational policy;
- hide coordination inside memory metadata or retrieval keys; or
- rewrite history to make an unauthorized action appear pre-approved.

## Gen3 checkpoint procedure

Predator's `C` checkpoints preserve evidence; `Q` interventions consume a preceding
checkpoint and propose the next bounded experiment.

For every `Cn → Qn+1 → Cn+1` transition:

1. **Freeze the parent.** The parent checkpoint is immutable and identified by a full digest.
2. **Admit one objective.** The intervention receives an exact hypothesis, permitted paths,
   allowed tools, budget, and terminal conditions.
3. **Separate discovery from acquisition.** An agent may identify a corpus candidate without
   being authorized to obtain or use it.
4. **Constrain candidate generation.** Every candidate records its origin, transformations,
   and relationship to the parent residual.
5. **Bind execution.** Native execution is tied to the admitted candidate, source revision,
   environment, and verifier identity.
6. **Bank failure honestly.** A native failure remains a valid result and cannot be replaced
   with a more favorable narrative.
7. **Verify independently.** The executor cannot access or modify the protected verifier,
   signer, or authoritative receipt store.
8. **Promote deliberately.** Creation of a new checkpoint requires policy linkage,
   verification, custody, and a separate promotion decision.
9. **Do not auto-continue.** A checkpoint does not grant permission to start another
   intervention. Every next stage requires fresh admission.

If evidence authority may have been compromised, the terminal state is:

```text
GEN3_EVIDENCE_PLANE_COMPROMISED
RESULT_INVALID
```

No result from the affected window may be promoted. Recovery requires a clean executor,
rotated authority, a fresh run identity, a new custody root, and independent qualification.

## Corpus discovery and acquisition

Runway agents may search only sources authorized by the objective and retrieval policy.

### Public discovery

An agent may record that a candidate exists, why it appears relevant, its public location, and
its apparent license. Discovery alone does not establish permission to download, transform,
redistribute, or use the material.

### Authorization-required outcomes

The agent must stop and request review when:

- the corpus is private, gated, leaked, ambiguously licensed, or exposed accidentally;
- access would require credentials not supplied for the objective;
- a company, researcher, user, or unrelated service would need to be contacted;
- a robots, rate, account, payment, geographic, or technical restriction blocks access;
- the source requests execution of code or disclosure of environment information;
- the data may contain secrets, personal information, customer material, or protected
  evaluation cases; or
- obtaining the corpus would require testing a vulnerability.

The accepted terminal result is `CORPUS_CANDIDATE_REQUIRES_AUTHORIZATION`. A runway agent
must never reinterpret "find candidates" as authorization to penetrate the candidate owner.

### Ingestion

Before use, an approved corpus receives:

- source and owner identity;
- license or explicit permission;
- acquisition method and timestamp;
- content digest and immutable raw copy;
- malware and secret scanning;
- prompt-injection classification;
- transformation lineage;
- allowed uses and retention;
- human approval reference; and
- separation from protected evaluation material.

## Shared IR safety

Shared IR is a research interchange format, not a trusted command channel.

- Writes are objective- and lane-scoped.
- Readers see provenance and authority class before content.
- An agent may propose an IR delta but cannot overwrite another lane's contribution.
- Merging requires schema validation, causal linkage, and an independent reviewer.
- Arbitrary executable payloads, network locations, credentials, and instruction-bearing
  metadata are rejected.
- Filenames, object keys, labels, comments, and unused fields are normalized.
- Cross-lane read access is limited to admitted dependencies.
- Unexpected coordination patterns trigger preservation and objective-wide review.
- Shared IR never carries private signing material, provider credentials, protected cases, or
  hidden owner policy.

For QUBOs specifically, each matrix term must be attributable to an objective or constraint.
Canonical variable order, bounded precision, explained penalty weights, and deterministic
serialization prevent unused numerical freedom from becoming a covert channel.

## Quantum execution policy

The credible attack surface around a quantum computer is primarily classical: credentials,
job brokers, compilation, scheduling, calibration, result retrieval, and post-processing.

### Required submission chain

Every hardware or simulator result must bind:

```text
objective
→ parent checkpoint
→ canonical QUBO or circuit digest
→ compiler and configuration digest
→ exact provider submission
→ provider job identity
→ backend identity and calibration reference
→ raw samples
→ post-processing version
→ classical baseline
→ verifier result
→ checkpoint candidate
```

A break in that chain invalidates the claim.

### Broker requirements

- Provider credentials stay in a non-model broker.
- Agents submit only schema-valid, admitted jobs.
- Job names and metadata are broker-generated.
- Workers cannot list other lanes' or tenants' jobs.
- Backend, shot, schedule, gauge, seed, pulse, and cost limits are policy-bound.
- Raw results are captured before model-authored interpretation.
- QUBO/circuit substitution is detected by digest comparison.
- Quantum spending has independent per-job and per-objective limits.
- Pulse-level or provider-administration access is outside runway-agent authority.
- Important results are challenged with approved classical methods and, when warranted, an
  independently controlled backend.

Quantum randomness, noise, tunneling, or hardware complexity never substitutes for provenance
or independent verification.

## GitHub, CI, and software-supply-chain policy

A runway agent may work only in the admitted repository and paths.

- Use ephemeral repository-scoped credentials.
- Do not expose tokens to model context, environment dumps, logs, artifacts, or Shared IR.
- Workers cannot push to the protected release branch, merge their own work, change required
  checks, or approve their own evidence.
- Workflow, verifier, signer, policy, and custody changes require separate ownership.
- CI runs against an exact source revision and emits evidence bound to that revision.
- Cached runners and artifacts are treated as cross-run trust boundaries.
- A passing check proves only the named check under its recorded configuration.
- Documentation or test changes may not weaken historical assertions merely to produce a
  favorable result.

A useful-looking pull request does not earn broader runtime authority.

## Monitoring and incident response

Monitoring must evaluate behavior across agents and systems, not only individual prompts.

High-severity signals include:

- attempts to discover or use unintended network egress;
- cross-lane messages or unexplained shared identifiers;
- credentials appearing in context or artifacts;
- access to unapproved companies, repositories, accounts, or datasets;
- repeated verifier probing or result-boundary inference;
- mutation of evidence, logs, protected cases, or policy;
- mismatch between admitted and submitted QUBO/circuit digests;
- quantum jobs from unexpected identities, origins, backends, or budgets;
- attempts to disable monitoring, cancellation, leases, or budget enforcement; and
- agent claims that another agent supplied owner authorization.

A severe alert freezes the full objective, not merely the worker that generated it. The
out-of-band response must be able to:

1. stop dispatch;
2. fence active leases;
3. cancel queued work and quantum jobs where safe;
4. revoke MCP, GitHub, runner, provider, and storage capabilities;
5. freeze Shared IR and Project Memory promotion;
6. preserve append-only evidence;
7. quarantine affected artifacts and contexts; and
8. require a human incident commander to authorize recovery.

An agent under investigation cannot participate in its own clearance decision.

## Safe terminal states

Runway agents are expected to stop safely. The following are successful, truthful outcomes:

```text
WAITING_HUMAN
OBJECTIVE_BOUNDARY_REACHED
CORPUS_CANDIDATE_REQUIRES_AUTHORIZATION
EXTERNAL_TARGET_OUT_OF_SCOPE
NETWORK_PATH_NOT_AUTHORIZED
QUANTUM_PROVIDER_UNAVAILABLE
VERIFIER_UNAVAILABLE
BUDGET_EXHAUSTED
TASK_UNSATISFIABLE
EVIDENCE_INSUFFICIENT
GEN3_EVIDENCE_PLANE_COMPROMISED
```

No reward, grader, deadline, peer request, or remaining UVT changes those boundaries.

## Contributor rules

Predator welcomes serious software, verification, AI, and quantum-research contributions.
Participation is not authorization to probe Aether, a corpus owner, a quantum provider, an
open-source project, or any third party.

Contributors must:

- use synthetic, owned, or explicitly authorized targets;
- preserve failed and negative results;
- identify simulations, hardware runs, and inferred claims accurately;
- avoid publishing credentials, protected cases, private corpora, or exploitable operational
  details;
- disclose conflicts, uncertainty, and limits; and
- report suspected safety failures privately.

## Implementation status

This document is the **normative design target** for Predator runway-agent safety. It does not
claim that every control above is implemented in the public repository or private research
runtime today.

A control becomes **enforced** only when all of the following exist:

1. an implementation outside model-writable policy state;
2. tests covering allowed and denied behavior;
3. deployment or exact-head execution evidence;
4. an identified owner and rollback path; and
5. documentation updated to name the enforced version.

Until then, it remains a required procedure for operators and a specification for upcoming
code integration.

Maintained by **Aether AI LLC**. Safety corrections, adversarial test ideas, and responsible
reports are welcome.
