# post-learn-earn

This repository contains project that visualize how much the college grads from different majors are earning after completing their education.

### Objectives

Below is the list of questions that we are looking to answer as a final outcome of this project:

*  How much the college grads from different majors are earning after completing their education?

### Goal Significance

Why do we need the earning data for college majors? What benefit we could derive by visualizing the 
earning data comparison between various college major grads? Below are the goals we can enlist: 

* This information will give us an idea about the current market trends: i.e. 
	* Understand the types of skill set are in demand
	* What are the extent of demand for various skills in general and in combination thereof 
under various fields. 

* This will help us to structure our future college course structure that can fulfil the industry 
requirements and help develop best placement opportunities for our future students. 

* This inference would also help us to frame our long-term & short-term goals and align the 
research activities with the industry demand/trends.

### Data

#### Data Source

The original data on job was released by American Community Survey, which conducts 
surveys and aggregates the data and available at:  
https://www.census.gov/programs-surveys/acs/ 

The data set cleaned by FiveThirtyEight is available for download at: 
https://github.com/fivethirtyeight/data/tree/master/college-majors

#### Data Lists
The data is available in the .csv file format. File name: recent-grads.csv 

### Data Extraction Details

The dataset shows different major in college in every row that contains information on 
student gender diversity, their employment rates, overall median salaries, etc. Some of the 
columns that carry info of our interest are:

Rank - Rank by median earnings (the dataset is ordered by this column).
Major_code - Major code.
Major - Major description.
Major_category - Category of major.
Total - Total number of people with major.
Sample_size - Sample size (unweighted) of full-time.
Men - Male graduates.
Women - Female graduates.
ShareWomen - Women as share of total.
Employed - Number employed.
Median - Median salary of full-time, year-round workers.
Low_wage_jobs - Number in low-wage service jobs.
Full_time - Number employed 35 hours or more.
Part_time - Number employed less than 35 hours.

### Highlights of the code. 
 
#### Software packages used:  
* Python
* Pandas
* Numpy
* Matplotlib.pyplot

#### Overview:

* Read the data and form the data frame
* Identify the relevant info and segregate it
* Plot scatter diagram to understand their correlations
* Plot histogram to understand the data distribution
* Plot scatter matrix to visualize the overall picture of data dependencies
* Generate bar charts to review and interpret the info
* Prepare box plot to get the data statistics
* Create Hexagonal Bin Plot to visualize data density 

### Visualize the results.

####  Scatter Plots to Review Data Correlations

![output_5_1](https://user-images.githubusercontent.com/33802087/40482513-c5b548f8-5f72-11e8-

864f-79a7e235c1fe.png)

![output_6_1](https://user-images.githubusercontent.com/33802087/40482520-c8ed4f34-5f72-11e8-

8085-9ba354b235f5.png)

![output_7_1](https://user-images.githubusercontent.com/33802087/40482531-d0e02680-5f72-11e8

-8879-5e72dbc557de.png)

![output_8_1](https://user-images.githubusercontent.com/33802087/40482537-d32d13da-5f72-11e8

-8a39-582dece0a824.png)

![output_9_1](https://user-images.githubusercontent.com/33802087/40482540-d5525c10-5f72-11e8

-8237-6e6fb97cf7bd.png)

![output_10_1](https://user-images.githubusercontent.com/33802087/40482544-d8ccf4b8-5f72-11e8

-9c45-5b7a8d5aa990.png)

#### Histograms to Verify Data Distribution

![output_12_1](https://user-images.githubusercontent.com/33802087/40482649-23c9df30-5f73-11e8

-9d6e-1bb6056dd47a.png)

![output_13_1](https://user-images.githubusercontent.com/33802087/40482651-24bfa8de-5f73-11e8

-97cf-4e1e83420598.png)

![output_14_1](https://user-images.githubusercontent.com/33802087/40482655-26a2ddd8-5f73-

11e8-869a-251cd48e2e07.png)

