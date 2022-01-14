#!/usr/bin/env python
# coding: utf-8

# # Computational Thinking in Engineering Mechanics
# 
# This document examines how computational thinking fits into engineering mechanics courses at TTU in particular:
# 
# :::{note}
# This page and similar are one faculty member's professional interpretation of the task to integrate, or downstream common year 1 items into the CECE curriculum.  Specifically, in this case, Computational Thinking.  There are similar treatises for the other two common topics; Nature Inspired Design, and Socio-Technological Aspects of Engineering.
# :::
# 
# ## Background
# Jeannette Wing, 2006 [http://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf](http://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf) coined the term “computational thinking” (CT) to articulate a vision that everyone, not just those who major in computer science, can benefit from thinking like a computer scientist, but afterwards gave the following definition of CT:
# 
# >*Computational Thinking is the thought processes involved in formulating problems and their solutions so that the solutions are represented in a form that can be effectively carried out by an information-processing agent* 
# 
# The ongoing interpretation of that original vision is that computational thinking is a problem-solving process that includes the following characteristics (Varela and others, 2019):
# 
# :::{note}
# These characteristics are essentially uncontested, Dogma if you will.
# :::
# 
# - Formulating problems in a way that it is **possible** to use a computer and **other tools** in their resolution.
# - Organizing data logically and analyzing them.
# - Representing data through abstractions.
# - Automating solutions.
# - Identifying, analyzing and implementing possible solutions in order to obtain the most effective combination.
# - Generalizing and transferring this process to a wide variety of solutions.
# 
# The remainder of this document examines each item in depth.
# 
# ### Problem Formulation 
# 
# With the above concepts in play CT in Mechanics would implement the first item unchanged from the past as to how statics problems are formulated. **Past problem formulation approaches are valid, effective, and fit the CT paradigm - no modification necessary**. There will be some value to selecting some problems with a computer solution in mind, but nothing special is needed.
# 
# ### Data Organization
# 
# The second concept of CT in Mechanics refers to data organization.  The past methods of listing *known* values (and their sources such as table look-up) and *unknown* or sought values is still valid and effective.  A listing of governing principls to be applied $F=m \cdot a$ and such will continue to suffice to satisfy the task
# *Organizing data logically and analyzing them.*  The adverb or adjective (not sure of author's intent) "logically" is a value judgement; the clause *analyzing them* is vague and obviously an obfuscation.   In CECE Mechanics Courses a listing of known,unknown, and governing equations will suffice and be emphasized, citation of data sources (URL, or tables in books) is considered vital and is also emphasized.  As in the previous item **Past problem formulation approaches are valid, effective, and fit the CT paradigm - no major modification necessary; emphasis on data source identification needs inclusion/emphasis**.
# 
# ### Data Abstraction
# 
# The next item in the list *Representing data through abstractions* as a practical matter refers to model(s) of the mechanics under consideration.  In past and present contexts the sketching of a situation and formulation of sets of equations describing the kinematics, forces, and accelerations constitutes the major abstraction.  The replacement of distributed forces with equivalent point forces and similar superpositional-type models are typical abstractions.  
# 
# As such, drawing the Free-Body Diagram (FBD) and substitution of user-defined forces into the governing equations of the previous component is data abstraction!  If the data are stochastic in some sense then their explicit values being replaced with an estimate from their underlying probability distribution would similarily be data abstraction.  
# 
# In CECE Mechanics Courses 
# 
# - a drawing of a coordinate system, 
# - a FBD (or multiple diagrams as necessary, especially if there are contact forces involved), 
# - naming and line of application conventions for the forces comprises the major data abstraction activity.
# - substitution of these named forces into governing equations
# 
# constitutes data abstraction and creates the data model for the problem.  **Past problem formulation approaches regarding the abstraction/modeling step are valid, and fit the CT paradigm - no major modification necessary**
# 
# ### Automating solutions
# 
# The automation of solutions (need more verbiage here)
# 
# **Past problem approaches need modification to provide practice in automation.  One approach is to build a generic solution, but to emphasize auotmation, provide multiple inputs and require each case be solved.  Enough cases will force automation** The instructor needs to be open to the possibility of an entire class conspiring to manually handle each input - but thats teamwork, something else to be encouraged!
# 
# ### Assessing possible solutions to obtain the most effective combination.
# 
# This is a bullshit characteristic, but will work up something
# 
# - Do nothing "solution"
# - Steal IP from someone else "solution"
# - Beat to death with numerics (that sounds computational!)
# - Throw money at the problem, let the crowd find an answer
# - 
# 
# ### Generalizing to a wide variety of solutions
# 
# Also somewhat bullshit.  See "automation" above.  Concievably generic "solvers" in an on-line venue handles generalization. Then problem formulation is the vital step.

# ## References
# 
# 1. Wing, J. (2006). *Computational Thinning* COMMUNICATIONS OF THE ACM March 2006/Vol. 49, No. 3. [http://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf](http://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf)
# 
# 2. Concepción Varela, Carolina Rebollar, Olatz García Eugenio, and Bravo Javier Bilbao. (2019) *Skills in computational thinking of engineering students of the first school year* Helyion. Vol. 5, No. 11, DOI: [https://doi.org/10.1016/j.heliyon.2019.e02820](https://doi.org/10.1016/j.heliyon.2019.e02820)

# In[ ]:




