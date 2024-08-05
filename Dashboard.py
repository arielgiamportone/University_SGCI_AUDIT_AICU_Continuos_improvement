import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
df = pd.read_csv('fishing_engineering_quality_data.csv')

# Asegurarse de que la columna 'year' es de tipo int para el agrupamiento
df['year'] = df['year'].astype(int)

# Seleccionar solo columnas numéricas
numeric_columns = [
    'graduation_rate', 'student_satisfaction', 'compliance_rate', 'audit_score',
    'accreditation_score', 'employability', 'technical_skills', 'soft_skills',
    'fishing_engineering_competence'
]
numeric_df = df[numeric_columns + ['year']]

# Promedios anuales
annual_means = numeric_df.groupby('year').mean()

# Función para crear las distribuciones
def plot_distributions(data):
    fig, axs = plt.subplots(3, 3, figsize=(18, 12))
    sns.histplot(data['graduation_rate'], bins=30, ax=axs[0, 0]).set_title('Graduation Rate Distribution')
    sns.histplot(data['student_satisfaction'], bins=30, ax=axs[0, 1]).set_title('Student Satisfaction Distribution')
    sns.histplot(data['compliance_rate'], bins=30, ax=axs[0, 2]).set_title('Compliance Rate Distribution')
    sns.histplot(data['audit_score'], bins=30, ax=axs[1, 0]).set_title('Audit Score Distribution')
    sns.histplot(data['accreditation_score'], bins=30, ax=axs[1, 1]).set_title('Accreditation Score Distribution')
    sns.histplot(data['employability'], bins=30, ax=axs[1, 2]).set_title('Employability Distribution')
    sns.histplot(data['technical_skills'], bins=30, ax=axs[2, 0]).set_title('Technical Skills Distribution')
    sns.histplot(data['soft_skills'], bins=30, ax=axs[2, 1]).set_title('Soft Skills Distribution')
    sns.histplot(data['fishing_engineering_competence'], bins=30, ax=axs[2, 2]).set_title('Fishing Engineering Competence Distribution')
    plt.tight_layout()
    return fig

# Función para crear las tendencias
def plot_trends(data):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(data.index, data['graduation_rate'], label='Graduation Rate')
    ax.plot(data.index, data['student_satisfaction'], label='Student Satisfaction')
    ax.plot(data.index, data['compliance_rate'], label='Compliance Rate')
    ax.plot(data.index, data['audit_score'], label='Audit Score')
    ax.plot(data.index, data['accreditation_score'], label='Accreditation Score')
    ax.plot(data.index, data['employability'], label='Employability')
    ax.plot(data.index, data['technical_skills'], label='Technical Skills')
    ax.plot(data.index, data['soft_skills'], label='Soft Skills')
    ax.plot(data.index, data['fishing_engineering_competence'], label='Fishing Engineering Competence')  # Añadir la competencia específica
    ax.set_xlabel('Year')
    ax.set_ylabel('Scores')
    ax.set_title('Annual Average Scores Trends')
    ax.legend()
    return fig

# Función para comparar instituciones
def plot_compare_institutions(data, institutions, indicators):
    fig, axs = plt.subplots(len(indicators), 1, figsize=(12, 8 * len(indicators)))
    if len(indicators) == 1:
        axs = [axs]
    for i, indicator in enumerate(indicators):
        for institution in institutions:
            inst_data = data[data['institution'] == institution]
            axs[i].plot(inst_data['year'], inst_data[indicator], label=f'{institution}')
        axs[i].set_xlabel('Year')
        axs[i].set_ylabel(indicator)
        axs[i].set_title(f'{indicator} Comparison')
        axs[i].legend()
    plt.tight_layout()
    return fig

# Configurar el dashboard en Streamlit
st.title('Fishing Engineering Quality Improvement Dashboard')

st.write('## Annual Average Scores Trends')
st.pyplot(plot_trends(annual_means))

st.write('## Distribution of Scores')
st.pyplot(plot_distributions(df))

st.write('## Detailed Data')
st.dataframe(df)

if st.checkbox('Show Analysis Summary'):
    st.write(annual_means.describe())

st.write('## Compare Institutions')
selected_institutions = st.multiselect('Select Institutions', df['institution'].unique())
selected_indicators = st.multiselect('Select Indicators', numeric_columns, default=numeric_columns)

if selected_institutions and selected_indicators:
    st.pyplot(plot_compare_institutions(df, selected_institutions, selected_indicators))

if st.checkbox('Show Raw Data for Selected Institutions'):
    if selected_institutions:
        st.write(df[df['institution'].isin(selected_institutions)])
    else:
        st.write("Select institutions to see the raw data.")
