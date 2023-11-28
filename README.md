![Static Badge](https://img.shields.io/badge/CONTRIBUTORS-3-red?link=https%3A%2F%2Fgithub.com%2FSmulemun%2Fmusic-to-image%2Fgraphs%2Fcontributors)
![Static Badge](https://img.shields.io/badge/LICENSE-MIT-green?link=https%3A%2F%2Fgithub.com%2FSmulemun%2Fmusic-to-image%2Fblob%2Fmain%2FLICENSE)


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Infrastructure object recognition using satellite data</h3>

  <p align="center">
      </p>
    <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://static7.tgstat.ru/channels/_0/ba/badb3a1dbc243ca1c631391943be588a.jpg" alt="Logo" width="80" height="80">
  </a>
  </p>
        Skolkovo Institute of Science and Technology
      <br />
        <p align="center">
          Team Vladik:
          Almaz Dautov, Damir Abdulayev, Danil Kuchukov
      </p>
    <a href="https://docs.google.com/document/d/1uiGTBn9Rf7Vny-fc9C7ETZ9FvvwLYmAYQ7yLU4dvCV4/edit#heading=h.tut3bn1jjr"><strong> Teaser»</strong></a>
     ·
    <a href="https://lodmedia.hb.bizmrg.com/presentations/1065852/1059974/Final_Presentation_1_.pdf"><strong>Presentation»</strong></a>
     ·
    <a href="https://drive.google.com/file/d/1F8hC8Akxj9BKKEsJc7F3LBb2lck7zNnx/view"><strong>View Demo»</strong></a>
    <br />
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#model-architecture">Model Architecture</a></li>
    <li><a href="#Results">Results</a></li>
     <li><a href="#Hackaton leaderboard">Hackaton leaderboard</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT -->
## About the project

We present a model for Semantic Segmentation of buildings using satellite data, Hackaton "Цифровой прорыв" case from Scholtech. This model allows you to segment buildings from satellite images in the form of a binary mask with high accuracy.
To solve the problem of binary semantic segmentation of buildings, a number of steps were taken:
- Collection of an additional dataset with a similar segmentation method. We used APIs from mapbox.com [2] for satellite imagery and openstreetmap.org [3] to segment individual buildings using QGIS [4] and the Overpass API [5].
- Post-processing masks by removing buildings smaller than 100 pixels (100 m^2)
- Preprocessing large satellite images by custom dividing them into “tiles” of 1024x1024 size.The peculiarity of this technique is that we can generate images that intersect with each other and restore the mask of the original image by voting.
- Training several models on original and tiled data, including Unet, Unet++ and Ensemble from Unet++


<!-- MODEL -->
## Model Architecture

### Ensemble UNet++

- Unet++ with 'resnet50' backbone and Unet++ with 'efficientnet-b7' backbone
- Encoders Weights: Pre-trained on ImageNet

Both models in the ensemble are instances of the UNet++ architecture, which is an extension of the traditional UNet architecture. UNet++ introduces a more expansive skip connection structure to improve information flow between the encoder and decoder. The use of different backbones (ResNet-50 and EfficientNet-B7) allows the model to capture features at different levels of abstraction.

![](https://miro.medium.com/v2/resize:fit:2000/1*XmqyKSM3I68GWGJg3V5ZkQ.jpeg)

## Results

| Model / backbone                            | F1 score (Validation) | F1 score (Test)  | 
|---------------------------------------------|----------|---|
| U-net ++ / resnet50                         | 0.5813   |   |  
| DeepLabV3+ / resnet152                      | 0.6043   |   |  
| U-net ++ Augmented / resnet50               | 0.6238   |   |  
| U-net++ / timm-efficientnet-b8              | 0.6571   |   |   
| U-net++ Ensemble/ resnet50, efficientnet-b7 | 0.7006   |  0.71133 |  

## Hackaton leaderboard

![0b15610d-ba29-42ca-aea2-215ef24e73e9](https://github.com/SpeedFireF/skoltech-ior/assets/64196918/aa419c67-6043-4b30-9bbb-1a757ac4be3e)


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.
