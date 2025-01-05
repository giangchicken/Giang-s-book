# **Development of credit scoring models**

---
## **Introduction**

A credit score is a numerical representation of an individual's creditworthiness, commonly used by credit lending institutions like banks, telecom and fintechs. These organizations employ complex credit models that consider various factors that run from customer demographic details, their sources of income, credit commitments, and past loan performance to calculate a credit score.

Credit scoring models can broadly be categorized into:

- **Application Scorecards (A-score)**: These scorecards are instrumental in the initial phase of lending when applicants seek credit approval or rejection. A-score assesses the probability of a customer defaulting on their obligations over a specific time frame, known as the performance window. Typically, this performance window for A-score ranges from 12 to 24 months. Lenders rely on A-scores to make well-informed decisions about whether to extend credit to an applicant. The development, validation, and continuous monitoring of Application Scorecards (A-score) are somewhat more complex for the reason that the scorecard is intended to score all applicants (i.e., through-the-door population). Application scorecards are typically utilized for new customers and do not rely on an observation window. This is because they assess applicants based on information available at the time of application. It’s noteworthy that, for these scorecards, external data sources such as credit bureau information often play a dominant role compared to internal data in evaluating the creditworthiness of individuals seeking credit. These scorecards play a pivotal role in the credit approval process, assisting in making decisions that range from approval to rejection or referral to higher authorities. 

- **Behavior Scorecards (B-score)**: On the other hand, B-scores are designed for ongoing risk management of existing customers. They help lenders evaluate the likelihood of a customer defaulting within a predefined performance window, which usually spans from 6 to 18 months. B-scores are essential for monitoring the credit behavior of borrowers throughout their relationship with the institution. Behavioral scorecards, in contrast to application scorecards, incorporate an observation window that leverages internal data. This observation window allows for the analysis of a client’s historical financial behavior and credit-related activities within the financial institution. As a result, behavioral scorecards usually have more predictive power compared to application scorecards, making them particularly valuable for assessing credit risk among existing clients.

---

## **Prepare Label for Credit Score model**

### **Target Definition**

When building a credit scoring model, it’s essential to define your “good,” “bad,” and “indeterminate” cases to train the model effectively. By clearly defining these categories, you establish the basis for your target variable, which is essential for training and validating your credit scoring model. The “good” and “bad” cases serve as the foundation for modeling credit risk, while the “indeterminate” cases are set aside as they lack sufficient credit history for meaningful analysis at that stage. Here’s how these cases are typically defined:

- **“Good” Cases**: These are clients who have demonstrated responsible credit behavior by successfully completing all their loan payments. In most cases, this means the loan has matured, and they have fulfilled their financial obligations. You can also consider including clients who have completed a significant portion of their payments, such as 90% or 95%, in this category. 

- **“Bad” Cases**: Clients falling into the “bad” category are those who have defaulted on their payments or are significantly delinquent, typically defined as missing three consecutive EMI (Equated Monthly Installment) payments. These individuals represent credit risk as they have not met their financial obligations. 

- **“Indeterminate” Cases**: Clients in the “indeterminate” category are still in the early stages of loan repayment. Their credit behavior hasn’t fully manifested, making it uncertain whether they will eventually fall into the “good” or “bad” category. As a result, they are typically excluded from the model-building process as their credit status is yet to be determined.


### **Sample Window and Performance Window in Credit Scoring**

To predict the creditworthiness of future clients, it’s essential to define two critical time frames: the sample window and the performance window. The choice of these windows depends on the type of scorecard being developed (application or behavior) and aims to provide a robust basis for modeling credit risk.

#### **Sample Window**

The sample window is the specific time frame during which you gather data on loans that have been approved and disbursed. When selecting this window, it’s important not to go too far back into the past, as approval criteria, business conditions, and market factors may have significantly changed over time. However, it should also not be too recent to allow clients enough time to demonstrate their performance. 

For example, let’s consider today as the 1st of January 2024. If historical analysis indicates that 80% of loan defaults in your portfolio occur within a year, you establish a performance window of 12 months. This means that your sample window can include loans disbursed from January to December 2022. Each of these loans is then monitored for a rolling performance period of 12 months, up to December 2023, to assess their repayment outcomes. The independent or input variables for your model can comprise all the information collected from the client at the proposal stage. 

#### **Performance Window**

The **performance window** is the specific length of time during which you monitor the repayment behavior of loans from the sample window to determine whether they fall into the “good” or “bad” category. In the example above, the performance window is set at 12 months.

However, the sampling process varies depending on whether you are building an application scorecard or a behavior scorecard.

#### **Vintage Analysis**

At this point it is important to perform a **vintage analysis** on the data extract. This will help unearth the following:

- Identify if loans issued in a particular month or quarter are riskier than others.
- Determine the optimal period of performance window in development of scorecard.
- Monitor or track risk of a portfolio.
- Estimate minimum months required after that we can cross-sell to new customers.
- Forecast risk and can also be used in stress testing.

#### **Roll Rate Analysis**

The other analysis to conduct is a roll rate analysis. This is commonly used in loss forecasting and in determination of 'bad' customers (defaulters). It is used to define the threshold of delinquency to identify 'bad' customers. You can also use it to determine if to fully or partially charge off a loan.Finally this can be used to assess and determine cure rates timing.

- **Roll Rate Analysis** can provide valuable inputs for the calculation of expected credit losses (ECL) under IFRS 9. By analyzing historical roll rates, financial institutions can gain insights into the probability of transitions between different credit states (e.g., from current to 30 days past due, from 30 days past due to charge-off) and use this information to estimate future credit losses.

- **Roll Rate Analysis** can be used to develop probability of default (PD) models, which are one of the components of IFRS 9 impairment calculations. PD models estimate the likelihood of a borrower defaulting within a given time period.

---

## **Feature Engineering**

### **Creating Variables**

### **Clearning Variables**

### **Feature Selection**

---

## **Modeling**

---

## **Evaluation**

---

## **Probability to Scorecard**

### **Master Scale**

#### **Basic terms**
- **PDO: Points to Double the Odds** - how many points does the score change if the odds double (for example, increase from 100:1 to 200:1). The common values of PDO are 20 or 40.

- **Base score**: This is a baseline score. There is a certain meaning to this score, for example, a base score of 550 means the good bad odds is 20:1

So, if the baseline score is 550 meaning good bad odds 20:1 and PDO is 40, then a score of 590 will means good bad odds of 40:1, 630 means a good bad odds of 80:1 and so on.



#### **Calibration**

**Calibration** is bringing the odds or probabilities obtained from a model to a common scale. This improves its readability and is used to evaluate the incoming applications as good or bad and hence giving out a loan or not.


---
## References
[https://www.linkedin.com/pulse/development-credit-scoring-models-r-tony-gitonga/](https://www.linkedin.com/pulse/development-credit-scoring-models-r-tony-gitonga/)
[https://compassway.org/digital-lending/a-step-by-step-guide-to-credit-scorecard-development-in-2024/](https://compassway.org/digital-lending/a-step-by-step-guide-to-credit-scorecard-development-in-2024/)
