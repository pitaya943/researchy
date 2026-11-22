---
candidate: ifc-bounded-declassification
date: 2026-11-22
verdict: undecided
sources:
  camel: {ref: "arXiv:2503.18813", title: "Defeating Prompt Injections by Design"}
  agentdojo: {ref: "arXiv:2406.13352", title: "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"}
  rtbas: {ref: "arXiv:2502.08966", title: "RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage"}
  appa: {ref: "arXiv:2607.24625", title: "APPA: Recoverable Information-Flow Control for Real-World LLM Agents"}
  limits: {ref: "arXiv:2611.10395", title: "The Limits of Information-Flow Control Enforcement for Agentic Systems"}
  planters: {ref: "arXiv:2611.11506", title: "On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents"}
  llmbda: {ref: "arXiv:2602.20064", title: "The LLMbda Calculus: AI Agents, Conversations, and Information Flow"}
  gif: {ref: "arXiv:2606.23277", title: "GIF: Locally Sound Geometric Information Flow Control for LLMs"}
  autonomy: {ref: "arXiv:2602.11416", title: "Optimizing Agent Planning for Security and Autonomy"}
---
# 有界洩漏的降級:讓資訊流控制的 LLM agent 不再過度封鎖

本頁開啟了 9 篇的摘要,並在 camel、planters、limits 三篇的內文裡搜尋了關鍵段落;沒有通讀。

## 一句話
如果只允許不可信的資料以「幾個位元」的資訊量影響 agent 的決定,能不能既保住任務完成率,又證明攻擊者能做的事有上限?

## 這個領域在做什麼
- [source-exists: agentdojo] LLM agent 會呼叫工具並讀取外部資料;外部資料裡藏的指令可以劫持 agent,這叫 prompt injection。
- [source-exists: camel] 一類防禦是 information-flow control(資訊流控制,IFC):追蹤每筆資料的來源,不讓不可信的資料影響程式流程或流向未授權的地方。
- [source-exists: appa] 傳統 IFC 的標籤只增不減,結果不是過度封鎖正常操作,就是 agent 一讀到未審查的資料就卡死。
- [source-exists: limits] 放寬標籤的做法叫 declassification(降級)。這篇 2026 年 11 月的論文結論是:光靠系統設計無法消除效用損失,所以需要降級機制。

## 需要的知識
| 知識 | 我有沒有 | 補起來要多久 |
|---|---|---|
| LLM agent 與工具呼叫的實作(Python) | 應該有 | 約 1 週 |
| IFC、noninterference、language-based security | 沒有 | 約 4 到 6 週 |
| Quantitative information flow(min-entropy leakage) | 沒有 | 約 3 週 |
| 操作語意與形式證明的寫法 | 沒有 | 約 4 週以上 |

合計約 12 週以上,超過上限。[model-only]

## 缺口還在嗎
2026-11-22 在 arXiv 以三組關鍵字搜尋(declassification 加 agent/LLM;information flow 加 prompt injection 加 quantitative/leakage/bounded;information flow control 加 prompt injection),各看最新 12 筆。

- **問題被正式承認了。** [source-exists: limits] 明確說需要降級機制。這表示缺口存在,也表示其他團隊正往這裡走。
- **最接近的理論工作沒有做量化的界。** [source-exists: planters] 用 Isabelle/HOL 機械化證明了含 budget 的 agent 的安全性,但內文明寫 quantitative guarantees 與 hijacking(注入讓 agent 做事而不洩漏資料)不在範圍內。這個題目關心的正是後者。
- **「用 enum 或布林值傳遞」的機制本身不新。** [source-exists: camel] 內文顯示 CaMeL 的隔離 LLM 已經用 schema 限制輸出型別,包含 bool 與 enum。新的部分只剩「計算位元預算並給出界」。
- **另有團隊在做 LLM 的量化資訊流。** [source-exists: gif] 用 Jacobian 給出互資訊的上界,並有 Lean 4 證明。
- 限制:只查了 arXiv。資安頂會的論文不一定在上面。

結論:缺口沒有被完全做掉,但已經被多個強團隊從不同方向包圍。

## 一年內做得完嗎
最小可交付的版本 [model-only]:在現有的 IFC 防禦上實作位元預算的降級,量測哪些任務被過度封鎖、完成率隨預算怎麼變,並證明多次降級組合後的界。

實證部分做得完。理論部分的對手是用定理證明器、每個月都在發論文的團隊。

## 需要的資源
- [source-exists: camel] CaMeL 的程式碼已公開。[source-exists: agentdojo] AgentDojo 是公開的評測環境。拿得到。
- LLM API 的費用:需要預算,金額未估。
- 不需要特殊硬體。

## 最可能失敗的原因
**核心定理太淺,而實證的改善空間可能很小。**
- 「映射到 2^b 個值的函數最多產生 2^b 種結果」幾乎是定義本身,不構成貢獻。有份量的部分是多次降級如何組合、攻擊者能適應時界還成不成立。[model-only]
- [source-exists: camel] CaMeL 在 AgentDojo 上完成 77% 的任務,無防禦時是 84%,差距只有 7 個百分點。內文還顯示它在 travel 類任務的完成率隨模型更新從 25% 升到 75%,而 CaMeL 本身沒有改動。也就是說,在這個評測上「過度封鎖」的問題正在自己縮小。

## 對照判準
| 判準 | 結果 | 依據 |
|---|---|---|
| 1. 跟得上 | 不符合 | 形式方法是全新領域,估計 12 週以上 |
| 2. 缺口還在 | 目前無法判斷 | 沒被完全做掉,但被包圍;非 arXiv 的論文沒查 |
| 3. 有模型也有驗證 | 符合 | 形式模型加 AgentDojo |
| 4. 資源拿得到 | 符合 | 程式與評測都公開;需要 API 預算 |
| 5. 一年做得完 | 邊緣 | 實證可以;理論要跟強團隊競爭 |
| 6. 有人能指導 | 目前無法判斷 | 報告說相關教授的論文清單沒抓到 |

## 結論
未定。缺一項事實:**在比 AgentDojo 更大的系統(多 agent、有狀態)上,IFC 的效用損失實際有多大?** 如果很大,這個題目應該換到那個場景;如果不大,它的實證價值就不足。
