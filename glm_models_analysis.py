# Import necessary libraries
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

# Set matplotlib configurations for better visualization
plt.rc("figure", figsize=(16, 8))
plt.rc("font", size=14)

# Section 1: Gamma Family Model with Default Link Function
def gamma_family_model():
    print("Running Gamma Family Model...")
    data = sm.datasets.scotland.load()
    data.exog = sm.add_constant(data.exog)

    # Instantiate and fit the model
    gamma_model = sm.GLM(data.endog, data.exog, family=sm.families.Gamma())
    gamma_results = gamma_model.fit()
    print(gamma_results.summary())

gamma_family_model()

# Section 2: Logistic Regression with GLM
def logistic_regression():
    print("Running Logistic Regression Model...")
    # Load the dataset
    star98 = sm.datasets.star98.load_pandas().data

    # Define the formula
    formula = ("SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + "
               "PCTYRRND + PERMINTE * AVYRSEXP * AVSALK + PERSPENK * PTRATIO * PCTAF")
    dta = star98[[
        "NABOVE", "NBELOW", "LOWINC", "PERASIAN", "PERBLACK", "PERHISP",
        "PCTCHRT", "PCTYRRND", "PERMINTE", "AVYRSEXP", "AVSALK",
        "PERSPENK", "PTRATIO", "PCTAF"
    ]].copy()
    dta["SUCCESS"] = dta["NABOVE"] / (dta["NABOVE"] + dta["NBELOW"])

    # Fit GLM model
    mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
    print(mod1.summary())

logistic_regression()

# Section 3: GLM Binomial Response
def glm_binomial_response():
    print("Running GLM Binomial Response...")
    data = sm.datasets.star98.load()
    data.exog = sm.add_constant(data.exog, prepend=False)

    # Fit the model
    glm_binom = sm.GLM(data.endog, data.exog, family=sm.families.Binomial())
    res = glm_binom.fit()
    print(res.summary())

    # Analyze model
    means = data.exog.mean(axis=0)
    means25 = means.copy()
    means25.iloc[0] = stats.scoreatpercentile(data.exog.iloc[:, 0], 25)
    means75 = means.copy()
    means75.iloc[0] = stats.scoreatpercentile(data.exog.iloc[:, 0], 75)

    resp_25 = res.predict(means25)
    resp_75 = res.predict(means75)
    diff = resp_75 - resp_25
    print(f"Difference in Response: {diff * 100:.4f}%")

glm_binomial_response()

# Section 4: Gamma Model for Proportional Count Response
def glm_gamma_response():
    print("Running Gamma Model for Proportional Count Response...")
    data2 = sm.datasets.scotland.load()
    data2.exog = sm.add_constant(data2.exog, prepend=False)

    # Fit the model
    glm_gamma = sm.GLM(data2.endog, data2.exog, family=sm.families.Gamma(sm.families.links.log()))
    glm_results = glm_gamma.fit()
    print(glm_results.summary())

glm_gamma_response()

# Section 5: Gaussian Distribution with Noncanonical Link
def glm_gaussian_response():
    print("Running Gaussian Distribution Model...")
    # Example data
    lny = np.log(np.random.rand(100))  # Placeholder for response variable
    X = sm.add_constant(np.random.rand(100, 3))  # Placeholder for predictor variables

    # Fit the model
    gauss_log = sm.GLM(lny, X, family=sm.families.Gaussian(sm.families.links.log()))
    gauss_log_results = gauss_log.fit()
    print(gauss_log_results.summary())

glm_gaussian_response()
