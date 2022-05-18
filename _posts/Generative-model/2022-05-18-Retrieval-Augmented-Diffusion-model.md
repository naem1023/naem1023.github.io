---
title: "Retreival-Augmented Diffusion model"
excerpt: "Review of Retreival-Augmented Diffusion model paper"
categories:
    - Generative-model
    - NLP
tags:
    - generative-model
    - nlp
---

# Abstract

논문은 NLP에서 성공적이었던 retrieval-based approach를 사용하여 diffusion model을 보완했다. 학습 시에, CLPI과 training instance에 이웃한 요소들과 같은 visual features를 retrieve하여 학습한다. 

논문의 모델은 CLIP의 image-text embedding space를 사용하는데, class-conditional이나 text-image synthesis처럼 explicity train을 하지 않는 task에 대해서 높은 성능을 보여준다. 또한 text와 image embedding에 모두 영향을 받을 수도 있다. 

논문의 모델은 SOTA를 찍은 unconditinal generation에도 적용할 수 있다. 

논문의 접근법은 적은 컴퓨터 자원을 소모하고 구현하기 쉽다고 한다. 

# Introduction
Language modeling과 high-fidelity images / other data types에 대한 generative synthesis는 엄청난 도약을 이뤘다. 특히 image synthesis에서 큰 충격을 준 결과들이 나왔다. [Ref 1, 2, 3, 4] 
이에 대한 3가지 main factor들은 아래와 같다.  

1. Vision task에서 transformer의 성공. Image synthesis에서는 이를 autoregressive modeing으로 수행했다.
2. Diffusion model이 high-resolution image generation에 성공적으로 적용됐고, generative image modeling의 표준이 됐다.
3. 1, 2번의 방법들은 scale이 잘 된다. 특히, 모델과 배치 사이즈를 고려할 때 scalability가 성능에 핵심적이라는 증거가 있다. 

하지만 대부분의 성능 개선 방법은 단순히 computational power와 parameter를 늘림으로써 이뤄진다. 이 논문은 이러한 방법을 사용하지 않고 성능을 향상시키고자 한다. 

반대로, retrieval-augmented generative language model의 성공에 영감을 얻어서, 논문은 visual examples의 memory를 위해 trainable parameters를 trade-off?한다. 또한 image database에 의하여 제안된 모델의 일부를 명시적으로 정의한다. (무슨 말인지 모르겠다..)

Training하는 동안, retrieval-augmented semi-parametric model은 nearest neighbor lookup을 통해 데이터베이스에 접근하고 retrieved visual building blocks를 기반으로 synthesize images를 학습한다.


# Reference
- Paper: https://arxiv.org/abs/2204.11824
- [1]: [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841)
- [2]: [Diffusion model beat GANs on image synthesis](https://arxiv.org/abs/2105.05233)
- [3]: [Glide: Towards photorealistic image generation and editing with text-guided
diffusion models](https://arxiv.org/abs/2112.10741)
- [4] [Hierarchical text-conditional
image generation with clip latents](https://arxiv.org/abs/2204.06125)
