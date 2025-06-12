from fastapi import HTTPException
from collections import defaultdict
import time

rate_limits = defaultdict(list)

def check_rate_limit(ip: str):
    now = time.time()
    window = 60  # 1 minute
    max_requests = 5

    rate_limits[ip] = [t for t in rate_limits[ip] if now - t < window]
    if len(rate_limits[ip]) >= max_requests:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    rate_limits[ip].append(now)
