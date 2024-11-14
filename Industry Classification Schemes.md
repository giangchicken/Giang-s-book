# **Summary of the Paper: A Comparison of Industry Classification Schemesfor Capital Market Research**

---

## Introduction
The article compares four prominent industry classification schemes used in financial research and capital markets: **SIC (Standard Industrial Classification)**, **NAICS (North American Industry Classification System)**, **GICS (Global Industry Classification Standard)**, and **FF (Fama-French Classification)**. The study investigates how each classification impacts the ability to explain economic similarity and stock return comovements among firms, addressing whether a scheme’s structure benefits from inherent advantages or biases.

---

## Knowledge Related

### Explanation of Sector, Industry Group, Industry, and Sub-Industry

![](./images/Screenshot%202024-11-14%20160138.png)

1. **Sector**: 
   - The highest level in an industry classification system, grouping broad areas of economic activity. For example, sectors like **Technology**, **Healthcare**, or **Finance** encompass various industries that share similar high-level economic roles.

   ![#](./images/90451.jpg)

2. **Industry Group**:
   - A subset within a sector that includes closely related industries. Industry groups provide more specific categories within a sector, helping to refine the classification. For instance, within the **Technology** sector, there could be an industry group called **Software & Services**.

3. **Industry**:
   - Within each industry group, an **industry** represents firms with more focused and related business activities. Industries enable a narrower classification, such as dividing the **Software & Services** group into **Application Software** and **IT Services** industries.

4. **Sub-Industry**:
   - The most granular level of classification, a **sub-industry** identifies firms with highly specific economic activities. Within the **Application Software** industry, for instance, sub-industries might differentiate between **Enterprise Software** and **Educational Software** firms.


![#](./images/90452.jpg) ![#](./images/90453.jpg)


>**Note**: These classification levels apply specifically to **GICS**. Each industry classification scheme (such as SIC, NAICS, and ISIC) has its own hierarchy and terminology for levels. Please consult detailed information on the specific classification scheme before applying it.

---

### **Industry Classification**: 
   **Industry classification schemes** organize firms to facilitate economic and financial analyses. The effectiveness of these schemes varies based on how accurately they capture industry-specific behaviors.
---
### **Classification Schemes**:
   - **SIC (Standard Industrial Classification)**: Developed by the U.S. government, SIC is widely used but is now being phased out in favor of NAICS.
   - **NAICS (North American Industry Classification System)**: Created collaboratively by the U.S., Canada, and Mexico, NAICS aims for more updated classification compared to SIC.
   - **GICS (Global Industry Classification Standard)**: A classification developed by Standard & Poor’s and MSCI, widely used in global financial markets.
   - **FF (Fama-French Classification)**: Tailored for academic research, the FF classification organizes industries to examine stock returns based on firm size and value.   


| Scheme           | 1st Digit (Broadest Level) | 2nd Digit           | 3rd Digit         | 4th Digit        | 5th Digit        | 6th Digit        | 7th Digit        | 8th Digit (Narrowest Level) |
|------------------|----------------------------|---------------------|-------------------|------------------|------------------|------------------|------------------|-----------------------------|
| **SIC**          | Division                   | Major Group         | Industry Group    | Industry         | N/A              | N/A              | N/A              | N/A                         |
| **NAICS**        | Sector                     |                     | Subsector         | Industry Group   | Industry         | National Industry| N/A              | N/A                         |
| **GICS**         | Sector                     |                     | Industry Group    |                  | Industry         |                  | Sub-Industry     |                             |
| **GICS**         | Industry                   |                     | N/A               | N/A              | N/A              | N/A              | N/A              | N/A                         |

---
### **Adjusted \( R^2 \)**: This metric measures how well a classification scheme explains stock return variations. The **Adjusted \( R^2 \)** accounts for the number of independent variables used, providing a more accurate reflection of a model’s explanatory power without overfitting.

---

## Data
The study uses data from **S&P 1500** firms, covering various sectors. The analysis includes:
   - **Firm stock returns**: To observe comovements and compare similarities among firms within industry groups.
   - **Financial metrics**: Such as **price-to-book (P/B) ratios**, **enterprise value-to-sales (EV/S) ratios**, and **profitability ratios** (e.g., ROE, ROA) to assess the economic relatedness across industry classifications.


---



---

## References
![#](https://www.ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN162099773)