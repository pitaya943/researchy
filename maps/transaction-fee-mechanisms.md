---
topic: Transaction fee mechanism (TFM) design
purpose: "先看全貌:在選第一堂課之前了解有哪些研究方向。這是 agent 的假設,學習者尚未確認。"
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
> **這張地圖查證到什麼程度。** 2026-11-22 透過 arXiv API 開啟了 `sources` 中每篇論文的標題、作者與摘要,所以這些論文確實存在,主題也與所屬方向相符。只有 `roughgarden-2021` 的第 2、3 節被完整讀過。分成八個方向仍是 agent 自己的劃分,沒有讀過任何 survey 來確認。

## 方向

- [ ] **1. 誘因性質(incentive properties)** [source-exists: roughgarden-2021]
  問題:一個手續費機制能防住哪些參與者?能同時防住全部嗎?
  需要:出塊者在做什麼;基本的拍賣概念(first-price auction、incentive compatibility)。
  Lesson:lessons/0001-tfm-incentive-properties.md(進行中)

- [ ] **2. 放寬模型** [source-exists: ganesh-thomas-weinberg-2024]
  問題:如果沒有機制能同時擁有所有想要的性質,可以放寬哪些假設來繞過?
  需要:方向 1。
  Lesson:(尚無)

- [ ] **3. 價格動態** [source-exists: ferreira-2021]
  問題:當協定直接公告價格而不是辦拍賣時,這個價格該如何逐區塊調整?它會穩定下來嗎?
  需要:方向 1 有幫助;一點控制或最佳化的直覺。
  Lesson:(尚無)

- [ ] **4. 多維費用** [source-exists: diamandis-2022]
  問題:不同的資源(運算、儲存、資料)應該分開定價,而不是共用一個費用嗎?
  需要:方向 3。
  Lesson:(尚無)

- [ ] **5. MEV 與出塊流程** [model-only]
  問題:當出塊者能從交易排序獲利,以及組裝區塊與提出區塊由不同角色負責時,什麼會改變?
  需要:方向 1;MEV 是什麼。
  Lesson:(尚無)

- [ ] **6. 協定架構** [source-exists: garimidi-heimbach-roughgarden-2025]
  問題:標準模型假設每個區塊只有一個出塊者。對 leaderless 協定或平行執行,什麼會改變?
  需要:方向 1;共識機制的基礎。
  Lesson:(尚無)

- [ ] **7. 以手續費為主的挖礦誘因** [source-exists: tang-zhang-2023]
  問題:當出塊者的收入主要來自手續費而不是區塊補貼時,哪些針對鏈本身的攻擊會變得有利可圖?
  需要:Bitcoin 的挖礦獎勵如何運作。
  Lesson:(尚無)

- [ ] **8. 實證研究** [source-exists: anchuri-mamageishvili-2026]
  問題:鏈上資料顯示,已上線的手續費機制與使用者實際上如何運作?
  需要:該研究所檢驗的那個方向;鏈上資料處理。
  Lesson:(尚無)

## 建議順序

先學方向 1。它提供其他方向都會用到的詞彙(有哪些參與者、各自能做什麼)。接著學方向 3,這是已上線機制中你能直接在資料裡看到的部分。之後依目的選擇:方向 7、8 最接近 Bitcoin 資料分析;方向 2、5、6 是理論前沿;方向 4 主要與 Ethereum 有關。

## 各方向的論文

- 方向 1:roughgarden-2021、roughgarden-2020、chung-shi-2021、chung-roughgarden-shi-2024
- 方向 2:chung-roughgarden-shi-2024、ganesh-thomas-weinberg-2024
- 方向 3:roughgarden-2020、ferreira-2021、crapis-moallemi-wang-2023
- 方向 4:crapis-moallemi-wang-2023、diamandis-2022、kiayias-2025
- 方向 5:沒有開啟過任何論文,所以維持 `model-only`。
- 方向 6:garimidi-heimbach-roughgarden-2025、acilan-2025
- 方向 7:tang-zhang-2023
- 方向 8:anchuri-mamageishvili-2026

roughgarden-2021 的閱讀指南:`guides/2106.01340.md`。
