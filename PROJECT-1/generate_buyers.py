import pandas as pd

data = {
    "username": ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "visual_user", "error_user"],
    "password": ["secret_sauce"] * 6
}

df = pd.DataFrame(data)
df.to_excel("buyers.xlsx", index=False)
print("✅ buyers.xlsx created")

