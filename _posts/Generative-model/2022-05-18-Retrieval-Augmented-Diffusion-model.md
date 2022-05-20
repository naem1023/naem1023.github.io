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

잘못된 내용에 대한 피드백은 언제나 감사합니다.

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

이러한 retrieval-enhanced 전략을 diffusion model과 결합하는 것으로 multi-modal datasets에서 fully parametric conterparts를 능가하는 경량화 모델을 얻을 수 있다.

![](/assets/Generative-model/20220520155013.png)  

Fig2에서는 CLIP을 사용하여 text-image space에서 nearst neighbors를 retrieve할 때, text prompts를 exemplar-based synthesis의 쿼리로 사용함을 보여준다. CLIP의 text encoding인 $\phi_{\text{\tiny CLIP}}(c_{\text{\tiny text}})$에 직접적으로 영향을 받아 retrieved neighbors를 구성할 때, 논문의 ImageNet 모델이 unseen/fictional한 text prompt를 일반화할 수 있음을 관찰했다. 
반면 $\phi_{\text{\tiny CLIP}}(c_{\text{\tiny text}})$를 retrieval database에서 가져온 $\phi_{\text{\tiny CLIP}}(c_{\text{\tiny text}})$와 관련 있는 k - 1개의 nearest neighbors와 함께 사용하거나, 혹은 text representation 없이 k개의 nearst neighbors와 사용한다면 모델은 generalization capabilities를 보여주지 않았다.

즉, Fig2는 'NNs only'와 'Text repr. and NNs'는 'Text repr. only'에 비해서 generalization capailities가 떨어지는 것을 보여주는 것이다.

## Abstract summary
따라서 논문은 retrieval-augmnented generative modeling with diffuson model이라는 간단한 framework를 보여준다. CLIP의 latent space에서 seraching, conditioning을 진행함으로써 아주 작은 컴퓨팅 연산만으로 nearest neighbo representation을 만들 수 있는 것이다. 또한 retrieval 속도는 매우 빠르고 CLIP embedding은 매우 작은 storage만을 요구한다. semi-parametric approach는 high fidelity와 diversity를 모두 충족시킬 수 있다고도 한다. 

CLIP의 image-text features를 사용하는 것으로 Fig2에서 보여줬던 text-to-image, class-conditional synthesis와 같은 다양한 conditional application을 만들 수 있다. 

마지막으로 test time에서 retrieval database를 변화시키는 것이 synthesis process control에 추가적인 flexibility를 부여하는지 demonstrate 할 것이다. 또한 이것이 기존의 classifier-free diffusion model과 어떻게 결합되는지도 보여줄 것이다.

# Related work

## Diffusion Models for Image Synthesis
일반적인 diffusion model의 성과와 한계에 대해서 짚는다. ImageNet과 같은 복잡한 Dataset에 대해서 unconditional image generation을 할 때, 모델의 크기와 compute resources가 많이 요구된다고 한다.

논문은 이러한 한계를 극복하기 위해 trainable parameters를 external memroy와 교환하는 것을 제안한다. 이를 통해 작은 모델이라 할지라도 지속적으로 발전하는 모델과 동등한 수준의 high fidelity image generation을 수행할 수 있도록 한다.

## Retrieval-Agumented Generative Models
External memory를 활용하여 기존 모델의 성능을 향상시키는 것은 NLP 분야에서 많이 사용하는 기법이다. RETRO[5]의 경우 더 적은 parameter와 compute resources를 사용해서 SOTA를 찍은 retrieaval-enhanced transformer를 제안했다. External memory를 사용한 retireval-augmented model이 parametric deep learning model을 semi-parametric model로 변환했다.

초기의 retireval-augmented visual model들은 external memory를 사용하지 않고 retrieval를 위해 training data를 사용했다. IC-GAN의 경우, GAN을 학습시키기 위해 training images의 neighborhood를 활용하고 training data의 single instances에 제한을 받아 samples를 생성한다. 

하지만 training data를 retireval 대상으로 삼았기 때문에 generalization capacity가 떨어질 수 밖에 없고, 우리는 exteranl memory를 통해 이를 해소하고자 한다.

## Concurrent Work
최근에 본 논문과 비슷한 연구들로 unCLIP[6]과 kNN-Diffusion[7]이 제안됐다. 

unCLIP은 CLIP의 representation으로 diffusion model을 conditioning하고 large-scale computation을 사용해서 high quality text-image results를 만든다. 하지만 본 논문의 연구와 다르게, 이 모델은 training data에 대한 CLIP representation에 제한을 받기 때문에, geneartive text-image를 나중에 학습한다. 

kNN-Diffusion은 unCLIP의 위와 같은 문제를 neighborhood를 통해 conditioning함으로써 회피하는데, 이것은 본 논문의 연구와 매우 유사하다. 또한 서로 다른 형태의 neighborhood representation을 분석하기 위해 discrete diffusion formulation보다 continuous formulation을 사용했고 text-image synthesis에 제한되지 않는다는 점 또한 매우 유사하다.

# Reference
- Paper: https://arxiv.org/abs/2204.11824
- [1]: [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841)
- [2]: [Diffusion model beat GANs on image synthesis](https://arxiv.org/abs/2105.05233)
- [3]: [Glide: Towards photorealistic image generation and editing with text-guided diffusion models](https://arxiv.org/abs/2112.10741)
- [4]: [Hierarchical text-conditional image generation with clip latents](https://arxiv.org/abs/2204.06125)
- [5]: [Improving language models by retrieving from trillions of tokens](https://arxiv.org/abs/2112.04426)
- [6]: [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125)
- [7]: [Knn-diffusion: Image generation via large-scale retrieval](https://arxiv.org/abs/2204.02849)