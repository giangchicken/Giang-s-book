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
### **Industry Classification** 
**Industry classification schemes** organize firms to facilitate economic and financial analyses. The effectiveness of these schemes varies based on how accurately they capture industry-specific behaviors.

---
### **Classification Schemes**:
   - **SIC (Standard Industrial Classification)**: Developed by the U.S. government, SIC is widely used but is now being phased out in favor of NAICS.
   - **NAICS (North American Industry Classification System)**: Created collaboratively by the U.S., Canada, and Mexico, NAICS aims for more updated classification compared to SIC.
   - **GICS (Global Industry Classification Standard)**: A classification developed by Standard & Poor’s and MSCI, widely used in global financial markets.
   - **FF (Fama-French Classification)**: Tailored for academic research, the FF classification organizes industries to examine stock returns based on firm size and value.   


```

      | Scheme    | 1st Digit (Broadest Level) | 2nd Digit    | 3rd Digit         | 4th Digit        | 5th Digit | 6th Digit        | 7th Digit      | 8th Digit (Narrowest Level) |
      |-----------|----------------------------|--------------|-------------------|------------------|-----------|------------------|----------------|-----------------------------|
      | **SIC**   | Division                   | Major Group  | Industry Group    | Industry         | N/A       | N/A              | N/A            | N/A                         |
      | **NAICS** | Sector                                    | Subsector         | Industry Group   | Industry  | National Industry| N/A            | N/A                         |
      | **GICS**  | Sector                                    | Industry Group                         Industry  |                  | Sub-Industry                                 |
      | **FF**    | Industry                                  | N/A               | N/A              | N/A       | N/A              | N/A            | N/A                         |

```
---
### **Adjusted R-square**
This metric in the Paper measures how well a classification scheme explains stock return variations. The **Adjusted R-square** accounts for the number of independent variables used, providing a more accurate reflection of a model’s explanatory power without overfitting.
![](./images/10_adjusted-r-squared.jpeg)

>[For more information](https://builtin.com/data-science/adjusted-r-squared)
---

### Economic Indicators 
 * **Price-to-Book (P/B) Ratio**:
 * **Enterprise Value-to-Sales (EV/S) Ratio**:
 * **Price-to-Earnings (P/E) Ratio**:
 * **Return on Equity (ROE)**:

## Data
The study uses data from **S&P 1500** firms, covering various sectors. The analysis includes:
   - **Firm stock returns**: To observe comovements and compare similarities among firms within industry groups.
   - **Financial metrics**: Such as **price-to-book (P/B) ratios**, **enterprise value-to-sales (EV/S) ratios**, and **profitability ratios** (e.g., ROE, ROA) to assess the economic relatedness across industry classifications.


---

## Results

* **Performance of GICS**: GICS consistently outperforms SIC, NAICS, and FF in explaining cross-sectional variations in firm-level returns, valuation multiples, and financial ratios. The study finds that GICS classifications explain, on average, 26.3% of monthly stock return variations compared to 22.9% for SIC.
* **Homogeneity in Valuation Multiples**: GICS also shows higher explanatory power for valuation multiples, especially for large-cap firms, making it more effective for classifying economically related firms.
* **Analyst Growth Forecasts**: The authors find that GICS classifications are more aligned with analyst forecasts, suggesting it better reflects market perceptions.

### **Key Findings to Note**
![Univariate Statistics for SIC, NAICS, FamaFrench and GICS](./images/Screenshot%202024-11-14%20191310.png)

### **TABLE 1**: Univariate Statistics for SIC, NAICS, FamaFrench and GICS
> This table reports univariate statistics for each classification level for SIC (Standard Industrial Classification), NAICS (North American Industry Classification System), Fama-French, and GICS (Global Industry Classification Standard), using S&P 1500 firms as of December 2001. 

> Fama-French refers to the industry classification system developed in their paper "Industry Costs of Equity" (1997).

> Panel A reports the number of classification levels, the official number of categories, and the functional number of categories for each classification level for each level of classification. A category is defined as functional if it has at least five members.

> Although some research uses the first digit as the broadest level, SIC codes are officially broken into 11 major divisions, labeled A through K. The sixth digit of the NAICS code is an additional level of detail specific to each country. For comparison purposes, the categories in the fifth and sixth digit levels are combined in this table, consistent with the 1997 NAICS manual.

> The level of industry we use for our analysis is boldface.

>Panel B reports univariate statistics for each of the preceding classification systems, using S&P 1500 firms as of December 2001, for the corresponding boldface level from Panel A.

---

### **TABLE 2**: Bridging Between SIC and NAICS, FamaFrench and GICS

![#](./images/Screenshot%202024-11-14%20210541.png) ![#](./images/Screenshot%202024-11-14%20210608.png) ![#](./images/Screenshot%202024-11-14%20211039.png)

> This table reports the degree of correspondence between SIC, Fama-French (FF), NAICS, and GICS for the December 2001 S&P 1500 firms by showing the level of agreement between SIC and the other three classifications.

> Fama-French refers to the industry classification system developed in their paper "Industry Costs of Equity" (1997). See their Appendix A for a description and definition of their industry names.

> We show the primary equivalent (i.e., the other system's category that has the highest level of correspondence) measured by the total number of firms for each two-digit SIC code. Only industry classifications that actually have member firms are considered.

> For example, the S&P 1500 has 38 firms in SIC industry 20 (Food and Kindred Products). The NAICS classification system classifies 30 of these firms in subsector 311 (Food Manufacturing) for a 79% correspondence. The FF classification system classifies 29 of these firms in their category of "Food" for a 76% correspondence. Finally, the GICS classification system classifies 25 of these firms in industry 302020 (Food Products) for a 66% correspondence.

> For brevity, only the category with the highest level of correspondence is shown. Note that the FF correspondence is slightly misleading because there is an explicit mapping from SIC into FF using all four SIC digits. However, for comparative purposes, we use only two-digit SIC here.


---

### **TABLE 3**:  Comparison of Adjusted R-Square Among SIC, NAICS, FamaFrench and GICS for Returns
```plaintext
                     
                              FUNCTION:       R(i,t) = α.t + β.R(ind,t) + ε(i,t)

```
![](./images/Screenshot%202024-11-14%20211402.png)
![](./images/Screenshot%202024-11-14%20225912.png)

> This table reports the firm-months and adjusted R-squared for the above monthly OLS regression.

> The dependent variable, R, is the monthly return for firm i within industry j in data month t, from the CRSP monthly database. The independent variable, Rind, is the monthly average return for all firms in that industry classification.

> Industries are defined by either the first two digits of the firm's SIC code, the first three digits of the firm's NAICS code, the firm's Fama-French classification (FF), or the first 6 digits of the firm's GICS code. Each industry included in these regressions must have at least five members.

> Because classifications differ among SIC, FF, NAICS, and GICS, there will be differences in the number of firm-months reported for each regression.

> We use all firms from the S&P index as of December for each year (from Research Insight) for which we are able to find a PERMNO from CRSP by matching based on CUSIP.

---

## References
![#](https://www.ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN162099773)