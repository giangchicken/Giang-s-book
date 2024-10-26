# **Summary of the Paper: "Using Publicly Available Satellite Imagery and Deep Learning to Understand Economic Well-Being in Africa"**

---

## **Introduction**

The paper addresses the **need for accurate local-level measurements of economic well-being** to support effective policy-making and targeted programs in developing regions, particularly **in Africa**. Traditional survey methods for measuring asset wealth are often **infrequent and costly**, leading to **gaps in data availability**. The authors propose an approach using **publicly available multispectral satellite imagery** combined with **deep learning** to predict **asset wealth** across approximately **20,000 African villages**, offering a **timely and scalable method** for economic estimation.

---

## **Results**

The study demonstrates that **deep learning models trained on satellite imagery** can **explain about 70% of the variation** in ground-measured village wealth, **outperforming previous benchmarks** that used high-resolution imagery. Furthermore, these models can explain **up to 50% of the variation in district-aggregated wealth changes** over time. The **errors in satellite-based estimates** are also **comparable to those in existing ground data**, indicating the **reliability** of satellite imagery as an economic measurement tool.

---

## **Modeling Approach**

The authors utilize a **convolutional neural network (CNN)** architecture to predict **village-specific wealth measures** from satellite imagery. Key aspects of the model include:

- **Input Data**: The model uses **multispectral daytime imagery** from **Landsat (30m/pixel)** and **nighttime lights imagery** as inputs, both **temporally and spatially matched**.
- **Architecture**: The CNN is designed to **learn features from both daytime and nighttime imagery** in an **end-to-end training process**. Separate models are trained for each imagery type and are **combined in a final fully connected layer**.
- **Training Process**: Models are trained using a **mean squared error loss function**, optimized with the **Adam optimizer**, and incorporate **data augmentation** to prevent overfitting.

---

## **Data and Quality**

The study leverages both **satellite imagery** and **ground truth data**:

- **Satellite Imagery**: Publicly available **multispectral images** from **Landsat** and **nighttime lights data**. These are processed into **3-year median composites** to reduce cloud cover effects.
- **Ground Truth Data**: Asset wealth data sourced from **Demographic and Health Surveys (DHS)** (2009-2016) covering **500,000+ households** across **19,669 villages** in **23 African countries**. An **asset wealth index** is created using **principal component analysis (PCA)** based on household asset data.
- **Data Collection Challenges**: The study notes challenges from **random GPS displacement in survey data**, which introduces **noise** and affects **spatial accuracy** when matching with satellite imagery.

This comprehensive approach illustrates the **feasibility of using satellite imagery and deep learning** to generate **reliable economic estimates**, providing a valuable resource for **researchers and policymakers** in regions where data is scarce.


[Read all paper](https://www.semanticscholar.org/paper/Using-publicly-available-satellite-imagery-and-deep-Yeh-Perez/83bd44a487ea02e19a27e9d77cd736dd4f5bcc00)