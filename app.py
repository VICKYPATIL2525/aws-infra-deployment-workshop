import streamlit as st

st.set_page_config(page_title="AWS Deployment Demo", page_icon="☁️", layout="centered")

st.title("☁️ AWS Deployment Demo")
st.caption("This is a demo project showcasing Python app deployment on AWS.")

st.divider()

# About
st.header("📌 About This Project")
st.info(
    "This Streamlit app is a **demo project** built to explore and showcase "
    "how Python web applications can be containerized and deployed on **AWS** — "
    "using services like **Elastic Beanstalk**, **ECS (Fargate)**, or **EC2**."
)

st.divider()

# AWS Deployment Notes
st.header("📝 Deployment Notes")

with st.expander("🔧 Steps to Deploy on AWS", expanded=True):
    st.markdown("""
1. **Containerize** — Write a `Dockerfile` to package the app
2. **Push to ECR** — Upload your Docker image to Amazon Elastic Container Registry
3. **Choose a service:**
   - `EC2` — Full control, manual setup
   - `Elastic Beanstalk` — Easy PaaS, good for beginners
   - `ECS / Fargate` — Serverless containers, no infra management
4. **Configure env variables** — Use AWS Parameter Store or `.env`
5. **Set up a Load Balancer** — For production traffic handling
6. **Enable auto-scaling** — Let AWS scale based on traffic
7. **Monitor with CloudWatch** — Logs, metrics, alarms
    """)

with st.expander("💡 Tips & Best Practices"):
    st.markdown("""
- Always use **IAM roles** instead of hardcoding AWS credentials
- Use **S3** for static assets and file storage
- Enable **HTTPS** via AWS Certificate Manager (ACM) + ALB
- Keep your Docker images **small** — use slim base images
- Use **multi-stage builds** in Dockerfiles to reduce image size
- Tag your AWS resources — it saves headaches in billing reports
- Set up **CloudWatch alarms** before going to production
    """)

with st.expander("⚠️ Common Gotchas"):
    st.markdown("""
- Forgetting to open the right **security group ports** (usually 8501 for Streamlit)
- Using the wrong **AWS region** for your resources
- Not setting `server.headless = true` in Streamlit config for cloud deployments
- Overlooking **VPC subnet** settings when services can't talk to each other
- Ignoring **cost alerts** — AWS bills can surprise you 😬
    """)

st.divider()

# Fun Section
st.header("😄 AWS Jokes (Because Why Not)")

jokes = [
    ("Why did the developer go broke?", "Because he left his EC2 instances running over the weekend."),
    ("What's a cloud engineer's favorite movie?", "\"There Will Be Bandwidth\""),
    ("Why don't AWS engineers ever get lost?", "Because they always follow the Route 53."),
    ("How many AWS services does it take to host a Hello World app?", "Approximately 12. Plus a Lambda just in case."),
]

for q, a in jokes:
    with st.expander(f"🤔 {q}"):
        st.write(f"**{a}**")

st.divider()

# Quick Reference
st.header("📚 Quick Reference")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Useful AWS Services")
    st.markdown("""
- **EC2** — Virtual machines
- **ECS / Fargate** — Containers
- **Elastic Beanstalk** — PaaS
- **S3** — Object storage
- **RDS** — Managed databases
- **CloudWatch** — Monitoring & logs
- **IAM** — Access management
    """)

with col2:
    st.subheader("Streamlit on AWS Tips")
    st.markdown("""
- Default port: **8501**
- Use `--server.headless true` flag
- Set `STREAMLIT_SERVER_PORT` env var
- ALB health check path: `/healthz`
- Docker base image: `python:3.11-slim`
- Store secrets in **AWS Secrets Manager**
- Use **ECR** for private image registry
    """)

st.divider()
st.success("✅ If you can see this page — the deployment worked!")
st.caption("Demo Python App · AWS Deployment Demo · Built with Streamlit")
