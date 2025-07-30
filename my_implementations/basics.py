# basics of fiance calculations
import math

"""
Basic Financial Instruments:
1. Equities - stocks(ownership in a company)
2. Fixed Income Securties - bonds(loan made by investor to a borrower) interert payments - coupon payments
3. Derivatives - financial contracts whose value is derived from the price of an underlying asset
4. Alternative Investments

"""

def risk_return(i=1, n, p, r):
    expected_return = 0 # p is the probabiility of outcome i, r is the return of outcome i
    for j in range(i, n):
        expected_return += p[j] * r[j]
    return expected_return

# PV = present value, r = interest rate, n = number of periods, FV = future value
def future_value(present_value, r, n):
    future_value = present_value * ((1 + r) ** n)
    return future_value
def present_value(future_value, r, n):
    present_value = future_value / ((1 + r) ** n)
    return present_value

# mean - average set of returns
def mean(i=1, n, returns):
    total = 0
    for j in range(i, n):
        total += returns[j]
    return total / n

# variance - measure of the dispersion of returns around the mean
def variance(i=1, n, returns):
    avg = mean(i, n, returns)
    total = 0
    for j in range(i, n):
        total += (returns[j] - avg) ** 2
    return total / n

# standard deviation - average amount returns deviate from the mean
def standard_deviation(i=1, n, returns):
    return math.sqrt(variance(i, n, returns))

# covariance - measure of how two assets of returns move together
# same direction = positive covariance
# different direction = negative covariance
def covariance(i=1, n, returns_x, returns_y):
    avg_x = mean(i, n, returns_x)
    avg_y = mean(i, n, returns_y)
    total = 0
    for j in range(i, n):
        total += (returns_x[j] - avg_x) * (returns_y[j] - avg_y)
    return total / n - 1

# correlation - standardized measure of covariance
# ranges from -1 to 1
def correlation(i=1, n, returns_x, returns_y):
    cov = covariance(i, n, returns_x, returns_y)
    std_x = standard_deviation(i, n, returns_x)
    std_y = standard_deviation(i, n, returns_y)
    return cov / (std_x * std_y)

# CAPM - framework for determining the expected return of an asset based on its risk related to the market
# beta - voliatility
# market risk premium = expected market return - risk-free rate
def capital_asset_pricing_model(risk_free_rate, beta, expected_market_return):
    expected_return = risk_free_rate + beta * (expected_market_return - risk_free_rate)
    return expected_return

# APT - extension of CAPM that considers multiple risk factors
def arbitrage_pricing_theory(risk_free_rate, beta, risk_premiums):
    expected_return = risk_free_rate
    for i in range(len(risk_premiums)):
        expected_return += beta[i] * risk_premiums[i]
    return expected_return