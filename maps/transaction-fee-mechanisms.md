---
topic: Transaction fee mechanism (TFM) design
purpose: "Orientation: see the research directions before choosing a first lesson. Assumed, not yet confirmed by the learner."
date: 2026-11-21
sources: {}
---
> **No source was opened for this map.** arXiv could not be reached from the
> session when it was written. Every branch below is `model-only`: the layout
> is the agent's own, cross-read against web-search result summaries. The
> papers under "Unopened leads" were seen in search results only.

## Branches

- [ ] **1. Incentive properties** [model-only]
  Question: which participants can a fee mechanism be made robust against, and can it be robust against all of them at once?
  Needs: what a block producer does; basic auction ideas (first-price auction, incentive compatibility).
  Lesson: lessons/0001-tfm-incentive-properties.md (in progress)

- [ ] **2. Relaxing the model** [model-only]
  Question: if no mechanism can have every desired property, which assumptions can be weakened to get around that?
  Needs: branch 1.
  Lesson: (none yet)

- [ ] **3. Price dynamics** [model-only]
  Question: when the protocol posts a price instead of running an auction, how should that price move from block to block, and does it settle?
  Needs: branch 1 helps; a little control or optimisation intuition.
  Lesson: (none yet)

- [ ] **4. Multidimensional fees** [model-only]
  Question: should different resources (computation, storage, data) have separate prices instead of one fee?
  Needs: branch 3.
  Lesson: (none yet)

- [ ] **5. MEV and the block-building pipeline** [model-only]
  Question: what changes when the block producer earns from ordering transactions, and when building and proposing a block are done by different parties?
  Needs: branch 1; what MEV is.
  Lesson: (none yet)

- [ ] **6. Protocol architecture** [model-only]
  Question: the standard model has one block producer per block; what changes for leaderless protocols or parallel execution?
  Needs: branch 1; consensus basics.
  Lesson: (none yet)

- [ ] **7. Mining incentives under fee revenue** [model-only]
  Question: when fees, not the block subsidy, pay the block producers, which attacks on the chain itself become profitable?
  Needs: how Bitcoin mining rewards work.
  Lesson: (none yet)

- [ ] **8. Empirical studies** [model-only]
  Question: what do on-chain data show about how deployed fee mechanisms and their users actually behave?
  Needs: whichever branch the study tests; on-chain data handling.
  Lesson: (none yet)

## Suggested order

Start with branch 1. It supplies the vocabulary (who the parties are and what
each can do) that every other branch uses. Then branch 3, which is the part of
a deployed mechanism you can see directly in data. After that, choose by
purpose: branches 7 and 8 are closest to Bitcoin data analytics; branches 2, 5
and 6 are the theory frontier; branch 4 matters mostly for Ethereum.

## Unopened leads

Titles and identifiers as shown in web-search results on 2026-11-21. None was opened.

- arXiv:2106.01340 "Transaction Fee Mechanism Design" (branch 1)
- arXiv:2012.00854 "Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559" (branches 1, 3)
- arXiv:2111.03151 "Foundations of Transaction Fee Mechanism Design" (branch 1)
- arXiv:2402.09321 "Collusion-Resilience in Transaction Fee Mechanism Design" (branches 1, 2)
- arXiv:2410.07566 "Revisiting the Primitives of Transaction Fee Mechanism Design" (branches 2, 5)
- arXiv:2103.14144 "Dynamic Posted-Price Mechanisms for the Blockchain Transaction-Fee Market" (branch 3)
- arXiv:2309.12735 "Optimal Dynamic Fees for Blockchain Resources" (branches 3, 4)
- arXiv:2208.07919 "Dynamic Pricing for Non-fungible Resources: Designing Multidimensional Blockchain Fee Markets" (branch 4)
- arXiv:2506.13271 "One-dimensional vs. Multi-dimensional Pricing" (branch 4)
- arXiv:2505.17885 "Transaction Fee Mechanism Design for Leaderless Blockchain Protocols" (branch 6)
- arXiv:2502.11964 "Transaction Fee Market Design for Parallel Execution" (branch 6)
- arXiv:2302.06769 "Transaction Fee Mining and Mechanism Design" (branches 1, 7; search results describe it as a survey)
- arXiv:2606.13555 "Price Elasticity of Gas Demand on L1 and L2: Evidence from Ethereum and Arbitrum" (branch 8)
