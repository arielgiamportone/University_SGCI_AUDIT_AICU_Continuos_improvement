# Fishing Engineering Quality Improvement Dashboard

## Overview

This repository contains a Streamlit dashboard designed to analyze and visualize key performance indicators related to the quality of Fishing Engineering education programs. The analysis and visualization are based on simulated data reflecting real-world metrics that are critical for academic quality assurance and continuous improvement.

## Context

### AUDIT y AICU certifications

The dashboard integrates concepts from two prominent certification systems:

- **AUDIT**: A quality assurance system for university management that emphasizes continuous improvement, focusing on areas such as teaching, research, and management processes.
- **AICU**: Accreditation for Continuous Improvement, which is centered on meeting and exceeding educational standards, fostering an environment of self-assessment, and promoting sustainable enhancement of academic programs.

Both certification systems are crucial for maintaining high standards in university education, ensuring that institutions are not only compliant with regulatory requirements but also engaged in ongoing enhancement of their educational offerings.

## Data Simulation

To demonstrate the functionality and benefits of the dashboard, we have generated simulated data using the `Faker` library. This data includes key performance indicators such as:

- Graduation rate
- Student satisfaction
- Compliance rate
- Audit score
- Accreditation score
- Employability
- Technical skills
- Soft skills
- Fishing engineering competence

These indicators provide a comprehensive view of the academic quality and outcomes specific to Fishing Engineering programs.

## Dashboard Features

### Annual Average Scores Trends

The dashboard displays trends over the years for each key performance indicator, allowing users to see how metrics have evolved and identify areas for improvement.

### Distribution of Scores

Visualizing the distribution of scores helps in understanding the variability and consistency of the key performance indicators across different years and institutions.

### Compare Institutions

Users can select multiple institutions and compare their performance across different indicators. This feature is particularly useful for benchmarking and identifying best practices.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- `pip` for managing Python packages

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fishing-engineering-dashboard.git
    cd fishing-engineering-dashboard
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Generate the simulated data:
    ```bash
    python generate_fishing_data.py
    ```

5. Run the Streamlit dashboard:
    ```bash
    streamlit run fishing_dashboard.py
    ```

## Conclusion

This dashboard serves as a powerful tool for institutions offering Fishing Engineering programs to monitor and enhance their educational quality. By leveraging the principles of AUDIT and AICU certifications, the dashboard promotes a culture of continuous improvement and excellence in higher education.

Feel free to contribute to this project by submitting issues or pull requests. We welcome any feedback and suggestions for further enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.