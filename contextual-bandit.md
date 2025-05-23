# Contextual Bandit: A Powerful Approach in Reinforcement Learning

<div align="center">

![#](./images/1_FH4t-DcuKWfLYRWvd4JIjA.jpeg)

</div>

## 1. Introduction

In the world of decision-making and experimentation, **A/B Testing** has long been the go-to method for comparing two options. Imagine you are running an experiment to determine whether version A or version B of a website layout drives more clicks. You split your users into two groups: 50% of users see version A, while the other 50% see version B. After two weeks, you analyze the results to declare a winner. This static allocation of traffic is the hallmark of A/B testing, making it simple and intuitive.

However, there’s a catch. A/B testing treats all users the same, ignoring the fact that different user groups may respond differently. For example, while version A might work well for frequent shoppers, version B could be better suited for casual visitors. But during an A/B test, this difference remains unnoticed until the test concludes, potentially leaving value on the table.

This is where **Multi-Armed Bandits (MAB)** come in. Unlike A/B testing, MAB dynamically adjusts traffic allocation based on performance. If version A starts performing better after the first few days, the algorithm automatically increases traffic to version A, reducing the exposure to version B. This dynamic nature ensures faster optimization and better overall outcomes. Yet, even MAB has a limitation—it ignores user characteristics. What if version A works better for some users but not others?

**Contextual Bandit** is an extension of MAB algorithm. Taking dynamic traffic allocation a step further, Contextual Bandits consider user-specific features—such as demographics, behavior, or preferences—to decide which option to serve. For example, if the algorithm learns that frequent shoppers prefer version A, it will show them version A more often, while steering casual visitors toward version B. This personalized approach optimizes outcomes for each user group in real-time.

<div align="center">

![#](./images/Screenshot%202024-11-17%20160833.png)

</div>

In this guide, we will walk through these method Contextual Bandit—step by step. **Let’s start!**

## 2. Key Components

1. **Context Representation**:
   The context `x` can be a vector of features representing the environment, user preferences, or any relevant information.
   
2. **Action Space**:
   A set of possible actions `{a_1, a_2, ..., a_k}`, where `k` is the number of actions.

3. **Reward Signal**:
   After taking action `a`, a reward `r` is observed, which serves as feedback for learning.

4. **Policy**:
   The policy `π` is the decision-making function that chooses actions based on the context.

<div align="center">

![#](./images/download.jpeg)

</div>

## 3. Contextual Bandits vs Full Reinforcement Learning (RL)
While contextual bandits extend the multi-armed bandit problem to incorporate contexts, they are simpler than the full RL problem. Here's how they compare:

### 3.1. Similarities to Full RL
- **Learning a policy**: Contextual bandits involve mapping situations (contexts) to actions, much like RL.
- **Dynamic decision-making**: The agent adapts its behavior based on the observed context.

### 3.2. Differences from Full RL
- **Immediate reward**: In contextual bandits, actions affect only the **immediate reward**. There is no consideration of how actions impact future situations or rewards.
- **No state transitions**: Contextual bandits assume the context for each round is independent, whereas full RL involves learning how actions influence the state transitions in an environment.

### 3.3. Why Contextual Bandits?

**Contextual bandits** provide a practical framework for scenarios where:
- Decisions depend on contextual information.
- Immediate rewards are the sole focus, without concern for future impacts.

This makes them highly applicable in fields such as:
- Personalized recommendations (e.g., choosing ads based on user profiles).
- Dynamic pricing (e.g., adjusting prices based on market signals).
- Clinical trials (e.g., assigning treatments based on patient characteristics).

A few examples should make this distinction clearer. Let’s say that we are building a system to decide what ads to show to users based on their age. We would expect that users from different age groups may find different ads more relevant to them, which means that a user’s age should affect what ads we should show them. However, the ad we showed them doesn’t in turn affect their age, so the one-step assumption of CB seems to hold. However, if we move one step further and find out that serving expensive ads deplete our inventory (and limit which ads we can serve in the future) or that the ad we show today affect whether the user will visit our site again, then the one-step assumption is indirectly inviolated, so we may want to consider developing a full-blown RL system instead.


## 4. Exploration and Exploitation in Contextual Bandits
One of the central challenges in contextual bandits, as well as in other reinforcement learning tasks, is the **exploration-exploitation tradeoff**. This involves balancing two competing objectives:

1. **Exploitation**: Leveraging existing knowledge to select the action that appears to provide the highest reward based on past observations.
2. **Exploration**: Testing less certain actions to gather new information that could potentially lead to higher rewards in the future.

This tradeoff is critical in contextual bandits, where the agent must not only choose actions but also consider how the observed context influences its decision.

---

### 4.1. Why Exploration and Exploitation Are Important?

Imagine the following scenario:
- You are designing a personalized recommendation system for a streaming service.
- For each user `context`, you recommend a movie `action` and observe their engagement `reward`.

If you **only exploit** the current best recommendation for similar users:
- You might **miss out** on discovering new or better movies for different user groups.
- Additionally, the initial rewards might not have converged to the **true optimal rewards**, leading to suboptimal decisions.

If you **only explore**, trying random recommendations without leveraging past data:
- The overall system performance might **suffer** due to suboptimal suggestions.

An effective **contextual bandit algorithm** needs to strike the right balance between exploring new possibilities and exploiting known high-reward actions.

### 4.2. Examples

<div align="center">

![#](./images/Screenshot%202024-11-18%20002951.png)

</div>

**Exploitation**:
- Items such as Nike, Adidas, and Puma are categorized as **"Similar Items based on History"**.
- This represents leveraging **what is already known** about the user's preferences or previous interactions.
- **Exploitation** involves recommending these high-confidence items that align with the user's historical data to maximize immediate rewards.

**Exploration**:
- Items marked as **"New Brand"** are categorized as **"Low-confidence Items"**.
- This represents exploring **new possibilities or untested options**, which might not align with the user's previous behavior but could help discover new preferences.
- **Exploration** is critical for long-term learning, ensuring the system doesn’t overly rely on historical data and can adapt to unknown preferences.


## 5. Contextual Bandit Algorithm

In **contextual bandits**, at each round `t`, a context $$c_t$$ is provided. This information helps the **learner** decide which **action** $$A_t$$ to take from `k` arms.  
After choosing $$A_t$$, the learner receives a **reward** $$x_{t, A_t}$$ corresponding to the chosen arm.  
The goal of the **learner** is to select actions in a way that **maximizes the total reward** after `n` rounds.  
However, since the **learner** does not know the rewards of the arms in advance, the action selection process may not be optimal, leading to **regret**.

**Regret measures** the "loss" of the learner compared to the optimal policy in hindsight (knowing all the information beforehand).

In the case of **contextual bandits**, each context  `c in C` may have a different optimal arm. Therefore, to compute regret, we compare the learner's actual total reward with the total reward of the **optimal context-dependent policy**.

$$R_n = \mathbb{E} \left[ \sum_{c \in C} \max_{i \in [k]} \sum_{t \in [n] : c_t = c} \left( x_{t, i} - x_{t, A_t} \right) \right]$$

- $$\sum_{t \in [n]: c_t = c}$$
    * Gathers all rounds `t` where the context `c_t = c`.
    * This allows us to group rounds by context.
    * For each context `c`, we calculate regret separately

- $$\max_{i \in [k]} \sum_{t \in [n]: c_t = c} x_{t, i}$$
    * Computes the total reward of the optimal arm for context `c`.
    * For each context `c`, there is an optimal arm `i` in hindsight (the arm that would yield the highest total reward if always chosen for `c`).


- $$x_{t, i} - x_{t, A_t}$$
    * Regret at a single round `t`: the difference between the reward of the optimal arm $$x*{t, i}$$ and the reward of the arm chosen by the learner $$x_{t, A_t}$$.

- $$\mathbb{E}[\cdot]$$
    * Takes the expectation to ensure the formula applies in cases where the learner uses a randomized algorithm (e.g., selecting actions based on a probability distribution).

### 5.1. Example
Let’s consider the following setup:

- `n = 6`: 6 rounds.  
- `k = 3`: 3 arms.  
- Contexts $$c_t$$ belong to the set $${c_1, c_2}$$.  
- Reward matrix $$x_{t, i}$$:

<div align="center">

| Round t  | Context $$c_t$$ | Arm 1 $$x_{t,1}$$ | Arm 2 $$x_{t,2}$$ | Arm 3 $$x_{t,3} $$ |
|-----------------|--------------------|-----------------------|-----------------------|-----------------------|
| 1               | $$c_1$$          | 0.5                   | 0.6                   | 0.3                   |
| 2               | $$c_1$$          | 0.4                   | 0.7                   | 0.5                   |
| 3               | $$c_2$$          | 0.8                   | 0.6                   | 0.4                   |
| 4               | $$c_2$$          | 0.9                   | 0.5                   | 0.7                   |
| 5               | $$c_1$$          | 0.5                   | 0.6                   | 0.2                   |
| 6               | $$c_2$$          | 0.7                   | 0.8                   | 0.3                   |

</div>

#### Optimal Reward for Each Context (Hindsight)
- For $$c_1$$:  
  The optimal arm is arm 2, with a total reward of:  **0.6 + 0.7 + 0.6 = 1.9**
- For $$c_2$$:  
  The optimal arm is arm 1, with a total reward of:  **0.8 + 0.9 + 0.7 = 2.4**

#### Learner’s Actions (Example)
Let’s assume the learner chooses the following arms for each round:
- $$A_1 = 1 $$, $$A_2 = 2$$, $$A_3 = 2$$, $$A_4 = 3$$, $$A_5 = 1$$, $$A_6 = 3$$.

#### Learner’s Reward
The rewards obtained by the learner are:
$$
x_{t, A_t} = 0.5 + 0.7 + 0.6 + 0.7 + 0.5 + 0.3 = 3.3
$$

#### Regret Calculation
- For $$c_1$$:  
  Total reward collected by the learner:  **0.5 + 0.7 + 0.5 = 1.7**
 
  Regret for $$c_1$$: **1.9 - 1.7 = 0.2**

- For $$c_2$$:  
  Total reward collected by the learner: **0.6 + 0.7 + 0.3 = 1.6**

  Regret for $$c_2$$: **2.4 - 1.6 = 0.8**

#### Total Regret
The total regret is the sum of the regrets for $$c_1$$ and $$c_2$$:
$$R_n = 0.2 + 0.8 = 1.0$$

### 5.2. Algorithms
[Check this blog](https://hackernoon.com/contextual-multi-armed-bandit-problems-in-reinforcement-learning)
[Check this book](https://tor-lattimore.com/downloads/book/book.pdf)

## 6. Demo
[Notebook](https://colab.research.google.com/drive/11X2qPYKlPdaAJivUoMEY1oVNBClGfm6h?usp=sharing)

## References
[An-overview-of-contextual-bandits](https://towardsdatascience.com/an-overview-of-contextual-bandits-53ac3aa45034)  

[Dynamic-traffic-allocation](https://www.kameleoon.com/blog/dynamic-traffic-allocation)

[Contextual-bandit-for-marketing-treatment-optimization](https://www.aboutwayfair.com/careers/tech-blog/contextual-bandit-for-marketing-treatment-optimization)

[Neural Contextual Bandits for Personalized Recommendation](https://www.youtube.com/watch?v=uzD-hRuH0s0)