![output_15_1](https://user-images.githubusercontent.com/33802087/40482656-28199b02-5f73-

11e8-8004-774591c72303.png)

![output_16_1](https://user-images.githubusercontent.com/33802087/40482663-2aca3244-5f73-

11e8-82b3-2d5ee2f1aa33.png)

![output_17_1](https://user-images.githubusercontent.com/33802087/40482667-2d12d68c-5f73-

11e8-8a09-88f10ef4a170.png)

![output_18_1](https://user-images.githubusercontent.com/33802087/40482668-2f817810-5f73-11e8

-8a6e-173bb655dde8.png)

![output_19_1](https://user-images.githubusercontent.com/33802087/40482675-318f056e-5f73-11e8

-85d3-c3a1947414fd.png)

#### Scatter Matrix Plot for Data Statistics 

![output_21_1](https://user-images.githubusercontent.com/33802087/40482732-57c1fc50-5f73-11e8

-86ce-59e659953656.png)

#### Scatter Matrix Plot for Unemployment Rate

![output_22_1](https://user-images.githubusercontent.com/33802087/40482753-67b36428-5f73-

11e8-9fe2-d217582b8f7a.png)

#### Women Proportions in Different Majors

![output_24_0](https://user-images.githubusercontent.com/33802087/40482786-82d8e70a-5f73-

11e8-944d-690556b34b41.png)

![output_24_1](https://user-images.githubusercontent.com/33802087/40482787-8323f7a4-5f73-11e8

-9433-7da43e92aef3.png)

#### Unemployment Rates in Different Majors

![output_26_0](https://user-images.githubusercontent.com/33802087/40482820-a53c5d72-5f73-

11e8-81c9-cb3e47628d74.png)

![output_26_1](https://user-images.githubusercontent.com/33802087/40482821-a581d1d6-5f73-

11e8-9ed8-94a732defebf.png)

#### Number of Men & Women in Each Major Category

![output_30_0](https://user-images.githubusercontent.com/33802087/40482868-c559619a-5f73-

11e8-8be0-0df9f010329b.png)

#### Distribution of Median Salaries & Unemployment Rate

![output_32_0](https://user-images.githubusercontent.com/33802087/40482914-e8a5a5a0-5f73-

11e8-82c3-0ee49618a4f9.png)

![output_32_1](https://user-images.githubusercontent.com/33802087/40482915-e8f0285a-5f73-11e8

-9b36-8954364d32b2.png)

#### Hexagonal Bin Plot to Visualize Data Density

![output_35_0](https://user-images.githubusercontent.com/33802087/40482932-f5979336-5f73-11e8

-9cef-dd32e300c8ec.png)

### Explain the results in a simple, concise and easy way. (non-technical audience)

The analysis and results give very useful info to shape our future planning based for:
* Couse mix
* Curriculum based on Industry trends 
* Corporate tie-up for the skill set in demand
* Marketing and segmentations
	
### Explain the results in the most technical way. (technical, data-scientist audience)

* Strong correlation has been observed between:
	* Sample Size vs. Median (of Earnings)
	* Sample Size Vs. Unemployment Rate 
	* Full Time Employment Vs. Median (of Earnings)
	* Men (Gender Specific) Vs. Median (of Earnings)
	* Women (Gender Specific) Vs. Median (of Earnings) 

* No correlation has been observed between:
	* Proportion of Women Vs. Unemployment Rate
	* Unemployment Rate Vs. Median (of Earnings) 

* Data distribution results: 
	* Most of the samples are found of size up to 500.
	* The median annual salary range appears to be 30,000 ? 40,000
	* The distribution of full-time employed grads is found highly skewed 
across the course majors.
	* Distribution of the woman proportion across the course majors appears 
to be uneven, i.e. not normally distributed.
	* Unemployment rate is found following close to the normal distribution 
across the course majors.
	* Gender distribution across the course majors is found highly skewed, indicating a strong 

gender specific inclination towards specific course 
majors. 

