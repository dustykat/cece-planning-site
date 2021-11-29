#!/usr/bin/env python
# coding: utf-8

# # CE 3354 Engineering Hydrology

# ## Evaporation Trend Examination using Data Science 
# 
# A downstream application of ENGR-1330
# 
# Contributed by Theodore Cleveland
# 
# ---

# :::{note}
# **Prerequesites (for this example)
# >- Students will have completed ENGR-1330
# >- Students are enrolled in CE 3354
# 
# **Problem Modality**
# >- Data acquisition and analysis using ENGR-1330 methods, internet and library resources
# >- Synthesize findings in a working Jupyter Notebook
# 
# **Special Instructions**
# >- Either individual or group exercise
# >- This problem tests how to directly embed computations into a Jupyter Book, however the code cells are intended for cut-and-paste.
# >- Students have completed similar problems in ENGR-1330; they have the code and knowledge 
# 
# :::

# ## Background
# Global warming is a currently popular and hotly (pun intended) debated issue. 
# The usual evidence is temperature data presented as a time series with various temporal correlations to industrial activity and so forth. The increase in the global temperature is not disputed - what it means for society and how to respond is widely disputed.
# 
# One possible consequence of warming, regardless of the cause is an expectation that
# <strong>evaportation rates would increase</strong> and temperate regions would experience more
# drought and famine, and firm water yields would drop. 
# 
# However in a paper by Peterson and others (1995) the authors concluded from analysis of pan evaporation data in various parts of the world, that there has been a <strong>downward trend in evaporation</strong> at a significance level of 99%. 
# Pan evaporation is driven as much by direct solar radiation (sun shining on water) as by surrounding air temperature.
# 
# Global dimming is defined as the decrease in the amounts of solar radiation reaching the surface of the Earth. The by-product of fossil fuels is tiny particles or pollutants which absorb solar energy and reflect back sunlight into space. This phenomenon was first recognized in the year 1950. Scientists believe that since 1950, the sun’s energy reaching Earth has dropped by 9% in Antarctica, 10% in the USA, 16% in parts of Europe and 30% in Russia – putting the overall average drop to be at an enormous 22%. This causes a high risk to our environment.
# 
# Aerosols have been found to be the major cause of global dimming. The burning of fossil fuels by industry and internal combustion engines emits by-products such as sulfur dioxide, soot, and ash. These together form particulate pollution—primarily called aerosols. Aerosols act as a precursor to global dimming in the following two ways:
# 
# These particle matters enter the atmosphere and directly absorb solar energy and reflect radiation back into space before it reaches the planet’s surface.
# Water droplets containing these air-borne particles form polluted clouds. These polluted clouds have a heavier and larger number of droplets. These changed properties of the cloud – such clouds are called ‘brown clouds’ – makes them more reflective.
# Vapors emitted from the planes flying high in the sky called contrails are another cause of heat reflection and related global dimming.
# 
# Both global dimming and global warming have been happening all over the world and together they have caused severe changes in the rainfall patterns. It is also believed that it was global dimming behind the 1984 Saharan drought that killed millions of people in sub-Saharan Africa. Scientists believe that despite the cooling effect created by global dimming, the earth’s temperature has increased by more than 1 deg. in the last century.
# 
# ### References
# 
# Peterson, T.C., Golubev, V.S. and Groisman, P. Ya. 1995. Evaporation
# losing its strength. Nature 377: 687-688. [https://www.nature.com/articles/377687b0](https://www.nature.com/articles/377687b0)
# 
# A primer on global dimming [https://www.conserve-energy-future.com/causes-and-effects-of-global-dimming.php](https://www.conserve-energy-future.com/causes-and-effects-of-global-dimming.php)
# 
# ## Problem Statement 
# In Texas, evaporation rates (reported as inches per month) are available from the Texas Water Development Board.
# https://waterdatafortexas.org/lake-evaporation-rainfall
# The map below shows the quadrants (grid cells) for which data are tabulated.
# 
# ![figure1](EvapMap.png)
# 
# Cell '911' is located between Corpus Christi and Houston in the Coastal Plains of Texas.  A copy of the dataset downloaded from the Texas Water Development Board is located at http://www.rtfmps.com/share_files/all_quads_gross_evaporation.csv
# 
# Using naive data science anlayze the data for Cell '911' and decide if the conclusions by Peterson and others (1995) are supported by this data.

