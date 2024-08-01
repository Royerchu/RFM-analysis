# RFM-analysis

Reference: https://www.kaggle.com/code/ekrembayar/rfm-analysis-online-retail-ii

## RFM Analysis

RFM is a data-driven customer segmentation technique that allows marketers to take tactical decisions.

**Recency:** How recently did the customer purchase?  INTERACTION with the brand are more likely to respond to new marketing efforts 
**Frequency:** How often do they purchase? How DEEPLY a customer is engaged with your brand
**Monetary value:** How much do they spend? More likely to SPEND MORE in the future



## Questions before planning the new metrics:

**Why need to scale them?**   
	- Need to know the Top 10%, the scale of 9=the second 10%   
	- If we don't scale it, we cannot know whether is high or low, since different industry will present different figure. So it will hard to define  
	- After scaling, R, F, M can be calculated together, since these three metrics should be considered at the same time.  

**Why I need to know RFM, what is the contribution for the company?**  
	- To know and category the customer segment  
	- Based on history to predict new customer behavior  
	- Lead to response rates, customer retention rate, customer satisfaction, and customer lifetime value (CLTV)   
	- Segment can create a relevant, personalized offer for a high-value customer  
 (so if I can find high-value customer, and make more offers and incentives, the company can earn more through the target customer)  

 **About the scaling:**  
	1. Min-Max Scaling  
	2. Standardization(Z-score)  
	3. Log Transformation

 ## Step by step for RFM analysis:
**STEP 1**: Assign Recency, Frequency, Monetary values (after scaling, average them. Reference: https://clevertap.com/blog/rfm-analysis/)  
**STEP 2**: Divide customer into Tiers  
**STEP 3**: Create customer groups  
**STEP 4**: Craft specific messaging  

## How to scale the RFM?
How many scale should I divide?  
The first 20%--> The scale=5  
The second 20% --> The scale =4  

OR

The first 10% --> The scale=10  
The second 10% --> The scale=9  

What will be the difference?  
- Broad Analysis: general trend analysis  
- Detailed Analysis : in-depth analysis

**My insights:** When planning the scale, it is important to consider the company's goals and the industry. In this project, the dataset is for the retail business. It should anticipate customers with higher scores for recency and frequency compared to monetary scores. Thus,  the RFM score could be calculated by giving more weight to R and F scores than M.

## New customer group creation:
**Champions**: select the top 25% with the highest scores of Weighted Average RFM Score.  
**Potential Loyalists**: select the group from the median to the top 25%.  
**At Risk Customers**: Select customers from the 25th percentile to the median of Weighted Average RFM Score.  
**New Customers**: select the group from the minimum to 25th percentile of the Weighted Average RFM Score.  



