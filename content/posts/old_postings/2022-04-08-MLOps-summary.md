---
title: MLOps Summary
excerpt: 산개된 mlops 내용들을 정리
categories: 
  - MLOps
tags:
  - mlops
---
# Set spec of service and experiment

서비스와 자원에 대한 spec이 명확해지면 MLOps 구성에 대한 결정이 가능하다.

절대적인 솔루션이 없기 때문에 여러 솔루션을 혼용해도 된다.
e.g., 서비스 스펙 상 kubernetes를 통한 pod 생성과 airflow를 통한 batch process가 병행되어야 할 수도 있다. 그렇다면 Airflow on Kubeflow 혹은 Airflow DAG를 통해 Kubeflow Pipeline을 trigger 구현하여 아키텍쳐를 구성해보자.

# MLOps frameworks
- MLflow
    - model tracking: commit, 실험지표, 실험 결과 artifact 관리
    - DVC(data version control): S3 Bucket과 호환되는 minio를 사용. git commit 기준으로 versioning한다.
- Airflow
    - ETL(Extraction, Transform, Load)이나 범용적인 task ochestration이 필요할 때.
    - shell script나 py파일을 사용하는 것만으로도 충분할 때. 
- Kubeflow
    - 다양하고 scaling이 가능한 ML/DL pipeline이 요구될 때
    - 노트북(ipynb) 위주의 개발, 배포가 필요하다면 유용.

# 예시
- CPU를 활용하는 작업이 많고 scaling이 필요하다면
    - Airflow + Kubernetes
- CPU를 활용하는 작업이 적다면
    - Airflow
- pipeline이 복잡하고 단순 scheduling만으로 불가능하다면
    - Kubeflow or Airflow + Kubeflow


