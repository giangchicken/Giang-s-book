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


>**Note**: These classification levels apply specifically to **GICS**. Each industry classification scheme (such as **SIC**, **NAICS** and **ISIC**) has its own hierarchy and terminology for levels. Please consult detailed information on the specific classification scheme before applying it.
---
### **Industry Classification** 
**Industry classification schemes** organize firms to facilitate economic and financial analyses. The effectiveness of these schemes varies based on how accurately they capture industry-specific behaviors.

---
### **Classification Schemes**:
   - **SIC (Standard Industrial Classification)**: Developed by the U.S. government, **SIC** is widely used but is now being phased out in favor of **NAICS**.
   - **NAICS (North American Industry Classification System)**: Created collaboratively by the U.S., Canada, and Mexico, **NAICS** aims for more updated classification compared to SIC.
   - **GICS (Global Industry Classification Standard)**: A classification developed by Standard & Poor’s and MSCI, widely used in global financial markets.
   - **FF (Fama-French Classification)**: Tailored for academic research, the FF classification organizes industries to examine stock returns based on firm size and value.   


```

| Scheme    | 1st Digit (Broadest Level) | 2nd Digit    | 3rd Digit         | 4th Digit        | 5th Digit | 6th Digit        | 7th Digit      | 8th Digit (Narrowest Level) |
|-----------|----------------------------|--------------|-------------------|------------------|-----------|------------------|----------------|-----------------------------|
| **SIC**   | Division                   | Major Group  | Industry Group    | Industry         | N/A       | N/A              | N/A            | N/A                         |
| **NAICS** | Sector                                    | Subsector         | Industry Group   | Industry  | National Industry| N/A            | N/A                         |
| **GICS**  | Sector                                    | Industry Group                       | Industry  |                  | Sub-Industry                                 |
| **FF**    | Industry                                  | N/A               | N/A              | N/A       | N/A              | N/A            | N/A                         |

```
---
### **Adjusted R-square**
This metric in the Paper measures how well a classification scheme explains stock return variations. The **Adjusted R-square** accounts for the number of independent variables used, providing a more accurate reflection of a model’s explanatory power without overfitting.
![](./images/10_adjusted-r-squared.jpeg)

