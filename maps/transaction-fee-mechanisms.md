---
topic: Transaction fee mechanism (TFM) design
purpose: "Orientation: see the research directions before choosing a first lesson. Assumed, not yet confirmed by the learner."
date: 2026-11-21
sources:
  roughgarden-2021: {ref: "arXiv:2106.01340", title: "Transaction Fee Mechanism Design"}
  roughgarden-2020: {ref: "arXiv:2012.00854", title: "Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559"}
  chung-shi-2021: {ref: "arXiv:2111.03151", title: "Foundations of Transaction Fee Mechanism Design"}
  chung-roughgarden-shi-2024: {ref: "arXiv:2402.09321", title: "Collusion-Resilience in Transaction Fee Mechanism Design"}
  ganesh-thomas-weinberg-2024: {ref: "arXiv:2410.07566", title: "Revisiting the Primitives of Transaction Fee Mechanism Design"}
  ferreira-2021: {ref: "arXiv:2103.14144", title: "Dynamic Posted-Price Mechanisms for the Blockchain Transaction Fee Market"}
  crapis-moallemi-wang-2023: {ref: "arXiv:2309.12735", title: "Optimal Dynamic Fees for Blockchain Resources"}
  diamandis-2022: {ref: "arXiv:2208.07919", title: "Dynamic Pricing for Non-fungible Resources: Designing Multidimensional Blockchain Fee Markets"}
  kiayias-2025: {ref: "arXiv:2506.13271", title: "One-dimensional vs. Multi-dimensional Pricing in Blockchain Protocols"}
  garimidi-heimbach-roughgarden-2025: {ref: "arXiv:2505.17885", title: "Transaction Fee Mechanism Design for Leaderless Blockchain Protocols"}
  acilan-2025: {ref: "arXiv:2502.11964", title: "Transaction Fee Market Design for Parallel Execution"}
  tang-zhang-2023: {ref: "arXiv:2302.06769", title: "Transaction Fee Mining and Mechanism Design"}
  anchuri-mamageishvili-2026: {ref: "arXiv:2606.13555", title: "Price Elasticity of Gas Demand on L1 and L2: Evidence from Ethereum and Arbitrum"}
---
> **How far this map was checked.** On 2026-11-22 the title, authors and
> abstract of each paper under `sources` were opened through the arXiv API, so
> the papers exist and are about what the branch says. Only sections 2 and 3
> of `roughgarden-2021` were read in full. The split into eight branches is
> still the agent's own; no survey was read to confirm it.

## Branches

- [ ] **1. Incentive properties** [source-exists: roughgarden-2021]
  Question: which participants can a fee mechanism be made robust against, and can it be robust against all of them at once?
  Needs: what a block producer does; basic auction ideas (first-price auction, incentive compatibility).
  Lesson: lessons/0001-tfm-incentive-properties.md (in progress)

- [ ] **2. Relaxing the model** [source-exists: ganesh-thomas-weinberg-2024]
  Question: if no mechanism can have every desired property, which assumptions can be weakened to get around that?
  Needs: branch 1.
  Lesson: (none yet)

- [ ] **3. Price dynamics** [source-exists: ferreira-2021]
  Question: when the protocol posts a price instead of running an auction, how should that price move from block to block, and does it settle?
  Needs: branch 1 helps; a little control or optimisation intuition.
  Lesson: (none yet)

- [ ] **4. Multidimensional fees** [source-exists: diamandis-2022]
  Question: should different resources (computation, storage, data) have separate prices instead of one fee?
  Needs: branch 3.
  Lesson: (none yet)

- [ ] **5. MEV and the block-building pipeline** [model-only]
  Question: what changes when the block producer earns from ordering transactions, and when building and proposing a block are done by different parties?
  Needs: branch 1; what MEV is.
  Lesson: (none yet)

- [ ] **6. Protocol architecture** [source-exists: garimidi-heimbach-roughgarden-2025]
  Question: the standard model has one block producer per block; what changes for leaderless protocols or parallel execution?
  Needs: branch 1; consensus basics.
  Lesson: (none yet)

- [ ] **7. Mining incentives under fee revenue** [source-exists: tang-zhang-2023]
  Question: when fees, not the block subsidy, pay the block producers, which attacks on the chain itself become profitable?
  Needs: how Bitcoin mining rewards work.
  Lesson: (none yet)

- [ ] **8. Empirical studies** [source-exists: anchuri-mamageishvili-2026]
  Question: what do on-chain data show about how deployed fee mechanisms and their users actually behave?
  Needs: whichever branch the study tests; on-chain data handling.
  Lesson: (none yet)

## Suggested order

Start with branch 1. It supplies the vocabulary (who the parties are and what
each can do) that every other branch uses. Then branch 3, which is the part of
a deployed mechanism you can see directly in data. After that, choose by
purpose: branches 7 and 8 are closest to Bitcoin data analytics; branches 2, 5
and 6 are the theory frontier; branch 4 matters mostly for Ethereum.

## Papers by branch

- Branch 1: roughgarden-2021, roughgarden-2020, chung-shi-2021, chung-roughgarden-shi-2024
- Branch 2: chung-roughgarden-shi-2024, ganesh-thomas-weinberg-2024
- Branch 3: roughgarden-2020, ferreira-2021, crapis-moallemi-wang-2023
- Branch 4: crapis-moallemi-wang-2023, diamandis-2022, kiayias-2025
- Branch 5: none opened. The branch stays `model-only`.
- Branch 6: garimidi-heimbach-roughgarden-2025, acilan-2025
- Branch 7: tang-zhang-2023
- Branch 8: anchuri-mamageishvili-2026

Reading guide for roughgarden-2021: `guides/2106.01340.md`.
