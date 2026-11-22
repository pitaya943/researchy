# 候選題目

狀態:`待評估`、`未定`(評估過但缺一項事實)、`保留`、`丟棄`、`選定`。

前十個題目來自 2026-11-18 的報告。該報告引用的論文在本 session 都還沒有開啟查證,所以它對每個題目的描述目前都是 `model-only`。

| 代號 | 題目 | 狀態 | 理由(一行) | 評估頁 |
|---|---|---|---|---|
| kv-offload-aging-flash | 可靠度感知的 KV cache 卸載:老化 flash 上「載入或重算」的最優決策 | 未定 | 缺:實際使用條件下 read retry 讓讀取吞吐量下降多少 | [頁面](kv-offload-aging-flash.md) |
| kv-zns-write-amp | KV cache 生命週期與 ZNS zone 對齊:寫入放大的解析模型 | 待評估 | | |
| ifc-bounded-declassification | 有界洩漏的降級:讓資訊流控制的 LLM agent 不再過度封鎖 | 未定 | 缺:在多 agent、有狀態的系統上 IFC 的效用損失有多大;另外學習成本超過上限 | [頁面](ifc-bounded-declassification.md) |
| agent-injection-epidemic | 多 agent 系統中 prompt injection 的傳播:流行病模型與閾值 | 待評估 | | |
| qkd-keypool-backpressure | QKD 網路的金鑰池排隊模型與吞吐量最優路由 | 待評估 | | |
| entanglement-cutoff-multipath | 帶 cutoff 的多路徑糾纏分配:速率與保真度的前緣 | 待評估 | | |
| xapp-conflict-game | O-RAN xApp 衝突的賽局模型與無政府代價 | 待評估 | | |
| 5g-core-metastability | 5G 核心網控制面在信令風暴下的排隊模型與准入控制 | 待評估 | | |
| eew-conformal | 具保證涵蓋率的地震預警:時空分佈偏移下的 conformal prediction | 待評估 | | |
| tee-llm-perf-model | 機密運算下 LLM 推論的效能模型 | 待評估 | | |
| tfm | 區塊鏈交易手續費機制(transaction fee mechanism);見 `maps/transaction-fee-mechanisms.md` | 待評估 | 這是一個領域,還不是題目;需要先收斂到其中一個方向 | |
