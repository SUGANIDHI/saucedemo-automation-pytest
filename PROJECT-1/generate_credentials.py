import pandas as pd

users = [
    "standard_user", "locked_out_user", "problem_user",
    "performance_glitch_user", "error_user", "visual_user"
]

df = pd.DataFrame({
    "username": users,
    "password": ["secret_sauce"] * len(users)
})
df.to_excel("credentials.xlsx", index=False)
print("✅ credentials.xlsx created.")