# :::{note}
# What follows is exploratory analysis for Cell 506.  These steps are a useful guideline for analyzing Cell 911, but alone are insufficient.  Once you can process the dataframe, you can apply your own analysis for Cell 911.
# :::
# 
# **Exploratory Analysis**
# To analyze these data a first step is to obtain the data.  The knowlwdge that the data are arranged in a file with a ``.csv`` extension is a clue how to proceede.  We will need a module to interface with the remote server, in this example lets use something different than ``urllib``. Here we will use ``requests`` , so first we will load the module
# 
# Now we will generate a ``GET`` request to the remote http server.  I chose to do so using a variable to store the remote URL so I can reuse code in future projects.  The ``GET`` request (an http/https method) is generated with the requests method ``get`` and assigned to an object named ``rget`` -- the name is arbitrary.  Next we extract the file from the ``rget`` object and write it to a local file with the name of the remote file - esentially automating the download process. Then we import the ``pandas`` module.
# 
# :::{note}
# The code cell is intentionally suppressed (it does not run when the book is built); but cut-and-paste is enabled
# :::

# ```
# import requests # Module to process http/https requests
# remote_url="http://54.243.252.9/cece-dev-databases/cece-planning-site/ctdslibrary-webroot/ctds-webbook/docs/hydrology/evaporation/all_quads_gross_evaporation.csv"  # set the url
# rget = requests.get(remote_url, allow_redirects=True, verify=False)  # get the remote resource, follow imbedded links, ignore the certificate
# open('all_quads_gross_evaporation.csv','wb').write(rget.content) # extract from the remote the contents, assign to a local file same name
# import pandas as pd # Module to process dataframes (not absolutely needed but somewhat easier than using primatives, and gives graphing tools)
# ```

# Now we can read the file contents and check its structure, before proceeding.

# In[1]:


import pandas as pd # Module to process dataframes (not absolutely needed but somewhat easier than using primatives, and gives graphing tools)
evapdf = pd.read_csv("all_quads_gross_evaporation.csv",parse_dates=["YYYY-MM"]) # Read the file as a .CSV assign to a dataframe evapdf
evapdf.head() # check structure


# Structure looks like a spreadsheet as expected; lets plot the time series for cell '506'

# In[2]:


evapdf.plot.line(x='YYYY-MM',y='506') # Plot quadrant 506 evaporation time series 


# Now we can see that the signal indeed looks like it is going up at its mean value then back down. Lets try a moving average over 12-month windows. The syntax is a bit weird, but it should dampen the high frequency (monthly) part of the signal.  Sure enough there is a downaward trend at about month 375, which we recover the date using the index -- in this case around 1985.
# 

# In[3]:


movingAvg=evapdf['506'].rolling(12, win_type ='boxcar').mean()
movingAvg
movingAvg.plot.line(x='YYYY-MM',y='506')
evapdf['YYYY-MM'][375]
evapdf['506'].describe()


# So now lets split the dataframe at April 1985.  Here we will build two objects and can compare them.  Notice how we have split into two entire dataframes.

# In[4]:


evB485loc = evapdf['YYYY-MM']<'1985-04'  # filter before 1985
evB485 = evapdf[evB485loc]
ev85uploc = evapdf['YYYY-MM']>='1985-04' # filter after 1985
ev85up= evapdf[ev85uploc]
print(evB485.head())
print(ev85up.head())


# Now lets get some simple descriptions of the two objects, and we will ignore thay they are time series.

# In[5]:


evB485['506'].describe()


# In[6]:


