# ----------Base Image----------------
FROM python:3.10-slim

#--------Enviornment-----------------

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#---------System dependencies---------

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


# -------------Create non-root user-------------------

RUN useradd -m appuser

# --------Set working directory

WORKDIR /app

#------Install dependencies------------

# copy only requirements first (for caching)

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---------Copy Applications----------
COPY . .

# ---------------Set permission ------------

RUN chown -R appuser:appuser /app

# Switch to no-root user

USER appuser

# ----------Expose Port--------

EXPOSE 8000

# --------------------Start FASTAPI------------

CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
