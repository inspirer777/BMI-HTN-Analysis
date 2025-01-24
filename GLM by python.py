# Load modules and data
import statsmodels.api as sm
data = sm.datasets.scotland.load()
data.exog = sm.add_constant(data.exog)

# Instantiate a gamma family model with the default link function.
gamma_model = sm.GLM(data.endog, data.exog, family=sm.families.Gamma())
gamma_results = gamma_model.fit()
print(gamma_results.summary())


#Logistic Regressio
import statsmodels.api as sm
import statsmodels.formula.api as smf

star98 = sm.datasets.star98.load_pandas().data
formula = "SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \
           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF"
dta = star98[
    [
        "NABOVE",
        "NBELOW",
        "LOWINC",
        "PERASIAN",
        "PERBLACK",
        "PERHISP",
        "PCTCHRT",
        "PCTYRRND",
        "PERMINTE",
        "AVYRSEXP",
        "AVSALK",
        "PERSPENK",
        "PTRATIO",
        "PCTAF",
       ]
   ].copy()
endog = dta["NABOVE"] / (dta["NABOVE"] + dta.pop("NBELOW"))
del dta["NABOVE"]
dta["SUCCESS"] = endog

#GLM model
mod1 = smf.glm(formula=formula, data=dta,family=sm.families.Binomial()).fit()
print(mod1.summary())


def double_it(x):
    return 2 * x


formula = "SUCCESS ~ double_it(LOWINC) + PERASIAN + PERBLACK + PERHISP + \     PCTCHRT + PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF"
mod2 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
print(mod2.summary())


print(mod1.params[1])
print(mod2.params[1] * 2)


#Generalized Linear Models
%matplotlib inline
import numpy as np
import statsmodels.api as sm
from scipy import stats
from matplotlib import pyplot as plt

plt.rc("figure", figsize=(16,8))
plt.rc("font", size=14)

#GLM: Binomial response data
print(sm.datasets.star98.NOTE)

data = sm.datasets.star98.load()
data.exog = sm.add_constant(data.exog, prepend=False)

print(data.endog.head())
print(data.exog.head())


#Fit and summary
glm_binom = sm.GLM(data.endog, data.exog, family=sm.families.Binomial())
res = glm_binom.fit()
print(res.summary())

print('Total number of trials:',  data.endog.iloc[:, 0].sum())
print('Parameters: ', res.params)
print('T-values: ', res.tvalues)


means = data.exog.mean(axis=0)
means25 = means.copy()
means25.iloc[0] = stats.scoreatpercentile(data.exog.iloc[:,0], 25)
means75 = means.copy()
means75.iloc[0] = lowinc_75per =      stats.scoreatpercentile(data.exog.iloc[:,0], 75)
resp_25 = res.predict(means25)
resp_75 = res.predict(means75)
diff = resp_75 - resp_25

print("%2.4f%%" % (diff*100))


#GLM: Gamma for proportional count response
print(sm.datasets.scotland.DESCRLONG)

data2 = sm.datasets.scotland.load()
data2.exog = sm.add_constant(data2.exog, prepend=False)
print(data2.exog.head())
print(data2.endog.head())

#Model Fit and summary
glm_gamma = sm.GLM(data2.endog, data2.exog, family=sm.families.Gamma(sm.families.links.log()))
glm_results = glm_gamma.fit()
print(glm_results.summary())


#GLM: Gaussian distribution with a noncanonical link
gauss_log = sm.GLM(lny, X, family=sm.families.Gaussian(sm.families.links.log()))
gauss_log_results = gauss_log.fit()
print(gauss_log_results.summary())









