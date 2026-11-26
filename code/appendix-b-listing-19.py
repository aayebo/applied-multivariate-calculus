from pathlib import Path
import pandas as pd

Path("results").mkdir(exist_ok=True)
summary = pd.DataFrame({"method": ["quadrature", "exact"],
                        "integral": [I, 1/3]})
summary.to_csv("results/integration_comparison.csv", index=False)
print(summary)
