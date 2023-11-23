# Python for Finance Final Project
Antoine CIBLAT

# Introduction 

In this final project, I chose to focus on the Modern Portfolio Theory (MPT), a pioneering
concept in financial management developed by economist Harry Markowitz. At the core of
this theory lies the essence of contemporary portfolio management. MPT is grounded in
fundamental principles such as diversification and maximizing returns.
A central pillar of MPT is diversification, which involves distributing investments across a
wide range of assets with low correlation in performance. This intentional diversification
enables investors to reduce the overall risk of their portfolio without significantly
compromising the anticipated returns.
The theory also considers the balance between expected returns and the level of risk. The
goal is to achieve an optimal balance where the return is satisfactory while minimizing the
level of risk. This compromise is evaluated through the Sharpe ratio. A ratio between 0 and 1
indicates that the portfolio's excess return over the risk-free rate is lower than the risk
incurred. A ratio above 1 signifies that the portfolio outperforms a risk-free investment,
demonstrating superior profitability.
Taking into account various indicators such as asset correlation and the risk/return ratio
enables investors to make more informed and optimal decisions regarding allocation and
setting return and risk objectives.
In this project, my primary objective was to construct a portfolio composed of assets with
minimal correlation to the overall market, aiming to significantly minimize the portfolio's risk
while targeting an attractive expected return.
Within this study, I developed two distinct portfolios, each aiming for specific objectives.
The first portfolio was primarily designed based on correlations between assets. The
underlying strategy was founded on the belief that over the long term, investment risk
decreases, particularly when selected actions display no correlation. This approach
emphasized maximizing performance without particular attention to risk levels.
As for the second portfolio, the goal was to integrate the notion of risk more prominently. In
its construction, I considered both the correlation between assets and the risk/return ratio.
The objective was to create a more efficient portfolio, optimizing the relationship between
expected returns and the level of risk.
To achieve these objectives, I utilized the Python programming language to acquire and
analyze historical asset data. This analysis involved calculating essential parameters such as
volatility, expected return, and correlation among different tickers from the period spanning
2000 to 2023. The choice of this timeframe aimed to account for past crises, offering insight
into each asset's behavior during these periods of financial disruption.


# I. First portfolio

To create this first portfolio, I selected several tickers that seemed interesting to me. I aimed
to emphasize innovative companies heavily investing in artificial intelligence such as Amazon,
Microsoft, Nvidia, Meta, Tesla. Other tickers were chosen based on industry sectors:
prominent banking entities (BNP), energy sector (Total), aviation (Airbus), automotive
(BMW), and retail (Walmart). In total, I selected around thirty tickers.
To define my initial portfolio comprising approximately 10 tickers, I initially made a selection
based on correlations. I generated a matrix of all the chosen titles using Python. Then, I
manually selected the tickers of interest that displayed negative correlations among
themselves (see Appendix 1).
This matrix indicates negative correlations (in green) among several tickers. For instance,
DBK.DE and MDLZ stocks are significantly uncorrelated at -0.7577. This negative correlation
suggests a tendency to move in opposite directions: when the price of one stock decreases,
the other tends to increase. This relationship holds particular importance during sectoral
crises, as theoretically, these two stocks would not experience a significant simultaneous
decline. This offers some stability to the portfolio, potentially reducing the negative impact of
a sectoral crisis on overall investments.
I then created code to calculate both the returns and volatility (risk) of each of these tickers
based on historical data (2000-2023). With this information, I computed the Sharpe ratio for
the tickers. I utilized this ratio to optimize the weight of each action using Python code. I
listed the tickers of interest, and based on the Sharpe ratio, I generated and tested several
combinations (2000) to find the most effective combination for my portfolio, aiming for the
highest possible Sharpe ratio.
Subsequently, using the proportions obtained from the calculations performed with Python, I
assessed the returns, volatility, and overall Sharpe ratio of the portfolio (see Appendix 2).
This table presents the fundamental characteristics of the portfolio composed of ten
uncorrelated actions. The total risk, evaluated at 0.242, denotes a relatively moderate
measure, while the overall return is around 9%, surpassing the risk-free rate estimated at 3%
(Livret A rate). However, the Sharpe ratio shows a low value, assessed at 0.262, indicating
relatively low excess return for each unit of risk incurred by the portfolio.
Despite the portfolio demonstrating a moderate level of risk (0.242) and an interesting
overall return, the Sharpe ratio suggests that the additional return compared to a risk-free
asset does not adequately compensate for this volatility, reflected in the low Sharpe ratio.
Generally, a higher Sharpe ratio is preferable as it signifies a better trade-off between return
and risk, a key goal for investors.
Although the portfolio exhibits a relatively moderate level of risk and an attractive overall
return, the Sharpe ratio might suggest inefficiency in managing risk concerning the generated
return. This might necessitate rebalancing or reassessing the portfolio composition to
optimize this return-risk relationship.

# II. Second portfolio

The second portfolio aimed to optimize the Sharpe ratio to surpass the risk-free rate,
considering the portfolio's risk level.
Its construction involved a wider selection of assets, comprising nearly fifty values from the
CAC40, S&P500, and NASDAQ indices. Similar to the previous portfolio, I calculated returns
and risks associated with each asset using Python. Following this, I created the correlation
matrix for all assets (see Appendix 3) and produced the Markowitz chart, placing assets on a
graph based on their Sharpe ratios (see Appendix 4).
To select the ten assets comprising the portfolio, I initially filtered correlations below 0.4 to
ensure adequate diversification. Then, I ranked the Sharpe ratios of these assets to retain
only the top ten values. This approach, combining relatively low correlations with the highest
possible Sharpe ratios, optimizes the portfolio composition.
For determining the optimal weights for each asset, I used an iterative process again to
identify the most performing combination (see Appendix 5). The result of this strategy
translates to an expected return of 34%, a risk evaluated at 0.38, and a significantly higher
Sharpe ratio than that of the previous portfolio, reaching 0.81. This higher Sharpe ratio
reflects a substantial excess return relative to the assumed level of portfolio risk,
demonstrating a more favorable risk-adjusted performance.
This second portfolio is theoretically more efficient, making it wiser to consider it over the
first one. Its returns are higher, and the overall risk is comparatively lower. In theory, for the
same invested amount and duration, the second portfolio would ensure a greater return on
investment.
However, it's important to note that these models are based on historical data (2000-2023)
to make estimations about the future, assuming that past behaviors of stocks might reflect
future behaviors.