>[For more information](https://builtin.com/data-science/adjusted-r-squared)
---

### Economic Indicators 
 - **Returns**: Stock returns from the CRSP database.
 - **Price-to-book (pb)**: Market capitalization divided by total common equity.
 - **Enterprise value-to-sales (evs)**: The sum of market capitalization and long-term debt divided by net sales.
 - **Price-to-earnings (pe)**: Market capitalization divided by net income before extraordinary items (for firms with positive net income only).
 - **Return on net operating assets (rnoa)**: Net operating income after depreciation divided by the sum of property, plant, and equipment, and current assets, less current liabilities.
 - **Return on equity (roe)**: Net income before extraordinary items divided by total common equity.
 - **Asset turnover (at)**: Total assets divided by net sales.
 - **Profit margin (pm)**: Net operating income after depreciation divided by net sales.
 - **Leverage (lev)**: Total liabilities divided by total stockholders’ equity.
 - **Long-term analyst growth forecast (ltgrowth)**: Analyst predictions for future growth.
 - **One-year-ahead realized sales growth (salesgrowth)**: Actual sales growth for the subsequent year.
 - **Scaled research and development expense (R&D)**: Research and development expense divided by net sales.

## Data
The study uses data from **S&P 1500** firms (**S&P 500** large-cap, **400** mid-cap, and **600** small-cap), covering various sectors. The analysis includes:
   - **Firm stock returns**: To observe comovements and compare similarities among firms within industry groups.
   - **Financial metrics**: Such as **price-to-book (P/B) ratios**, **enterprise value-to-sales (EV/S) ratios** and **profitability ratios** (e.g., ROE, ROA) to assess the economic relatedness across industry classifications.

**Industries Classification**:
Industries are defined by:
   1. The first two digits of the firm's **SIC** code.
   2. The firm's **Fama-French** classification (FF).
   3. The first three digits of the firm's **NAICS** code.
   4. The first six digits of the firm's **GICS** code.
---

## Results

* **Performance of GICS**: **GICS** consistently outperforms **SIC**, **NAICS**, and **FF** in explaining cross-sectional variations in firm-level returns, valuation multiples, and financial ratios. The study finds that GICS classifications explain, on average, 26.3% of monthly stock return variations compared to 22.9% for SIC.
* **Homogeneity in Valuation Multiples**: GICS also shows higher explanatory power for valuation multiples, especially for large-cap firms, making it more effective for classifying economically related firms.
* **Analyst Growth Forecasts**: The authors find that GICS classifications are more aligned with analyst forecasts, suggesting it better reflects market perceptions.

### **Key Findings to Note**
![Univariate Statistics for SIC, NAICS, FamaFrench and GICS](./images/Screenshot%202024-11-14%20191310.png)

### **TABLE 1**: Univariate Statistics for SIC, NAICS, FamaFrench and GICS
> This table reports univariate statistics for each classification level for **SIC (Standard Industrial Classification)**, **NAICS (North American Industry Classification System)**, **Fama-French**, and **GICS (Global Industry Classification Standard)**, using S&P 1500 firms as of December 2001.
>
> **Fama-French Classification**:
> - Refers to the industry classification system developed in their paper "Industry Costs of Equity" (1997).
>
> **Panel A**:
> - Reports the following for each classification system:
>   1. The number of classification levels.
>   2. The official number of categories.
>   3. The functional number of categories for each classification level.
> - A **functional category** is defined as one with at least **five members**.
> - Although the first digit of **SIC** codes is often used as the broadest level, the official system divides industries into **11 major divisions** labeled **A through K**.
> - The sixth digit of the **NAICS** code provides additional country-specific detail. For comparison purposes, this table combines the categories at the fifth and sixth levels, consistent with the **1997 NAICS manual**.
> - The **boldface level** represents the level of industry classification used for subsequent analysis.
>
> **Panel B**:
> - Reports univariate statistics for each classification system using the **S&P 1500 firms** as of December 2001.
> - These statistics correspond to the **boldface level** from Panel A for each classification system.

---

### **TABLE 2**: Bridging Between SIC and NAICS, FamaFrench and GICS

![#](./images/Screenshot%202024-11-14%20210541.png) ![#](./images/Screenshot%202024-11-14%20210608.png) ![#](./images/Screenshot%202024-11-14%20211039.png)

> This table reports the degree of correspondence between **SIC**, **Fama-French (FF)**, **NAICS**, and **GICS** for the December 2001 **S&P 1500 firms** by showing the level of agreement between SIC and the other three classifications.
>
> **Fama-French Classification**:
> - Refers to the industry classification system developed in the paper "Industry Costs of Equity" (1997) by Fama and French.
> - See **Appendix A** of their paper for a detailed description and definition of their industry names.
>
> **Methodology**:
> - The primary equivalent for each two-digit SIC code is determined by identifying the category in the other classification system (**NAICS**, **FF**, or **GICS**) with the highest level of correspondence.
> - Correspondence is measured by the total number of firms classified in each system.
> - Only industry classifications with actual member firms are considered.
>
> **Example**:
> - In **SIC industry 20** (Food and Kindred Products), there are **38 firms** in the **S&P 1500**:
>   - The **NAICS** system classifies **30 firms** in subsector **311 (Food Manufacturing)**, resulting in a **79% correspondence**.
>   - The **FF** system classifies **29 firms** in the category "Food", resulting in a **76% correspondence**.
>   - The **GICS** system classifies **25 firms** in industry **302020 (Food Products)**, resulting in a **66% correspondence**.
>
> **Key Note**:
> - Only the category with the highest level of correspondence is shown for brevity.
> - The FF correspondence might appear slightly misleading because there is an explicit mapping from **SIC** into **FF** using all four SIC digits. However, for comparative purposes, this table uses only the two-digit SIC codes.


---

### **TABLE 3**:  Comparison of Adjusted R-Square Among SIC, NAICS, FamaFrench and GICS for Returns
```plaintext
                     
                              FUNCTION:       R(i,t) = α.t + β.R(ind,t) + ε(i,t)

   The dependent variable, R, is the monthly return for firm i within industry j in data month t, 
   from the CRSP monthly database. The independent variable, Rind, is the monthly average return 
   for all firms in that industry classification.

```
![](./images/Screenshot%202024-11-14%20211402.png)
![](./images/Screenshot%202024-11-14%20225912.png)

> This table reports the firm-months and adjusted **R-squared** for the above monthly OLS regression.
>
>
> Each industry included in these regressions must have at least **five members**.
>
> **Methodology**:
> - Because the definitions of industries differ among **SIC**, **FF**, **NAICS**, and **GICS**, the number of firm-months reported will vary across the regressions.
> - The analysis uses all firms in the **S&P index** as of December for each year, sourced from **Research Insight**.
> - Firms are matched to a **PERMNO** from CRSP using their **CUSIP**.

---

### **TABLE 4**:   Comparison of Adjusted R-square for S&P 1500 Firms Among SIC, NAICS, FamaFrench and GICS (Industries for Returns, Financial Ratios and Other Financial Information)
```plaintext
                     
                              FUNCTION:       vble(i,t) = α1 + β.vble(ind, t) + ε(i,t)

   vble(i,t) is one of the following: returns, price-to-book (P/B, market capitalization divided 
   by total common equity), enterprise value-to-sales (EV/S, the sum of market capitalization and 
   long-term debt divided by net sales), price-to-earnings (P/E, market capitalization divided by 
   net income before extraordinary items), return on net operating assets (RNOA, net operating 
   income after depreciation divided by the sum of property, plant, and equipment and current 
   assets, less current liabilities), return on equity (ROE, net income before extraordinary items 
   divided by total common equity), asset turnover (AT, total assets divided by net sales), profit 
   margin (PM, net operating income after depreciation divided by net sales), leverage (LEV, total 
   liabilities divided by total stockholders' equity), long-term analyst growth forecast 
   (LT Growth), one-year-ahead realized sales growth (Sales Growth), and scaled research and 
   development expense (R&D, research and development expense divided by net sales) for firm i 
   within industry j in data year t.

   vble(ind) is the yearly average for that variable for all firms in that industry classification.

```

![#](./images/Screenshot%202024-11-15%20031545.png)
![#](./images/Screenshot%202024-11-15%20031627.png)

> This table reports the average **adjusted R-squared** for **S&P 1500 firms**, from Research Insight, for the above OLS regression. Returns are from CRSP's monthly database. Share prices and shares outstanding are drawn from CRSP as of December 31 of each year. Financial statement information is from Compustat, for the fiscal year ending in that year. Analyst long-term growth forecasts are the most recent December consensus forecast for that year, from IBES.
>
>
> Each industry included in these regressions must have at least **five members**.
>
> **Key Methodology**:
> - For each variable, the highest adjusted **R-squared** is highlighted in boldface.
> - A two-tailed **t-test** is performed to compare the adjusted differences between **GICS** and other classifications.
> - The analysis is based on the time series of differences from **1994 to 2000** (2001 for returns).
>
> **Panel Descriptions**:
> - **Panel A**: Reports results for stock returns.
> - **Panel B**: Reports results for valuation multiples.
> - **Panel C**: Reports results for financial ratios.
> - **Panel D**: Reports results for other financial information.

---

### **TABLE 5**:    Monte Carlo Simulated Adjusted R2

>**Note**: Although we attempt to ensure that the numbers of industry groups are
         similar across the classification schemes, differences remain. Because we
         require at least five firms per industry, one possible concern is that one
         industry definition might have a mechanical advantage over others. For 
         example, a classification system with fewer industry partitions has an inherent
         disadvantage when the total number of firms is held constant. If ones cheme
         has 10 functional industries consisting of 6 member firms each,and another
         scheme has 3 functional industries consisting of 20 members each, we can
         expect the first scheme to achieve a higher R2 than the second, even if the
         actual allocation of firms for both schemes was random.
         To ensure our results are not due to these differences, we conduct Monte
         Carlo simulations that neutralize the advantage a scheme derives from 
         having a greater number of industry categories. To conduct the simulation,
         we randomly assign S&P 1500 firms into the same number of industry cat
         egories, with the same number of firms per industry, as a given scheme.
         We then conduct the regression on the simulated data, generating a 
         simulated R2. We then repeat the procedure 500 times, producing an average
         simulated R2 for each classification scheme. Each simulated R2 serves as a
         performance benchmark for the scheme in question.

![](./images/Screenshot%202024-11-16%20154647.png)
![](./images/Screenshot%202024-11-16%20154725.png)
![](./images/Screenshot%202024-11-16%20154749.png)

> This table compares the average adjusted **R-squared** for **S&P 1500** firms, obtained from Research Insight, with simulated adjusted **R-squared** values generated by randomly assigning firms to industry classifications. Each simulation was repeated 500 times, and the table presents the average adjusted **R-squared** from these simulations. The "Revised" column represents the difference between the actual average **R-squared** and the average simulated values.
>
> **Data Sources**:
> - Returns are sourced from CRSP's monthly database.
> - Share prices and shares outstanding are from CRSP as of December 31 of each year.
> - Financial statement information is from Compustat for the fiscal year ending in that year.
> - Analyst long-term growth forecasts are the most recent December consensus forecast for that year, obtained from IBES.
>
> **Panel Descriptions**:
> - **Panel A**: Results for stock returns.
> - **Panel B**: Results for valuation multiples.
> - **Panel C**: Results for financial ratios.
> - **Panel D**: Results for other financial information.
>
> Industries are classified using one of the following methods:
> 1. The first two digits of the firm’s **SIC** code.
> 2. The firm’s **Fama-French** classification (FF).
> 3. The first three digits of the firm’s **NAICS** code.
> 4. The first six digits of the firm’s **GICS** code.
>
> Each industry must have at least five members to be included in these regressions.
>
> We conduct two-tailed **t-tests** to compare the adjusted differences between the **GICS** classification and other methods. These tests are based on the time series of differences from 1994 to 2000 (2001 for returns). For these tests, the average simulated adjusted **R-squared** is treated as a constant.

---

### **TABLE 6**:    Comparison of Adjusted R2 Among SIC, NAICS, FamaFrench and GICS Industries for Returns, Financial Ratios and Other Financial Information

```plaintext

                              FUNCTION:       vble(i,t) = α.t + β.vble(ind,t) + ε(i,t)

   The dependent variable, vble, represents the yearly value for firm i within industry j in year t. 
   The independent variable, vble(ind), is the yearly average value for all firms in that industry classification.

```

![](./images/Screenshot%202024-11-16%20160104.png)
![](./images/Screenshot%202024-11-16%20160127.png)
![](./images/Screenshot%202024-11-16%20160149.png)

> This table reports the average adjusted \(R^2\) for firms from 1994 to 2000 (2001 for returns) based on Research Insight for the above OLS regression. Returns are sourced from CRSP’s monthly database. Share prices and shares outstanding are drawn from CRSP as of December 31 of each year. Financial statement information is from Compustat for the fiscal year ending in that year. Analyst long-term growth forecasts are the most recent December consensus forecast for that year, sourced from IBES.
>
> Firm \(i\) within industry \(ind\) at year \(t\), the independent variable, \(vbleind\), is the yearly average (or monthly average for returns) for that variable across all firms in that industry classification.
>
>
> Each industry included in these regressions must have at least five members. For each variable, the highest average adjusted \(R^2\) is highlighted in boldface. We perform a two-tailed t-test on the difference between GICS and other classifications based on the time series of differences.
>
> - **Panel A** shows results for S&P 500 firms.
> - **Panel B** shows results for S&P 400 (midcap) firms.
> - **Panel C** shows results for S&P 600 (small-cap) firms.


---

## References
![#](https://www.ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN162099773)