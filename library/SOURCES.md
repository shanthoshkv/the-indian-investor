# Sources read for the screens

The skills cite a page or a file that was opened. A PDF in this folder stays on the machine. `library/*.pdf` is gitignored. This note is the file that is tracked.

## Saved locally and read

- `library/nber-w23394.pdf`. Kewei Hou, Chen Xue, and Lu Zhang, "Replicating Anomalies", NBER working paper 23394, downloaded from `https://www.nber.org/system/files/working_papers/w23394/w23394.pdf`. Appendix A.4.21 restates the nine annual signals in Piotroski (2000). That restatement is what `screen-piotroski` uses. The quarterly score in A.4.22 and the failure-probability equation in A.4.23 are not skills. The Journal of Accounting Research PDF of Piotroski (2000) was not downloaded.
- `library/altman-z-score-notes.pdf`. Edward Altman, notes on the Z-score models, NYU faculty archive, `https://archive.nyu.edu/bitstream/2451/26762/2/S-CDM-02-11.pdf`. `screen-altman` uses the 1968 Z equation, the private-firm Z' equation, and the four-variable Z'' equation as those notes print them. The zone numbers that blogs attach to Z' and the upper bound blogs attach to Z'' were not in this file. They are not in the skill. The file does not state a license to republish it, so the PDF stays local.
- SEBI Investor, "How to Manage Investment Risks", `https://investor.sebi.gov.in/investment_risk_managment.html`. Fetched as HTML. `review-diversification` uses that page. The page prints no stock count.

## Not downloaded

Copyrighted books stay out of this repo. Where a public checklist was already written into a skill, the skill is named. The book text was not copied.

| Work | Why it is not in `library/` | Where a public checklist already lives |
| --- | --- | --- |
| Graham, *The Intelligent Investor* and *Security Analysis* | Copyrighted. US-dollar defensive cutoffs were not opened, so they are not a skill. | `lens-buffett`, `lens-damani` |
| Fisher, *Common Stocks and Uncommon Profits* | Copyrighted. | None. Scuttlebutt is not a filing. |
| Lynch, *One Up on Wall Street* | Copyrighted. | None. |
| Greenblatt, *The Little Book That Beats the Market* | Copyrighted. The magic-formula page was not opened. | None. No earnings-yield cutoff was added. |
| Munger, *Poor Charlie's Almanack* | Copyrighted. | `lens-munger` |
| Berkshire Hathaway letters | The letters are Buffett's. They were not vendored. | `lens-buffett` |
| Mukherjea, Coffee Can books | Copyrighted. The screen uses his public two-metric statement. | `screen-coffee-can` |
| Prasad, *What I Learned About Investing from Darwin* | Copyrighted. | `lens-prasad` |
| Baid, *The Joys of Compounding*; Parikh, *Stocks to Riches*; Pabrai, *The Dhandho Investor*; Klarman, *Margin of Safety* | Copyrighted. No public checklist was opened for a new skill. | None |
| SEBI Financial Education Booklet (November 2020) | The booklet says reproduction needs the publisher's written permission. | The HTML risk page above, not the booklet |
| Beneish (1999), *Financial Analysts Journal* | The paper was not opened. Coefficients repeated on blogs were not copied. | None |
| Sloan (1996) on accruals | The paper was not opened. | The binary accrual test inside `screen-piotroski` is Piotroski's, not Sloan's continuous ratio |
| Markowitz (1952) | The paper was not opened. | `review-diversification` is the SEBI page, not an optimizer |
| Evans and Archer; Statman, on how many stocks | Those papers were not opened. | No stock-count cutoff |
| Campbell, Hilscher, and Szilagyi (2008) | Equation A10 is in the NBER PDF and needs prices and an index this pack will not invent. | None |
| Damodaran's teaching files | A page he offers for download was not opened in this pass. | None. No discount rate and no industry ERP |
| KMV expected default frequency | The Altman notes describe distance to default. The map from that distance to a probability is KMV's database and is not a formula in the file. | None |