ev85up['506'].describe()


# If we look at the means, the after 1985 is lower, and the SD about the same, so there is maybe support of the paper claims, but the median has increased while the IQR is practically unchanged.  We can produce boxplots from the two objects and see they are different, but not by much.  So the conclusion of the paper has support but its pretty weak and hardly statisticlly significant. 

# In[7]:


evB485['506'].plot.box()


# In[8]:


ev85up['506'].plot.box()


# At this point, we would appeal to hypothesis testing or some other serious statistical analysis tools.  Lets try a favorite (of mine) non-paramatric test called the ``mannwhitneyu`` test.  
# 
# ### Background
# In statistics, the Mann–Whitney U test (also called the Mann–Whitney–Wilcoxon (MWW), Wilcoxon rank-sum test, or Wilcoxon–Mann–Whitney test) is a nonparametric test of the null hypothesis that it is equally likely that a randomly selected value from one population will be less than or greater than a randomly selected value from a second population.
# 
# This test can be used to investigate whether two independent samples were selected from populations having the same distribution.
# 
# ## Application
# As usual we need to import necessary tools, in this case scipy.stats.  Based on the module name, it looks like a collection of methods (the dot ``.`` is the giveaway).  The test itself is applied to the two objects, if there is a statistical change in behavior we expect the two collections of records to be different.

# In[9]:


from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(evB485['506'],ev85up['506'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# If there were indeed a 99% significance level, the p-value should have been smaller than 0.05 (two-tailed) and the p-value was quite high.  I usually check that I wrote the script by testing he same distribution against itself, I should get a p-vale of 0.5.  Indeed that's the case.  

# In[10]:


stat, p = mannwhitneyu(evB485['506'],evB485['506'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# Now lets repeat the analysis but break in 1992 when Clean Air Act rules were slightly relaxed:

# In[11]:


evB492loc = evapdf['YYYY-MM']<'1992'  # filter before 1992
evB492 = evapdf[evB492loc]
ev92uploc = evapdf['YYYY-MM']>='1992' # filter after 1992
ev92up= evapdf[ev92uploc]
#print(evB492.head())
#print(ev92up.head())


# In[12]:


stat, p = mannwhitneyu(evB492['506'],ev92up['506'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# So even considering the key date of 1992, there is marginal evidence for the claims (for a single spot in Texas), and one could argue that the claims are confounding -- as an FYI this evevtually was a controversial paper because other researchers obtained similar results using subsets (by location) of the evaporation data.
# 
# ## Homework
# Using  data science tools anlayze the data for Cell '911' and decide if the conclusions by Peterson and others (1995) are supported by this data. That is, do the supplied data have a significant trend over time in any kind of grouping?
# 
# Some things you may wish to consider as you design and implement your analysis are:
# Which summary statistics are relevant? 
# Ignoring the periodic signal, are the data approximately normal? 
# Are the data homoscedastic? 
# What is the trend of the entire dataset (all years)? 
# What is the trend of sequential decades (group data into decades)? 
# What is the trend of sequential 15 year groups? 
# Is there evidence that the slope of any of the trends is zero? 
# At what level of significance?
# 
# Some additional things to keep in mind:
# 
# > - These data are time series; serial correlation is present.
# > - An annual-scale periodic signal is present 
# 
# Peterson and others (1995) only analyzed May through September data,
# does using this subset of data change your conclusions?

# ## Deliverables:
# - Each student is expected to submit one notebook of their analysis.
# > - The notebook should be complete and running, use markdown cells to explain your work. 
# > - The notebook should be uploaded on Blackboard in both PDF format and as IPYNB (two files).
# > - The course-section number, course name, project title, and student names should be shown at the top of the notebook.

# :::{note}
# A modification would be to assign the problem to each student using a different data cell, then in class examine if there is any difference in findings spatially (coastal plains vs. East Texas vs. North and West Texas).
# 
# Instructors can also explore other states
# :::

# In[ ]:




