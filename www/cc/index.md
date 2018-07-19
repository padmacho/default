# Cloud Computing.
# [Continuous Delivery](Continuous-Delivery.html)

# Introduction to Cloud Computing
 - Service Orientation
     - Rent - **Don't Own**
         - No upfront cost
         - Minimize lock-in
         - Swapability
     - Leverage- **Don't Build**
         - Offload Operational Burden
         - Usually Cheaper
     -  **Always look at using the service first**

# Cloud Native Application Design
- Agility
    - Deploy in minutes vs weeks
    -  Support next-generation development paradigms
- Elasticity
    - Scale capacity based on demand
    - Accommodate variable seasonality for workloads (e.g. daily, weekly)
- Resiliency
    - Fault tolerant, "always on" Services
    - Fast response and recovery times
- Flexible Pricing
    - 'Pay-as-you-go': Only pay for those service consumed.
    -  Charges can accrue per minute, per hour, per moth, etc..
- Location Independence
    - Workloads are not dependent on running in a fixed location
    - Workloads can migrate seamlessly between environments
- Automation
    - End to end service Automation (e.g provisioning, scaling, decommission)
    - Menu of fully self-service options available for consumption
- Multi Tenancy
    - Infrastructure resources are shared across multiple customers
    - Efficient utilization of physical hardware

#  Cloud Native Application Design - Responsibilities
- Benefits of cloud are not free
- Agility , elasticity, resiliency must be **engineered into applications**
- The Could Native Maturity Model provides a guide:
    - Applications are **not** formally scored, it is merely a guide
    - Minimum bar to entry up to a micro service based architecture model
    - Some applications will never need to meet Level 3

# Cloud Maturity Model (CMM)
Level | Description
--- | ---
3 (Cloud Native) | - Micro service architecture and principals - API first Design
2  (Cloud Resilient) | - Design for failure , - Apps are unaffected by dependent service failure,  - Metrics and monitoring baked in , - Cloud agnositc implementation
1 (Cloud Friendly) | - Twelve Factor applications, - Horizontal scalability, - Leverage Platform HA
0 (Cloud Ready) | - No file system (NAS/SAN), use API based storage, e.g. S3. , - Self contained applications, - Platform managed ports and addressing,- Consume off platform services using platform semantics

# 12 Factor principles
- **Code base**. One code base tracked in revision control, many deploys.
- **Dependencies** - Explicitly declare and isolate dependencies
- **Configuration** - Store configuration in the environment
- **Backing Services** - Treat backing services as attached resources.
- **Build, release, run** - Strictly separate build and run stages
- **Process** - Execute the app as one or more stateless processes
- **Port binding** - Export services via port binding
- **Concurrency**- Scale out via the process Model
- **Disposability** - Maximize robustness with fast startup and graceful shutdown
- **Dev/Prod parity** - Keep development, staging and production as similar as possible
- **Logs** - Treat logs as event streams
- **Admin processes** - Run admin/management tasks as one-off processes

# Overview
 - Cloud is powerful but not magic. You need to design and code to get the benefits of cloud.
 - 12 Factors
 - Cloud platform services , speeds up development
 - Remember not to leave services running as this will cost for every minute





- API
- Micro Services

# Infrastructure Contract
- Availability
- Resiliency
- Security
# Decomposing Monolithic Application
# Container Delivery model
