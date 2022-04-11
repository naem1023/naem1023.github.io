---
title: "NVTabular"
excerpt: "Summary of NVTabular"
categories: "ML"
tags: "ml", "nvt", "preprocessing"
---

# NVTabular
https://nvidia-merlin.github.io/NVTabular/v0.6.1/Introduction.html

Nvidia에서 제공해주는 tabular data에 대한 Feature Engineering, Preprocessing 라이브러리이다. Transformers4Rec에서 해당 라이브러리를 사용하기에 정리했다.

GPU 연산도 지원한다고 한다.

## Categorify
Tabular data에서 text 형태의 categorical data를 unique integer value로 변환해준다.

```py
# Define pipeline
cat_features = CATEGORICAL_COLUMNS >> nvt.ops.Categorify(freq_threshold=10)

# Initialize the workflow and execute it
proc = nvt.Workflow(cat_features)
proc.fit(dataset)
proc.transform(dataset).to_parquet('./test/')
```