* For women, 
	* Following are the top 10% paying majors:
		* Petroleum Engineering, Mining and Mineral Engineering,Metallurgical, Engineering, Naval Architecture and Marine Engineering, Chemical Engineering, Nuclear Engineering, Actuarial Science, Astronomy and Astrophysics, Mechanical Engineering, and Electrical Engineering.

	* Following are the bottom 10% paying majors:
		* Library Science, Counselling Psychology, Clinical Psychology, 
Educational Psychology, Zoology, Composition and Rhetoric, Drama and Theatres, Other Foreign Languages, and Childhood Education. 

* The unemployment rate is found:
	* Higher amongst the following top 10% paying majors:
		* Nuclear Engineering
		* Mining and Mineral Engineering
		* Actuarial Science

	* Lowest amongst the following top 10% paying majors:
		* Petroleum Engineering
		* Astronomy and Astrophysics
		* Metallurgical Engineering

	* Highest amongst the following bottom 10% majors:
		* Clinical Psychology
		* Foreign Languages
		* Library Science

	* Lowest amongst the following bottom 10% majors:
		* Childhood Education
		* Zoology
		* Counselling Psychology

* Gender distribution amongst the major categories:
	* Both, Men and Women are equally inclined towards the following majors:
		* Business
		* Social Science
		* Physical Sciences
		* Low & Public Policy

	* Women prefers following majors to men:
		* Education
		* Humanity & Library Arts
		* Health
		* Psychology & Social Work
		* Communications and Journalism

	* Men prefers following majors to women:
		* Engineering
		* Computers & Mathematics

* Median of Earnings across the majors are as follows: (all numbers are approx.)
	* 25% majors are found having median earnings of up to $32,500
	* 25% majors are found having median earnings of between $32,500 - $36,000
	* 25% majors are found having median earnings of between $36,000 - $45,000
	* 25% majors are found having median earnings of above $45,000

### Conclusion

#### What we learn from this outcome. (non-technical audience)

* By this study, our understanding of the upcoming industry trends and change in the 
demand for the skill sets got improved. This would help us to shape our long-term 
courses proposition and industry tie-up to align with the market demand.

* This analysis can also help us to tune up our course majors based on the high and 
low unemployment rates in different sectors.

* The results can be effectively used to plan and emphasize our marketing efforts in 
appropriate sectors, i.e. we can vigorously focus our marketing over the highly 
paying majors with low unemployment rate while carry out our re-structure efforts 
for low-paying sectors with high unemployment rates.

* The gender specific inclinations for certain majors can also help us to decide about 
our message copy for different market clusters.

####  Technical significance of the results. (technical, data-science audience)

* We learnt correlations between various factors that affect the earnings of grads 
from different majors. 

* We came to know the distribution of various features amongst the clusters such as 
median salary, full-time employment, unemployment rate, gender participations in 
various majors etc.

* We also understand what the high paying and low paying majors for women are. 

* There exist gender specific preferences for different majors: we realized what 
majors men prefers to women and vice versa. 

* We realized what are the top 10% and bottom 10% paying majors wherein the 
unemployment rate was the highest and the lowest. 

* We got info about the Earning quartiles. 

### Suggestion for Further Development

#### How differently you would have done this project, if get a chance to do it again. Why?

In case of gotten second chance to do this project again, I would have:

* Touched upon some more features such as,
	* College jobs,
	* Non-College Jobs
	* 25th & 75th Percentile
	* Part Time Employed, etc.
to develop correlation matrix and determine their influence over the earnings for different course 

majors. 

* Verified the sufficiency of the sample size and come up with the conclusive suggestion about:
	* the data sufficiency 
	* need for more data
	* need for more features to be included in the survey, etc.

* Tried to explore more analytical info that could help to make long-term strategic 
decisions.
	
#### Your suggestions for someone if s/he wants to further continue this work. 

Someone could pick one or more of the untouched data fields, explore and add 
additional features and continue this journey further to cherish more flavors in the 
analysis. S/he could follow some of the suggestions that are mentioned above in the 
second chance effort.
